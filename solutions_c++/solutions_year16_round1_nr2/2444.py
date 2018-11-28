#include <bits/stdc++.h>

using namespace std;

int n;
vector<vector<int>> a, b;
vector<bool> used;

bool compare_col(int c, int i, int to) {
  for (int r = 0; r < to; ++r) {
    if (b[r][c] != -1 && b[r][c] != a[i][r]) {
      return false;
    }
  }
  return true;
}

bool compare_row(int r, int i) {
  for (int c = 0; c < n; ++c) {
    if (b[r][c] != -1 && b[r][c] != a[i][c]) {
      return false;
    }
  }
  return true;
}

bool put(int cur, int last, bool skipped) {
  for (int i = 0; i < n; ++i) {
    b[last][i] = a[cur][i];
  }
  //bool debug = cur == 1 && last == 1 && !skipped;
  bool debug = false;
  if (debug) {
    for (int i = 0; i <= last; ++i) {
      for (int j = 0; j < n; ++j) cerr << b[i][j] << " ";
      cerr << endl;
    }
    cerr << endl;
  }
  if (last == 0) {
    return true;
  }
  vector<bool> u = used;
  if (debug) {
    for (bool x : u) cerr << x << " "; cerr << endl;
  }
  for (int i = 0; i < n; ++i) {
    bool found = false;
    for (int j = 0; j < (int) a.size(); ++j) {
      if (debug) {
        cerr << "i=" << i << " j=" << j << " " << compare_col(i, j, last + 1) << endl;
      }
      if (!u[j] && compare_col(i, j, last + 1)) {
        u[j] = true;
        found = true;
        break;
      }
    }
    if (!found) {
      if (debug) {
        cout << i << endl;
      }
      if (skipped) {
        return false;
      } else {
        skipped = true;
      }
    }
  }
  return true;
}

vector<int> get_ans(int skip) {
  vector<bool> u = used;
  vector<int> res(n, -1);
  //for (int i = 0; i < n; ++i) {
  //  for (int j = 0; j < n; ++j) {
  //    cerr << b[i][j] << " ";
  //  }
  //  cerr << endl;
  //}
  //cerr << "skip=" << skip << endl;
  //for (int i = 0; i < (int)a.size(); ++i) {
  //  cerr << u[i] << " ";
  //}
  //cerr << endl;
  if (skip != -1) {
    for (int c = 0; c < n; ++c) {
      for (int j = 0; j < (int) a.size(); ++j) {
        if (!u[j] && compare_col(c, j, n)) {
          u[j] = true;
          res[c] = a[j][skip];
          break;
        }
      }
    }
  } else {
    for (int c = 0; c < n; ++c) {
      bool found = false;
      for (int j = 0; j < (int)a.size(); ++j) {
        if (!u[j] && compare_col(c, j, n)) {
          u[j] = true;
          found = true;
          break;
        }
      }
      if (!found) {
        if (skip != -1) return vector<int>();
        skip = c;
      }
    }
    if (skip == -1) return vector<int>();
    for (int r = 0; r < n; ++r) {
      res[r] = b[r][skip];
    }
  }
  for (int i = 0; i < n; ++i) {
    if (res[i] == -1) return vector<int>();
  }
  return res;
}

vector<int> rec(int cur, int last, int skip) {
  //cerr << "cur=" << cur << " last=" << last << " skip=" << skip << endl;
  //for (int i = 0; i < last; ++i) {
  //  for (int j = 0; j < n; ++j) {
  //    cerr << b[i][j] << " ";
  //  }
  //  cerr << endl;
  //}
  //cerr << endl;
  if (last == 0 && cur >= 2) {
    return vector<int>();
  }
  if (cur == (int) a.size()) {
    if (last < n) {
      return vector<int>();
    }
    return get_ans(skip);
  }
  if (last + (int)a.size() - cur < n - 1) {
    return vector<int>();
  }
  if (last < n && skip == -1) {
    for (int i = 0; i < n; ++i) {
      b[last][i] = -1;
    }
    vector<int> ret = rec(cur + 1, last + 1, last);
    if (!ret.empty()) return ret;
  }
  used[cur] = true;
  if (last < n && put(cur, last, skip != -1)) {
    vector<int> ret = rec(cur + 1, last + 1, skip);
    if (!ret.empty()) return ret;
  }
  used[cur] = false;
  return rec(cur + 1, last, skip);
}

int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    cerr << tt << endl;
    cin >> n;
    a = vector<vector<int>>(2 * n - 1, vector<int>(n));
    b = vector<vector<int>>(2 * n - 1, vector<int>(n));
    used = vector<bool>(2 * n - 1);
    for (int i = 0; i < 2 * n - 1; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> a[i][j];
      }
    }
    sort(a.begin(), a.end());
    //for (int i = 0; i < (int)a.size(); ++i) {
    //  for (int x : a[i]) cerr << x << " "; cerr << endl;
    //}
    vector<int> res = rec(0, 0, -1);
    cout << "Case #" << tt << ":";
    for (int x : res) cout << " " << x;
    cout << endl;
  }
}
