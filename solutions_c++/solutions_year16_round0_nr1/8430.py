#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
#define ll long long
using namespace std;

#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);
#define aov(a) a.begin(),a.end()
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define scl2(a,b) scanf("%lld%lld",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scl3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define debug(x) cout<<"x"<<endl;
#define mod 1000000007
#define xx first
#define yy second
#define pb push_back
#define f(i,n) for(int i=0;i<n;i++)
#define bits(a) __builtin_popcount(a)
#define mem(x) memset(x,0,sizeof(x))
#define memn(x) memset(x,-1,sizeof(x))
#define inf (INT_MAX/10)


ll bigmod(ll p,ll e,ll M)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return ret;
}

ll extended(ll a,ll b,ll &x,ll &y)
{
    a=abs(a);
    b=abs(b);
    ll g,x1,y1;
    if(!b)
    {
        x=1;
        y=0;
        g=a;
        return g;
    }
    g=extended(b,a%b,x1,y1);
    x=y1;
    y=x1-(a/b)*y1;
    return g;
}
ll modinverse(ll a,ll M)
{
    return bigmod(a,M-2,M);    // M is prime
}
ll bpow(ll p,ll e)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p);
        p = (p * p);
    }
    return ret;
}

int toInt(string s)
{
    int sm;
    stringstream ss(s);
    ss>>sm;
    return sm;
}
int toLlint(string s)
{
    long long int sm;
    stringstream ss(s);
    ss>>sm;
    return sm;
}

string convertInt(ll number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0; i<temp.length(); i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

ll ncr[1001][1001];

void NCR()
{
    for(int i=1; i<=1000; i++)
    {
        ncr[i][i]=1;
        ncr[i][0]=1;
        for(int r=1; r<i; r++)
        {
            ncr[i][r]=(ncr[i-1][r]+ncr[i-1][r-1])%mod;
        }
    }
}

///int month[]= {-1,31,28,31,30,31,30,31,31,30,31,30,31}; //Not Leap Year
///int month1[]= {-1,31,29,31,30,31,30,31,31,30,31,30,31}; // Leap Year
///int dx[]= {1,0,-1,0};int dy[]= {0,1,0,-1}; //4 Direction
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int dx[]={-1,-1,+0,+1,+1,+0};int dy[]={-1,+1,+2,+1,-1,-2}; //Hexagonal Direction
///const double eps=1e-6;

int ar[10];

int main()
{
    READ("jamAAA.txt");
    WRITE("jamAL.txt");

    int test,cnt,cs=0;
    long long val,it,cur;
    string ss;
    sc(test);
    while(test--)
    {
        cs++;
        it=1;
        mem(ar);
        cnt=0;
        cin>>val;
        cur=val;
        if(val==0)
        {
            cout<<"Case #"<<cs<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        ss=convertInt(val);
        for(int i=0; i<ss.length(); i++)
        {
            if(ar[ss[i]-'0']==0) ar[ss[i]-'0']=1,cnt++;
        }

        while(cnt<10)
        {
            it++;
            val=cur*it;
            ss=convertInt(val);
            for(int i=0; i<ss.length(); i++)
            {
                if(ar[ss[i]-'0']==0) ar[ss[i]-'0']=1,cnt++;
            }
        }
        cout<<"Case #"<<cs<<": "<<val<<endl;

    }
}

