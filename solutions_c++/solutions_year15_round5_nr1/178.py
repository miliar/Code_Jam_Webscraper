// tested by Hightail: https://github.com/dj3500/hightail
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <cassert>
using namespace std;
#define pb push_back
#define INF 1001001001
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define DBG(vari) //cerr<<"["<<__LINE__<<"] "<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (__typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

namespace rmq {
// RMQ na przedziale od 0 do n-1
// przed uzyciem ustawic MAXX, n i odpalic init
// zwieksz zwieksza wartosci z przedzialu [aw,bw] o x
// getmax zwraca maximum z przedzialu [aw,bw]
// MAXX - 2 * (najmniejsza potega dwojki wieksza od n) + 10

#define MAXX (1 << 21)
ll incr[MAXX], maxn[MAXX];
int n;

void init () { FOR(i,MAXX) incr[i] = maxn[i] = 0; }

int aw,bw,x; // temp

void zwieksz2 (int v, int a, int b) {
   if (aw > b || bw < a) return;
   if (a >= aw && b <= bw) {
      incr[v] += x;
      maxn[v] += x;
   } else {
      int mid = (a+b)/2;
      zwieksz2(2*v, a, mid);
      zwieksz2(2*v+1, mid+1, b);
      maxn[v] = incr[v] + max(maxn[2*v], maxn[2*v + 1]);
   }
}

void zwieksz (int _aw, int _bw, int _x) {
   aw = _aw; bw = _bw; x = _x;
   zwieksz2(1,0,n-1);
}

ll getmax (int v, int a, int b) {
   if (aw > b || bw < a) return (ll)-INF * INF;
   if (a >= aw && b <= bw) {
      return maxn[v];
   } else {
      int mid = (a+b)/2;
      return incr[v] + max(getmax(2*v, a, mid), getmax(2*v+1, mid+1, b));
   }
}

ll getmax (int _aw, int _bw) {
   aw = _aw; bw = _bw;
   return getmax(1,0,n-1);
}
};
int n;
const int N = 1000007;
ll S[N], Rs, Rm, As, Am, Cs, Cm, M[N], D;
vi adj[N];
void dfs (int v, ll mi, ll ma) {
    DBG(v)
    REMIN(mi, S[v]);
    REMAX(ma, S[v]);
    int a = max(0LL, ma - D);
    int b = min(mi, 1000000LL);
    if (a <= b) rmq::zwieksz(a, b, 1);
    FOREACH(it,adj[v]) {
        dfs(*it, mi, ma);
    }
}

int main () {
    wez(te)
    FORI(testno,te) {
        printf("Case #%d: ", testno);
        //return 0;
        cin >> n >> D >> S[0] >> As >> Cs >> Rs >> M[0] >> Am >> Cm >> Rm;
        REP(i,0,n-2) {
            S[i+1] = (S[i] * As + Cs) % Rs;
            M[i+1] = (M[i] * Am + Cm) % Rm;
        }
        //DBG(vi(S,S+n));
        //DBG(vi(M,M+n));
        FOR(i,n) adj[i].clear();
        REP(i,1,n-1) {
            adj[M[i] % i].pb(i);
        }
        DBG("ok");
        rmq::n = 1000001;
        rmq::init();
        DBG("ok");
        dfs(0, INF, -INF);
        DBG("ok");
        ll res = rmq::getmax(0, rmq::n - 1);
        DBG("ok");
        cout << res << "\n";
        cerr << testno << " done\n";
    }
}
