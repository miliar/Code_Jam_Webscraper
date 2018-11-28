#include <algorithm>
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
#define PI 3.1415926535897932384626

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)
//
//#define    vi 	 vector < int >
//#define    vii 	 vector < vector < int > >

//typedef pair <int,int>pii;

#define CLR(n, v) memset(n, v, sizeof( n ))

#define ff first
#define ss second

#define ll long long int
#define ull unsigned long long int

//******************DELETE****************
#define howcum
#ifdef howcum
     #define debug(args...) {dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;
//******************DELETE****************

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > T gcd(T a, T b) { return (b == 0 ? a : gcd(b, a % b)); }
template< class T > T lcm(T a, T b) { return (a / gcd(a, b) * b); }


int Set(int N,int pos){return N=N | (1<<pos);}
int reset(int N,int pos){return N= N & ~(1<<pos);}
bool check(int N,int pos){return (bool)(N & (1<<pos));}

typedef pair<int,int>ii;
typedef vector<ii>vii;
typedef vector<int>vi;
typedef vector<ll>vl;
typedef pair<ll,ll>lii;
typedef vector<lii>vlii;


int freq[11];
bool call_freq()
{
    int flag=1;
    for(int i=0;i<10;i++)
    {
        if(freq[i]==0)
        {
            flag=0;
            break;
        }
    }
    return flag;
}

int main()
{
//        READ("inA.txt");
//    WRITE("outA.txt");
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        ll n;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",tc);
            continue;
        }
        CLR(freq,0);
        ll i=1;
        while(1)
        {
            ll t=n*i;
            while(t!=0)
            {
                freq[t%10]++;
                t/=10;
            }
            if(call_freq())
            {
                break;
            }
            i++;
        }
        printf("Case #%d: %lld\n",tc,(n*i));
    }
    return 0;
}


//10
//8 1 9 8 3 4 6 1 5 2


