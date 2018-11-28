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


LL n,p;

bool canHigh(LL m, LL n, LL p) {
    if (m < p) return true;
    if (m == n-1) return false;
    return canHigh((m+1)/2,n/2,p);
}

bool canLow(LL m, LL n, LL p) {
    if (m >= p) return true;
    if (m == 0) return false;
    return canLow((m-1)/2,n/2,p-n/2);
}

void solution() {

    int tn = gi();
    FI(it,tn) {
        cin >> n >> p;
        LL l = 0, r = (1ll << n);
        while (l < r) {
            LL m = l + (r-l)/2;
            if (canLow(m,(1ll<<n),p)) r = m;
            else l = m+1;
        }
        LL gar = l - 1;
        l = 0, r = (1ll << n);
        while (l < r) {
            LL m = l + (r-l)/2;
            if (!canHigh(m,(1ll<<n),p)) r = m;
            else l = m+1;
        }
        LL can = l - 1;
        printf("Case #%d: %lld %lld\n",it+1,gar,can);
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

