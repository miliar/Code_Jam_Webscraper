/********************************
*MAHBUBCSEJU                    *
*CSE 22                         *
*JAHANGIRNAGAR UNIVERSITY       *
*TIMUS:164273FU                 *
*UVA>>LIGHTOJ>>HUST:mahbubcseju *
********************************/
#include<cfloat>
#include<climits>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<map>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<string.h>
#define ll long long int
#define ull unsigned long long int
#define I(a) scanf("%d",&a)
#define I2(a,b) scanf("%d%d",&a,&b)
#define I3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define L(a) scanf("%lld",&a)
#define L2(a,b) scanf("%lld%lld",&a,&b)
#define L3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define PI(a) printf("%d\n",a)
#define PL(a) printf("%lld\n",a)
#define PT(t) printf("Case %d: ",t)
#define IT(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define ITP(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) {  cout << *it << " "; } cout << endl;
#define PB push_back
#define xx first
#define yy second
#define SC scanf
#define PC printf
#define NL printf("\n")
#define SET(a) memset(a,0,sizeof a)
#define SETR(a) memset(a,-1,sizeof a)
#define SZ(a) ((int)a.size())
//#define pi 2.0*acos(0.0)
#define R(a) freopen(a, "r", stdin);
#define W(a) freopen(a, "w", stdout);
#define CB(x) __builtin_popcount(x)
#define STN(a) stringtonumber<ll>(a)
#define lol printf("BUG\n")
#define mk make_pair
using namespace std;
template <class T> inline T BM(T p, T e, T M)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a, T b)
{
    if(b == 0)return a;
    return gcd(b, a % b);
}
template <class T> inline T MDINV(T a, T M)
{
    return BM(a, M - 2, M);
}
template <class T> inline T PW(T p, T e)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p);
        p = (p * p);
    }
    return (T)ret;
}
template <class T>string NTS ( T Number )
{
    stringstream ss;
    ss << Number;
    return ss.str();
}
template <class T>T stringtonumber ( const string &Text )
{
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
template <class T>bool ISLEFT ( T a,T b,T c)
{
    if(((a.xx-b.xx)*(b.yy-c.yy)-(b.xx-c.xx)*(a.yy-b.yy))<0.0)return 1;//Uporer dike //A,b,c, x okkher ordera sorted
    else return 0;
}
#define mx 5000000
#define md 10000000000007ll

#define maxp 100000000000000004
typedef pair<int , int >P;
typedef vector<int >V;

////////define value/////
ll res1(ll num,ll ba)
{
    ll ans=1;
    ll res=0;
    for(ll i=0; i<16; i++)
    {
        if((num&(1<<i)))
        {
            res=ans+res;
        }
        ans*=ba;
    }
    for(ll j=2; j*j<=ans; j++)
    {
        if(res%j==0)return j;

    }
    return 0;

}
int main()
{
   R("in.txt");
    W("Out.txt");
    int tc,cs=0;
    I(tc);
    while(tc--)
    {
        int n,m;
        I2(n,m);
        vector<ll>v[100];
        int sz=0;
        ll ar[13];
        int xo=0;
        for(int i=1; i<(1<<n); i++)
        {

            if(i>(1<<(n-1))&&i%2)
            {
                bool fl=0;
                ++sz;
                int s=0;
                for(ll j=2; j<=10; j++)
                {
                    ll x=res1(i,j);
                    if(x==0)
                    {
                        fl=1,sz--;
                        break;
                    }
                    else
                    {
                       ar[++s]=x;
                    }
                }
                if(!fl)
                {
                   ++xo;
                    v[xo].PB(i);
                    for(int l=1;l<=9;l++)v[xo].PB(ar[l]);

                    if(xo==m)break;
                }
            }
        }
      //  cout<<xo<<endl;
        PC("Case #%d:\n",++cs);
        for(int i=1;i<=m;i++)
        {
            string s;
            for(int j=0;j<n;j++)
            {
                if((v[i][0]&(1<<j)))s+='1';
                else s+='0';
            }
            reverse(s.begin(),s.end());
            cout<<s<<" ";
            for(int j=1;j<9;j++)
            {
                PC("%lld ",v[i][j]);
            }
            PC("%lld\n",v[i][9]);
           // lol;
        }

    }
    return 0;
}
