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

ll get(ll x) {
   for(ll i = 2; i * i <= x; i++) {
      if(x % i == 0) {
         return i;
      }
   }
   return -1;
}

vector<ll> base(string s) {
   vector<ll> v;
   for(int j = 2; j <= 10; j++) {
      ll cur=0;
      for(int i = 0; i < s.size(); i++)
         cur=cur*j+(s[i]-'0');
      v.pb(get(cur));
      if(v.back()==-1)return v;
   }
   return v;
}

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
      cin >> n >> m;
      cout << "Case #" << ++t << ":\n";
      for(int i = 0; i < (1 << (n - 2)); i++) {
         string c = "1";
         for(int j = 0; j < n - 2; j++) {
            if((i >> j) % 2) c += "1";
            else c += "0";
         }
         c += "1";
         vector<ll> cur = base(c);
         bool ok = 1;
         for(int j = 0; j < sz(cur); j++) {
            if(cur[j] == -1) {
               ok = 0;
               break;
            }
         }
         if(ok) {
            cout << c << " ";
            for(int j = 0; j < sz(cur); j++)
               cout << cur[j] << ' ';
            cout << endl;
            m--;
            if(m == 0) break;
         }
      }
   }
   return 0;
}

