#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(x) x.begin(),x.end()
#define sz(x) (int)(x.size())
#define LL long long
#define mp make_pair
#define pb push_back
#define f first
#define s second

using namespace std;

const int N = 1e5 + 7;
const int mod = 1e9 + 7;

int T, ans;
string s;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
    cin >> T;
    for(int it = 1; it <= T; ++it) {
      cin >> s;
      ans = 0;
      forn(i, sz(s)) {
        if(i == 0 || s[i] == s[i-1]) 
          continue;
        ans++;
      }
      if(s[sz(s) - 1] == '-') 
        ans++;
      printf("Case #%d: %d\n", it, ans);
    }
  return 0;
}
