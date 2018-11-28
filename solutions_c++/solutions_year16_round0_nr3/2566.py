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
#define    bitCheck(a,k)     ((bool)(a&(1<<(k))))
#define    bitOff(a,k)       (a&(~(1<<(k))))
#define    bitOn(a,k)         (a|(1<<(k)))
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

#ifdef mamun
#define debug(args...) {cerr<<"*: "; dbg,args; cerr<<endl;}
#else
#define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger
{
    template<typename T> debugger& operator, (const T& v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;
///****************** template ends here ****************
int t,n,m;
#define mx 100000000
vector<int> primes;
bool Check(ll N,ll pos)
{
    return (bool)(N & (1<<pos));
}
int Set(ll N,ll pos)
{
    return N=N | (1<<pos);
}
int status[(mx/32)+2];
void sieve()
{
    int i, j;
    primes.push_back(2);
    for( i = 3; i*i <=mx; i += 2 )
    {
        if( Check(status[i>>5],i%31)==0){
                primes.push_back(i);
            for( j = i*i; j <= mx; j += (i<<1) )
                status[j>>5]=Set(status[j>>5],j & 31)   ;
        }
    }
    while(i<mx)
    {
        if( Check(status[i>>5],i%31)==0)primes.push_back(i);
        i+=2;
    }
}
int sz;
int finddivisor(ll num)
{
    for(int i=0; i<sz&&(ll)primes[i]*(ll)primes[i]<=num; i++)
    {
        if(num%primes[i]==0)
        {
            return primes[i];
        }
    }
    return -1;
}
vector<pair<string,vector<ll> > > ans;
int cnt;
void call(int pos,string num,vector<ll> v)
{
    if(cnt==m)return;
    if(pos==n)
    {
        vector<ll> tmp;
        repI(i,9)
        {
            ll val=finddivisor(v[i]);
            if(val==-1)return;
            tmp.push_back(val);
        }
        ans.push_back(make_pair(num,tmp));
        cnt++;
        return;
    }
    if(pos==0||pos==n-1)
    {
        num+="1";
        repI(i,9)
        {
            v[i]=v[i]*(i+2)+1;
        }
        call(pos+1,num,v);
        if(cnt==m)return;
    }
    else
    {
        vector<ll> tmp=v;
        repI(i,9)
        {
            v[i]=v[i]*(i+2)+0;
        }
        call(pos+1,num+"0",v);
        if(cnt==m)return;
        repI(i,9)
        {
            tmp[i]=tmp[i]*(i+2)+1;
        }
        call(pos+1,num+"1",tmp);
        if(cnt==m)return;
    }
}

int main()
{
    ///check for 0 or -1 if input not specified
#ifdef mamun
    READ("C-small-attempt0.in");
    WRITE("C-small-attempt0.out");
#endif // mamun
    sieve();
    getI(t);
    sz=primes.size();
    rep(cs,t)
    {
        cnt=0;
        ans.clear();

        getII(n,m);
        vector<ll> v;
        repI(i,9)v.push_back(0);
        call(0,"",v);

        debug(ans.size())

        printf("Case #%d:\n",cs);
        repI(i,ans.size())
        {
            cout<<ans[i].ff;
            v=ans[i].ss;
            repI(j,v.size())printf(" %lld",v[j]);
            puts("");
        }


    }


    return 0;
}

