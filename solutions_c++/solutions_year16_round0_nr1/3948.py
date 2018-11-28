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
   //ios_base::sync_with_stdio(0), cin.tie(0);
   int cases, t = 0, n;
   scanf("%d", &cases);
   while(cases--) {
      scanf("%d", &n);
      printf("Case #%d: ", ++t);
      if(!n)
         puts("INSOMNIA");
      else {
         set<int> s;
         int a = n;
         while(true) {
            int c = n;
            while(c) {
               s.insert(c % 10);
               c /= 10;
            }
            if(s.size() == 10)
               break;
            n += a;
         }
         printf("%d\n", n);
      }
   }
   return 0;
}

