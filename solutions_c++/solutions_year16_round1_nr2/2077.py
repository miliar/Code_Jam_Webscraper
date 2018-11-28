#include <string>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int nextInt() {
  int x;
  scanf("%d", &x);
  return x;
}

string nextstring() {
  char buf[11111];
  scanf("%s", buf);
  return buf;
}

vector<pair<vector<int>, vector<int> > > makePairs(int n, vector<vector<int> > a) {
  vector<pair<vector<int>, vector<int> > > res(n);
  for (int idx = 0; idx < n; ++idx) {
    int min_value = a[0][idx];
    for (int i = 0; i < a.size(); ++i) {
      if (min_value > a[i][idx]) {
        min_value = a[i][idx];
      }
    }
    vector<vector<int> > x, y;
    for (int i = 0; i < a.size(); ++i) {
      if (a[i][idx] == min_value) {
        x.push_back(a[i]);
      } else {
        y.push_back(a[i]);
      }
    }
    a = y;

    res[idx].first = x[0];
    if (x.size() > 1) {
      res[idx].second = x[1];
    }
  }
  return res;
}


vector<int> solve(int n, vector<vector<int> >& a) {
  vector<pair<vector<int>, vector<int> > > p = makePairs(n, a);

  for (int i = 0; i < p.size(); ++i) {
    if (p[i].second.size() == 0) {
      vector<int> res(n, -1);
      res[i] = p[i].first[i];
      for (int j = 0; j < n; ++j) {
        if (j != i) {
          res[j] = p[j].second[i] == p[i].first[j]
              ? p[j].first[i]
              : p[j].second[i];
        }
      }
      return res;
    }
  }
  cerr << "BOTVA!";
  return vector<int>();
}

int main() {
  int T = nextInt();
  for (int test_number = 1; test_number <= T; ++test_number) {
    cerr << test_number << endl;
    int n = nextInt();
    vector<vector<int> > a(2 * n - 1);
    for (int i = 0; i < a.size(); ++i) {
      a[i].resize(n);
      for (int j = 0; j < n; ++j) {
        a[i][j] = nextInt();
      }
    }

    vector<int> res = solve(n, a);
    printf("Case #%d:", test_number);
    for (int i = 0; i < n; ++i) {
      printf(" %d", res[i]);
    }
    printf("\n");
  }
  return 0;
}
