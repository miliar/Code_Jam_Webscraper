// CONTEST SOURCE
#include <algorithm>
#include <climits>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define pi 2 * acos(0.)
int tc, k;
string s;
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> tc;
  for(int t = 1; t <= tc; ++t) {
    cerr << t << endl;
    cin >> s >> k;
    int ans = 0;
    for(int j = 0; j < L(s); ++j) {
      if (s[j] == '-') {
        if (j + k <= L(s)) {
          for(int i = j; i < j + k; ++i) {
            s[i] ^= ('+'^'-');
          }
          ++ans;
        } else {
          ans = -1;
          break;
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (ans >= 0) cout << ans << endl; else cout << "IMPOSSIBLE\n";
  }
}
