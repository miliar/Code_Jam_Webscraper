//CONTEST SOURCE
#include <cstring>
#include <iostream>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
int n, t, k;
double p[22];
int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n >> k;
    for(int i = 0; i < n; ++i) cin >> p[i];
    double bp = 0;
    for(int mask = 0; mask < (1 << n); ++mask) {
      int bits = 0;
      for(int bit = 0; bit < n; ++bit){
        if (mask & (1 << bit)) ++bits;
      }
      if (bits == k) {
        double cur = 0;
        for(int sub = mask; sub > 0; sub = (sub - 1) & mask) {
          int cbit = 0;
          double now = 1;
          for(int i = 0; i < n; ++i ) {
            if (sub & (1 << i)) {
              ++cbit; now *= p[i];
            } else {
              if (mask & (1 << i))
               now *= (1 - p[i]);
            }
          }
          if (cbit == k / 2) cur += now;
        }
        if (cur > bp) bp = cur;
      }
    }
    printf("Case #%d: %0.9lf\n", tc, bp);
  }
}

