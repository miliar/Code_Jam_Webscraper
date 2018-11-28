#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
#define rep1(i,n) for(i=1;i<=n;i++)
#define rev(i,n) for(i=n-1;i>=0;i--)
#define rev1(i,n) for(i=n;i>=1;i--)
#define REP(i,a,b) for(i=a;i<b;i++)
#define REP1(i,a,b) for(i=a;i<=b;i++)
#define FOR(it,v) for(auto it=v.begin();it!=v.end();it++)
#define pb push_back
#define pq priority_queue
#define mem(i,n) memset(i,n,sizeof(i))
#define eps 1e-7
#define debug printf("bug!!!\n")
#define sz size()
#define em empty()
#define cl clear()
#define fi first
#define se second
#define mp make_pair
#define Sort(v) sort( v.begin(),v.end() )

/*Knight direction*/
long kx[]={2,-2,2,-2,1,-1,1,-1};
long ky[]={1,1,-1,-1,2,2,-2,-2};
/*4 & 8 move direction*/
long dx[]={1,-1,0,0,1,-1,1,-1};
long dy[]={0,0,1,-1,1,1,-1,-1};
//#define check(a,b,row,column) ((a>=0 && a<row) && (b>=0 && b<column))

/*Bit Mask DP Macros*/
#define Set(n,pos) ( n | (1<<pos) )
#define reset(n,pos) (n & (~(1<<pos)))
#define check(n,pos) ((bool)(n&(1<<pos)))

/*input && output*/
#define sf3(x,y,z) scanf("%ld %ld %ld",&x,&y,&z)
#define sf2(x,y) scanf("%ld %ld",&x,&y)
#define sf1(x) scanf("%I64d",&x)
#define pf3(x,y,z) printf("%ld %ld %ld\n",x,y,z)
#define pf2(x,y) printf("%ld %ld\n",x,y)
#define pf1(x) printf("%ld\n",x)
#define NL puts("")
/*typedef*/
//typedef long L;
typedef long long L;
const L INF= (1e18);
inline L MOD(L a,L b)
{
    L res=a%b;
    return res<0 ? res+abs(b) : res;
}
inline L Pow(L base, L exp)
{
    L res = 1;
    while (exp>0)
    {
        if (exp & 1) res*= base;
        exp >>= 1;
        base *= base;
    }
    return res;
}
inline L Log(L base,L n)
{
    L ans=(L) ( floor( log10( (double)n ) / log10( (double)base ) )+eps );
    return ans;
}
inline L BigMod(L base, L exp,L M)
{
    base=MOD(base,M);
    L res = 1;
    while (exp>0)
    {
        if (exp & 1) res= MOD(res*base,M);
        exp >>= 1;
        base=MOD(base*base,M);
    }
    return res;
}
typedef pair<L,string> pll;
typedef vector <L> vl;
typedef map < string, L > msl;
typedef map < L,string > mls;
typedef map < char, L > mcl;
typedef map < L,char > mlc;
typedef map < L, L > mll;
typedef queue <L> Queue;
typedef vector <string> vs;
typedef vector <pll> vp;
#define mx 509

bool checker(const string &s)
{
    L i,k=s.sz;

    rep(i,k)
    {
        if(s[i]=='-')
        {
            return false;
        }
    }
    return true;
}

bool checker1(const string &s)
{
    L i,k=s.sz;

    rep(i,k)
    {
        if(s[i]=='+')
        {
            return false;
        }
    }
    return true;
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    L x,y,z,i,j,k,l,m,n,p,q,r,u,v,w,t,cas,edge,node,a,b,c,d,e,f,ans,cnt,ass;
    sf1(t);
    rep1(cas,t)
    {
        string s;
        cin>>s;
        k=s.sz;

        cnt=0;
        while(1)
        {
            if(checker(s)==true) break;
            if(checker1(s)==true)
            {
                cnt++;
                break;
            }
            a=b=0;

            rep(i,k)
            {
                if(s[i]=='+') a++;
                else b++;
                if( (a==1 && b>=1) || (b==1 && a>=1) )
                {
                    rep(j,i)
                    {
                        s[j]=(s[j]=='+'?'-':'+');
                    }
                    cnt++;
                    break;
                }

            }

        }

        printf("Case #%I64d: %I64d\n",cas,cnt);
    }

    return 0;
}







