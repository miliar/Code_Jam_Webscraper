#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

short d[20000][10000];
char s[20005];

int main(int argc, char* argv[]) {
  int TEST_FROM = 0;
  int TEST_TO = 123456789;
  if (argc == 3) {
    sscanf(argv[1], "%d", &TEST_FROM);
    sscanf(argv[2], "%d", &TEST_TO);
  }
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    scanf("%s", s);
    if (test < TEST_FROM || test > TEST_TO) continue;
    cerr << test << endl;
    printf("Case #%d: ", test);
    memset(d, 0, sizeof(d));
    int n = strlen(s);
    int res = n/2*5;
    vector<char> x;
    for (int i = 0; i < n; ++i) {
      if (!x.empty() && x.back() == s[i]) {
        res += 5;
        x.pop_back();
      } else x.push_back(s[i]);
    }
    cout << res << endl;
/*    for (int l = 2; l <= n; l += 2) {
//      cerr << l << ' '
      int l2 = l / 2;
      for (int i = 0; i + l <= n; ++i) {
        d[i][l2] = d[i+1][l2-1] + 1;
        if (s[i] == s[i+l-1]) d[i][l2] += 1;
        for (int j = 1; j < l2; ++j) {
          short x = d[i][j] + d[i+2*j][l2-j];
          d[i][l2] = max(d[i][l2], x);
        }
      }
    }
    cout << 5*d[0][n/2] << endl;*/
  }
  return 0;
}
