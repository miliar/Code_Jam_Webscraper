#pragma comment(linker, "/stack:640000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
const double PI=acos(-1.0);

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)
#define    MP(x, y) 	     make_pair(x, y)
#define    PB(x)             push_back(x)
#define    rep(i,n)          for(int i = 1 ; i<=(n) ; i++)
#define    repI(i,n)         for(int i = 0 ; i<(n) ; i++)
#define    FOR(i,L,R) 	     for (int i = L; i <= R; i++)
#define    ROF(i,L,R) 	     for (int i = L; i >= R; i--)
#define    FOREACH(i,t)      for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define    ALL(p) 	         p.begin(),p.end()
#define    ALLR(p) 	         p.rbegin(),p.rend()
#define    SET(p) 	         memset(p, -1, sizeof(p))
#define    CLR(p)            memset(p, 0, sizeof(p))
#define    MEM(p, v)         memset(p, v, sizeof(p))
#define    getI(a) 	         scanf("%d", &a)
#define    getII(a,b) 	     scanf("%d%d", &a, &b)
#define    getIII(a,b,c)     scanf("%d%d%d", &a, &b, &c)
#define    getL(a)           scanf("%lld",&a)
#define    getLL(a,b)        scanf("%lld%lld",&a,&b)
#define    getLLL(a,b,c)     scanf("%lld%lld%lld",&a,&b,&c)
#define    getC(n)           scanf("%c",&n)
#define    getF(n)           scanf("%lf",&n)
#define    getS(n)           scanf("%s",n)
#define    bitCheck(N,in)    ((bool)(N&(1<<(in))))
#define    bitOff(N,in)      (N&(~(1<<(in))))
#define    bitOn(N,in)       (N|(1<<(in)))
#define    iseq(a,b)          (fabs(a-b)<EPS)
#define    vi 	 vector < int >
#define    vii 	 vector < vector < int > >
#define    pii 	 pair< int, int >
#define    ff 	 first
#define    ss 	 second
#define    ll	 long long
#define    ull 	 unsigned long long

template< class T > inline T _abs(T n)
{
    return ((n) < 0 ? -(n) : (n));
}
template< class T > inline T _max(T a, T b)
{
    return (!((a)<(b))?(a):(b));
}
template< class T > inline T _min(T a, T b)
{
    return (((a)<(b))?(a):(b));
}
template< class T > inline T _swap(T &a, T &b)
{
    a=a^b;
    b=a^b;
    a=a^b;
}
template< class T > inline T gcd(T a, T b)
{
    return (b) == 0 ? (a) : gcd((b), ((a) % (b)));
}
template< class T > inline T lcm(T a, T b)
{
    return ((a) / gcd((a), (b)) * (b));
}
template <typename T> string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}

#ifdef dipta007
#define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
#define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;

int main()
{
#ifdef dipta007
    READ("ina.txt");
    //WRITE("out.txt");
#endif // dipta007

    int t;
    getI(t);
    FOR(ci,1,t)
    {
        int n;
        getI(n);
        int sum=0;
        vector <pii> vp;
        FOR(i,0,n-1)
        {
            int x;
            getI(x);
            sum += x;
            vp.PB(pii(x,i));
        }
        sort(ALLR(vp));
        printf("Case #%d:",ci);
        while(1)
        {
            //debug(vp[0].ff,vp[0].ss);
            if(vp[0].ff==1)
            {
                int cnt=0;
                FOR(j,0,n-1)
                {
                    if(vp[j].ff) cnt++;
                }
                if(cnt%2==1)
                {
                    printf(" %c",vp[0].ss+'A');
                    vp[0].ff--;
                }
                else
                {
                    printf(" %c%c",vp[0].ss+'A',vp[1].ss+'A');
                    vp[0].ff--;
                    vp[1].ff--;
                }
                sort(ALLR(vp));
                continue;
            }
            if(vp[0].ff==0) break;

            vp[0].ff--;
            char c2;
            char c1 = vp[0].ss + 'A';

            sum--;

            sort(ALLR(vp));
            if(vp[0].ff==0)
            {
                printf(" %c",c1);
                break;
            }
            int k = ceil((double)(sum)/2.0);
            if(vp[0].ff>=k)
            {
                vp[0].ff--;
                sum--;

                c2 = vp[0].ss + 'A';
            }
            else
            {
                printf(" %c",c1);
                continue;
            }
            printf(" %c%c",c1,c2);

            sort(ALLR(vp));
        }
        printf("\n");

    }

    return 0;
}




