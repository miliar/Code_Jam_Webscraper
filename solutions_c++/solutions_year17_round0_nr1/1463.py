
#include <bits/stdc++.h>
  
using namespace std;
#define forn(i, n) for (int i = 0; i < n; i++)
#define re return
#define fi first
#define mp make_pair
#define se second
#define sz(a) (int)a.size()
#define tm tmmm
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const ll mod = ll(1e9) + 7, p = 239;
const int ma = 16 * 1024;

int t;

int main() {
   iostream::sync_with_stdio(0);
   //freopen("a.in", "r", stdin);
   //freopen("a.out", "w", stdout);
   cin >> t;
   forn (i, t) {
      int k;
      string s;
      cin >> s >> k;
      int ans = 0;
      bool ok = true;
      for (int i = 0; i < sz(s); i++) {
         if (s[i] == '-') {
            ans++;
            if (i + k > sz(s)) {ok = false; break;}
            for (int j = i; j < i + k; j++) {
               if (s[j] == '-') {
                  s[j] = '+';
                  continue;
               }
               s[j] = '-';
            }
         }
         //cout << s << "\n";
      }
      cout << "Case #" << i + 1 << ": ";
      if (ok) {
         cout << ans << "\n";
      } else {
         cout << "IMPOSSIBLE\n";
      }
   } 
}

