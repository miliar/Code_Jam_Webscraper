/// BIS-MILLAHIR RAHMANIR RAHIM

#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>

using namespace std;

#define I1(n) scanf("%d",&n)
#define LL1(n) scanf("%lld",&n)
#define I2(n1,n2) scanf("%d%d",&n1,&n2)
#define LL2(n1,n2) scanf("%lld%lld",&n1,&n2)
#define I3(n1,n2,n3) scanf("%d%d%d",&n1,&n2,&n3)
#define LL3(n1,n2,n3) scanf("%lld%lld%lld",&n1,&n2,&n3)

#define F(i, a, b) for(  i = (a); i <= (b); i++ )
#define FR(i, a, b) for(  i = (a); i < (b); i++ )
#define FRR(i, a, b) for(  i = (a); i >b; i-- )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Pr(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) cout << *it << " "; cout << endl;

#define all(a) a.begin(),a.end()
#define pb push_back
#define pi acos(-1.0)
#define MEM(a,val) memset(a,val,sizeof(a))
#define eps 1e-9
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define sz(a) ((int)(a).size())
#define IN  freopen("input.txt","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define CLR(n) n.clear()
#define SQR(n) (n*n)
#define LEFT (idx<<1)
#define RIGHT (LEFT+1)
#define PC printf("Case %d:",cas++);
#define NL printf("\n");

template<typename T> T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}

int Set(int N,int pos){return N=N | (1<<pos);}
int reset(int N,int pos){return N= N & ~(1<<pos);}
bool check(int N,int pos){return (bool)(N & (1<<pos));}

//// sieve (prime generate)
/*
#define Prime_M 10000003
bool is_prime[Prime_M];
vector<int>prime;
void prime_generate()
{
    int i,j;
    for(i=3;i<=3163;i+=2) if(!is_prime[i])for(j=i+i+i;j<Prime_M;j+=(i+i)) is_prime[j]=true;
    prime.pb(2); for(i=3;i<Prime_M;i+=2) if(!is_prime[i]) prime.pb(i);
}
*/

int ar[113];
int nn;
int dp[10000+1][101];
bool vis[10000+1][101];

int call(int mote,int n)
{
    if(n==nn) return 0;

    if(vis[mote][n]) return dp[mote][n];
    vis[mote][n] = true;

    //cout << mote << " shaheen " << n << endl;

    if(ar[n]<mote) return dp[mote][n] = call(mote+ar[n],n+1);

    int mn = INT_MAX;
    if(mote>1) mn = call(mote+mote-1,n)+1;

    return dp[mote][n] = Min(mn,call(mote,n+1)+1);

    //return mn;

//    return Min( call(mote+mote-1,n)+1 , call(mote,n+1)+1 );
}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

    int tc,cas=1;
    int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,cnt=0;

    I1(tc);

    while(tc--)
    {
        MEM(vis,false);

        I1(a);
        I1(nn);

        FR(i,0,nn) I1(ar[i]);
        sort(ar,ar+nn);

       // FR(i,0,nn) cout << ar[i] << "<<--" <<endl;

        printf("Case #%d: %d\n",cas++,call(a,0));
    }

    return 0;
}
