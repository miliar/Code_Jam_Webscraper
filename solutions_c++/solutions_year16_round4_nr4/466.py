//CONTEST SOURCE
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
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
#define pdd pair<double, double>
int n, t;
char a[5][5];
char b[5][5];
int main() {
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n;
    for(int i = 0; i < n; ++i) cin >> a[i];

    int best = 1e9;
    for(int mask = 0; mask < (1 << (n * n)); ++mask) {
      int bit = 0, bits = 0;
      for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
          b[i][j] = a[i][j];
          if (mask & (1 << bit)) {
            b[i][j] = '1';
            ++bits;
          }
          ++bit;
        }
      }
      if (bits > best) continue;

      vector<int> ord(0);
      for(int i = 0; i < n; ++i) {
        ord.pb(i);
      }
      bool can_break = 0;
      do {
        for(int guy = 0; guy < n; ++guy) {
          vector<int> take(0);
          for(int i = 0; i < n; ++i) {
            if (b[ord[guy]][i] == '1') {
              take.pb(i);
            }
          }
          do {
            vector<int> cpy = take;
            for(int i = 0; i < guy; ++i) {
              for(int j = 0; j < L(cpy); ++j) {
                if (b[ord[i]][cpy[j]] == '1') {
                  swap(cpy[j], cpy.back());
                  cpy.pop_back();
                  break;
                }
              }
            }
            if (L(cpy) == 0) can_break = 1;
            if (can_break) break;
          } while(next_permutation(all(take)));
          if (can_break) break;
        }
        if (can_break) break;
      } while(next_permutation(all(ord)));
      if (can_break) continue;
      best = bits;
    }
    cout << "Case #" << tc << ": " << best << endl;
  }
}

