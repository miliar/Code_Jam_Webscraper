#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

void print(vector<vector<int> > h) {
  for (int i = 0; i < int(h.size()); ++i) {
    for (int j = 0; j < int(h[i].size()); ++j) {
      cerr << h[i][j] << " ";
    }
    cerr << endl;
  }
}

void print(vector<int> v) {
  for (int i = 0; i < int(v.size()); ++i) {
    cerr << v[i] << " ";
  }
  cerr << endl;
}

vector<int> get_col(const vector<vector<int> >& h, int j) {
  vector<int> col;
  for (int i = 0; i < int(h.size()); ++i) {
    col.push_back(h[i][j]);
  }
  return col;
}

vector<int> get_row(const vector<vector<int> >& h, int i) {
  return h[i];
}

bool less_than(vector<int> u, vector<int> v) {
  for (int i = 0; i < int(u.size()); ++i) {
    if (u[i] >= v[i] && u[i] != -1 && v[i] != -1) return false;
  }
  return true;
}

bool ok_col(const vector<vector<int> >& h, int j, vector<int> col) {
  for (int i = 0; i < int(col.size()); ++i) {
    if (h[i][j] != -1 && h[i][j] != col[i]) return false;
  }
  if (j - 1 >= 0) {
    vector<int> col1 = get_col(h, j - 1);
    if (!less_than(col1, col)) return false;
  }
  if (j - 2 >= 0) {
    vector<int> col2 = get_col(h, j - 2);
    if (!less_than(col2, col)) return false;
  }
  return true;
}

bool ok_row(const vector<vector<int> >& h, int i, vector<int> row) {
  for (int j = 0; j < int(row.size()); ++j) {
    if (h[i][j] != -1 && h[i][j] != row[j]) return false;
  }
  if (i - 1 >= 0) {
    vector<int> row1 = get_row(h, i - 1);
    if (!less_than(row1, row)) return false;
  }
  if (i - 2 >= 0) {
    vector<int> row2 = get_row(h, i - 2);
    if (!less_than(row2, row)) return false;
  }
  return true;
}

void set_col(vector<vector<int> >& h, int j, vector<int> col) {
  for (int i = 0; i < int(col.size()); ++i) {
    h[i][j] = col[i];
  }
}

void set_row(vector<vector<int> >& h, int i, vector<int> row) {
  h[i] = row;
}

vector<int> missing;

vector<vector<int> > rec(vector<vector<int> > h, vector<vector<int> > lists, int k) {
  /*
  cerr << "h:" << endl;
  print(h);
  cerr << "lists:" << endl;
  print(lists);
  */
  if (k == int(h.size())) {
    return h;
  }

  int mn_kth = lists[0][k];
  for (int i = 0; i < int(lists.size()); ++i) {
    if (lists[i][k] < mn_kth) {
      mn_kth = lists[i][k];
    }
  }
  vector<int> inds;
  for (int i = 0; i < int(lists.size()); ++i) {
    if (lists[i][k] == mn_kth) {
      inds.push_back(i);
    }
  }
  /*
  cerr << "inds:" << endl;
  print(inds);
  cerr << "-----" << endl;
  */
  if (inds.size() == 1) {
    if (ok_col(h, k, lists[inds[0]])) {
      vector<vector<int> > h_mrow = h;
      set_col(h_mrow, k, lists[inds[0]]);
      vector<vector<int> > lists_mrow = lists;
      lists_mrow.erase(lists_mrow.begin() + inds[0]);
      vector<vector<int> > result = rec(h_mrow, lists_mrow, k + 1);
      if (result.size() > 0) {
        missing = get_row(result, k);
        return result;
      }
    }
    if (ok_row(h, k, lists[inds[0]])) {
      vector<vector<int> > h_mcol = h;
      set_row(h_mcol, k, lists[inds[0]]);
      vector<vector<int> > lists_mcol = lists;
      lists_mcol.erase(lists_mcol.begin() + inds[0]);
      vector<vector<int> > result = rec(h_mcol, lists_mcol, k + 1);
      if (result.size() > 0) {
        missing = get_col(result, k);
        return result;
      }
    }
    return vector<vector<int> >();
  } else if (inds.size() == 2) {
    if (ok_col(h, k, lists[inds[0]]) && ok_row(h, k, lists[inds[1]])) {
      vector<vector<int> > h_cr = h;
      set_col(h_cr, k, lists[inds[0]]);
      set_row(h_cr, k, lists[inds[1]]);
      vector<vector<int> > lists_cr = lists;
      lists_cr.erase(lists_cr.begin() + inds[0]);
      lists_cr.erase(lists_cr.begin() + inds[1] - 1);
      vector<vector<int> > result = rec(h_cr, lists_cr, k + 1);
      if (result.size() > 0) return result;
    }
    if (ok_col(h, k, lists[inds[1]]) && ok_row(h, k, lists[inds[0]])) {
      vector<vector<int> > h_rc = h;
      set_col(h_rc, k, lists[inds[1]]);
      set_row(h_rc, k, lists[inds[0]]);
      vector<vector<int> > lists_rc = lists;
      lists_rc.erase(lists_rc.begin() + inds[0]);
      lists_rc.erase(lists_rc.begin() + inds[1] - 1);
      vector<vector<int> > result = rec(h_rc, lists_rc, k + 1);
      if (result.size() > 0) return result;
    }
    return vector<vector<int> >();
  }
  cerr << "oops: inds.size() = " << inds.size() << endl;
  return vector<vector<int> >();
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n;
    cin >> n;
    vector<vector<int> > lists(2 * n - 1, vector<int>(n));
    for (int i = 0; i < int(lists.size()); ++i) {
      for (int j = 0; j < int(lists[i].size()); ++j) {
        cin >> lists[i][j];
      }
    }

    vector<vector<int> > empty_h(n, vector<int>(n, -1));
    missing = vector<int>();
    vector<vector<int> > h = rec(empty_h, lists, 0);
    if (missing.size() == 0) {
      cerr << "oops: missing is empty" << endl;
    }
    cout << "Case #" << ca << ":";
    for (int i = 0; i < int(missing.size()); ++i) {
      cout << " " << missing[i];
    }
    cout << endl;
  }
}
