#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};
//////////////////////

void arquivo() {
  freopen("","r",stdin);
  freopen("","w",stdout);
}

const int N = 17;

vector< vector<ll> > g[17];

ll goBase(ll x, ll i) {
  ll novo = 0;
  ll pot = 1LL;
  while(x) {
    if(x % 2LL == 1LL) novo += pot;
    x /= 2LL;
    pot *= i;
  }
  return novo;
}

ll test(ll x) {
  for(ll i = 2; i * i <= x; ++i) {
    if(x % i == 0) return x / i;
  }
  return -1;
}

void ok(ll len, ll x) {
  vi coins;
  coins.pb(goBase(x, 10));
  for(ll i = 2; i <= 10; ++i) {
    ll bas = goBase(x, i);
    ll divi = test(bas);
    if(divi == -1) return;
    coins.pb(divi);
  }
  g[len].pb(coins);
}

void go(ll n) {
  for(ll i = 0; i < (1LL << n); ++i) {
    if((i % 2LL == 0LL) || ((1LL << (n - 1LL)) & i ) == 0) continue;
    ll num = 0;
    for(ll j = 0; j < n; ++j) if((i >> j) & 1) num |= (1LL << j);
    ok(n, num);
    if(g[n].size() >= 50) return;
  }
}


inline void main2() {
  int n, m; scanf("%d %d", &n, &m);
  for(int i = 0; i < m; ++i) {
    for(int j = 0; j < g[n][i].size(); ++j) printf("%lld ", g[n][i][j]);
    printf("\n");
  }
}

int main() {
  for(int i = 16; i <= 16; ++i) go(i);
  int t; scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    printf("Case #%d:\n", i);
    main2();
  } 
  return 0;
}