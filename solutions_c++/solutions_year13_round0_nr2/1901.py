#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
   int n, m;
   cin >> n >> m;
   vector< vector<int> > a(n, vector<int> (m, 0));
   for (int i = 0; i < n; ++i)
       for (int j = 0; j < m; ++j)
           cin >> a[i][j];
   for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j) {
          bool ok1 = true;
          for (int k = 0; k < n; ++k)
              if (a[k][j] > a[i][j])
                  ok1 = false;
          bool ok2 = true;
          for (int k = 0; k < m; ++k)
              if (a[i][k] > a[i][j])
                  ok2 = false;
          if ((!ok1) && (!ok2)) {
               cout << "NO" << endl;
               return;
          }
      }
      cout << "YES" << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
