#include <bits/stdc++.h>

#define left nadnlassad
#define right asdaslknd
#define y1 kjdajasjdsas

#define pb push_back
#define mp make_pair

#define f first
#define s second

#define ll long long
#define ld long double
#define ull unsigned ll

#define _hash pair<ll, ull>
#define pii pair<int, int>
#define prr pair<pii, pii>

#define sqr(x) ((x) * 1LL * (x))

#define vec vector<int>
#define sz(v) int(v.size())
#define all(v) v.begin(), v.end()
#define endl "\n";
#define iter set<int>::iterator
#define _bits(x) __builtin_popcountll(x)

using namespace std;

const int nx[8] = {2, -2, -2, 2, 1, 1, -1, -1};
const int ny[8] = {1, 1, -1, -1, 2, -2, -2, 2};

const ll LINF = (ll) 3e18;
const int INF = 1e9 + 7;

const int N = 1e5 + 100; // change this !!!
const int MAXN = 5e7 + 50;
const double EPS = 1e-9, PI = 2 * acos(0.0);


int main() {
   #define fname "triples"
   #ifdef sony
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
   #else
      //freopen(fname".in", "r", stdin);
      //freopen(fname".out", "w", stdout);
   #endif // sony
   srand(time(0));
   ios_base::sync_with_stdio(0), cin.tie(0);
   int cases, t = 0, n, m;
   string s;
   cin >> cases;
   while(cases--) {
      cin >> s;
      cout << "Case #" << ++t << ": ";
      int ans = 0, j = 0;
      for(int i = s.size() - 1; i >= 0; i--) {
         int cur = (s[i] == '+');
         cur ^= j;
         if(!cur) {
            ans++;
            j ^= 1;
         }
      }
      cout << ans << "\n";
   }
   return 0;
}

