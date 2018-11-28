#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <numeric>
#include <complex>
#include <string>
#include <ctime>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pnt;


#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (LL i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair
#define ALL(a) a.begin(),a.end()
#define V(t) vector < t >
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define ALL(a) a.begin(),a.end()

#define dout(a) cerr << a << endl
#define sout(a) cerr << a << "  "

const double pi = 3.14159265358979323846264338327950288419716939937511;
const double eps = 1e-9;

//*
char ch_ch_ch[1<<20];
inline string gs() {scanf("%s",ch_ch_ch); return string(ch_ch_ch);}
inline string gl() {gets(ch_ch_ch); return string(ch_ch_ch);}
inline int gi() {int x; scanf("%d",&x); return x;}
//*/

const int inf = 1000000000;

// code starts here

int n;
int m;
typedef pair <pnt, int> chu;
V(chu) tin,tout;

const int mod = 1000002013;

V(int) a;

map<int, int> mapa;
int cnt;

int apam[10000];

int cost(int i, int j) {
    int d = j - i;
    LL ras = n + n - d + 1;
    if (d%2 == 0) d/=2;
    else ras/=2;
    return (d*1ll*ras)%mod;
}

V(int) zu;

void solution() {

    int tn = gi();
    FI(it,tn) {
        n = gi();
        m = gi();
        tin.clear();
        tout.clear();
        mapa.clear();
        cnt = 0;
        int old = 0;
        zu.clear();
        FI(i,m) {
            int x,y,c;
            scanf("%d%d%d",&x,&y,&c);
            tin.pb(mp(mp(x,y),c));
            tout.pb(mp(mp(y,x),c));
            old = (old + c *1ll* cost(x,y))%mod;
            zu.pb(x);
            zu.pb(y);
        }
        sort(ALL(zu));
        zu.resize(unique(ALL(zu)) - zu.begin());
        FI(i,zu.size()) apam[i] = zu[i];
        cnt = zu.size();
        sort(ALL(tin));
        sort(ALL(tout));
        a.clear();
        a.resize(cnt,0);
        int res = 0;

        FI(ic,cnt) {
            int cur = apam[ic];
            FI(i,m) if (tin[i].first.first == cur) a[ic] += tin[i].second;
            int toout = 0;
            FI(i,m) if (tout[i].first.first == cur) toout += tout[i].second;
            for (int i = ic; toout && i >= 0; --i) {
                int op = min(toout,a[i]);
                if (op == 0) continue;
                a[i] -= op;
                toout -= op;
                res = (res + op *1ll* cost(apam[i],apam[ic]))%mod;
            }
        }


        printf("Case #%d: ",it+1);
        printf("%d\n",(old + mod - res)%mod);
    }





}


// code ends here

int main(int argc, char** argv) {

#ifdef IGEL_ACM
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    clock_t beg_time = clock();
#else
    //freopen(argv[1],"r",stdin);
    //freopen("painting.in", "r", stdin);
    //freopen("painting.out", "w", stdout);

#endif

    solution();

#ifdef IGEL_ACM
    fprintf(stderr,"*** Time: %.3lf ***\n",1.0*(clock()-beg_time)/CLOCKS_PER_SEC);
#endif

    return 0;
}

