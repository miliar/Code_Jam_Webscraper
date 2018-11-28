#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<cstring>
#include<algorithm>
#include <climits>
#include <cmath>
#include<cstdlib>
#include<cstdio>
#include <cctype>
#include<iostream>
#include<sstream>
#include<ctime>
#include <functional>
#include <numeric>
using namespace std;


#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define DEBUG if(0)
#define SZ(c) c.size()
#define ALL(x) x.begin(),x.end()
#define ff first
#define ss second
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define PSI pair<string, int>
#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI >
#define VPI vector< PII >
#define LL long long
#define ULL unsigned long long
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define REPR(i,n) for(int i=(int)n-1; i>=0; --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)


template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template< class T > T GCD(const T a, const T b) { return (b ? GCD<T>(b, a%b) : a); }
template< class T > T LCM(const T a, const T b) { return (a / GCD<T>(a, b) * b); }
template< class T > T mod(const T &a, const T &b) { return (a < b ? a : a % b); }
template< class T > bool inrange(const T &a, const T &b, const T &c) { return a<=b && b<=c; }

const int INF=1000000007;
const int MOD=1000000007;
const LL LINF = 1ll << 60;

int arr[1005];

int main()
{
   READ("in.txt");
   WRITE("out.txt");

   int tc, smax;
   string str;

   cin>>tc;
   for(int cs=1; cs<=tc; cs++)
   {
       cin>>smax>>str;
       for(int i=0; i<=smax; i++)
       {
           arr[i]=str[i]-'0';
       }
       int sum=0, res=0;
       if(arr[0]==0) sum=1, res=1;
       else sum=arr[0];

       for(int i=1; i<=smax; i++) if(arr[i]>0)
       {
           if(sum<i) res+=(i-sum), sum+=(i-sum);
           sum+=arr[i];
       }

       cout<<"Case #"<<cs<<": "<<res<<endl;
   }

    return 0;
}




