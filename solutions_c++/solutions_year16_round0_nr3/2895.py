#pragma comment(linker, "/stack:640000000")
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

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;
//******************DELETE****************

template< class T > T _abs(T n)
{
    return (n < 0 ? -n : n);
}
template< class T > T _max(T a, T b)
{
    return (!(a < b) ? a : b);
}
template< class T > T _min(T a, T b)
{
    return (a < b ? a : b);
}
template< class T > T _swap(T &a, T &b)
{
    a=a^b;
    b=a^b;
    a=a^b;
}
template< class T > T gcd(T a, T b)
{
    return (b == 0 ? a : gcd(b, a % b));
}
template< class T > T lcm(T a, T b)
{
    return (a / gcd(a, b) * b);
}


int Set(int N,int pos)
{
    return N=N | (1<<pos);
}
int reset(int N,int pos)
{
    return N= N & ~(1<<pos);
}
bool check(int N,int pos)
{
    return (bool)(N & (1<<pos));
}

typedef pair<int,int>ii;
typedef vector<ii>vii;
typedef vector<int>vi;
typedef vector<ll>vl;
typedef pair<ll,ll>lii;
typedef vector<lii>vlii;

int n,j;
#define mx 100000002
bool marked[mx+3];
vi primes;

bool isPrime(ll n)
{
    if(n%2==0)
    {
        return 0;
    }
    if(n<mx)
    {
        return marked[n]==0;
    }
    else
    {
        int flg=1;
        for(int i=0;i<primes.size();i++)
        {
            if(n%(ll)primes[i]==0)
            {
                flg=0;
                break;
            }
        }
        return flg;
    }
}

void sieve()
{
    int sqrtn=sqrt(mx);
    for(int i=3; i<=sqrtn; i+=2)
    {
        if(marked[i]==0)
        {
            for(int j=i*i; j<=mx; j+=i+i)
            {
                marked[j]=1;
            }
        }
    }
    primes.push_back(2);
    for(int i=3; i<=mx; i+=2)
    {
        if(marked[i]==0)
        {
            primes.push_back(i);
        }
    }
}
int cnt;
void call(int pos,string temp)
{
    if(cnt==j)
    {
        //printf("")
        return;
    }
    if(pos==n-1)
    {
        //debug(temp);
        temp+='1';
        if(temp[0]== '0' || temp[pos-1]=='0')
        {
            return;
        }

        int fl=1;
        vi div;
        div.assign(11,0);
        for(int i=2; i<=10; i++)
        {
            ll now=0;
            int len=temp.size();
            for(int k=0; k<len; k++)
            {
                ll t=temp[k]-48;
                now*=(ll)i;
                now+=t;
            }
            //debug(temp);
            if(isPrime(now))
            {
                fl=0;
                break;
            }

        }
        if(fl==0)
            {
                return;
            }

        //debug(temp);
        cout<< temp << " ";
        for(int i=2; i<=10; i++)
        {
            ll now=0;
            int len=temp.size();
            for(int k=0; k<len; k++)
            {
                ll t=temp[k]-48;
                now*=(ll)i;
                now+=t;
            }
            //debug(i,now);
            for(ll k=2; k*k<=now; k++)
            {

                if(now%k==0)
                {
                    printf(" %lld",k);
                    break;
                }
            }

        }
        cnt++;
        printf("\n");
        return;
    }

    call(pos+1,temp+'1');
    call(pos+1,temp+'0');
}

int main()
{
    //READ("in.txt");
//    WRITE("outA.txt");
    sieve();
    int T;
    scanf("%d",&T);
    for(int tc=1; tc<=T; tc++)
    {
        scanf("%d %d",&n,&j);
        cnt=0;
        printf("Case #%d:\n",tc);
        call(1,"1");
    }
    return 0;
}


//10
//8 1 9 8 3 4 6 1 5 2


