//OM
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <algorithm>
using  namespace  std;

#define  x first
#define  y second
#define  pb push_back
#define  mp make_pair
#define  PI (acos(-1.0))
#define  mem(a,b) memset(a,b,sizeof(a))
#define  Sort(x) sort(x.begin(),x.end())
#define  FOR(i, b, e) for(int i = b; i <= (int)(e); i++)
#define  FORR(i, b, e) for(int i = b; i >=(int)(e); i--)
#define  FORI(i, s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
#define  pr(x) cout<<x<<"\n"
#define  prs(x) cout<<x<<" "
#define  pr2(x,y) cout<<x<<" "<<y<<"\n"
#define  pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
#define  ppr(a) cout<<a.x<<" "<<a.y<<"\n"

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double , double> pdd;
typedef  vector <int> vi;
typedef  vector <pii> vpii;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction

#define  EPS 1e-9
#define  MAX 100007

// Miller Rabin Primarility Testing
ll  bigmod(ll a,ll b,ll mod) { //Bigmod
    ll ans=0;
    while(b){
        if (b&1)
            ans=(ans+a)%mod;
        a=(a+a)%mod;
        b>>=1;
    }
    return ans;
}
// Random Number Generator
ll  randomll () {
    ll  ans = 0;
    FOR(i,0,3)
        ans = (ans << 16) ^ rand();
    return ans;
}
// Binary Represt.
ll  binByMod(ll  a, ll  to, ll  mod) {
    ll ans=1;
    while(to){
        if(to&1)
            ans=bigmod(ans,a,mod);
        a=bigmod(a,a,mod);
        to>>=1;
    }
    return ans;
}
// Prime Testing
bool isPrime(ll  n) {
    if (n % 2 == 0 && n != 2||n==1)
        return false;
    FOR(i,0,20) {
        ll  a = (randomll () % (n - 1));
        if (a < 0) a += n - 1;
        a++;
        a = binByMod(a, (n - 1) / 2, n);
        if (a != n - 1 && a != 1)
            return false;
    }
    return true;
}



bool mark[100000007];
int prime[5761459];
int  prime_gen(int n)
{
    for(int i=3;i*i<=n;i+=2)
        if(!mark[i])
            for(int j=i*i,k=i<<1;j<=n;j+=k)
            mark[j]=true;
    int k=0;
    prime[k++]=2;
    for(int i=3;i<=n;i+=2)if(!mark[i])prime[k++]=i;
    return k;
}

ll base[20];
ll now[20];
bool isjam(int n)
{
   // pr(n);
    mem(base,0LL);
    FOR(i,2,10)now[i]=1;
    FOR(j,0,15)
    {
        if(n&(1<<j))
        {
            FOR(i,2,10)base[i]+=now[i];
        }
        FOR(i,2,10)now[i]*=i;
    }
    FOR(i,2,10)if(isPrime(base[i]))return false;
    return true;
}
string toBinary(int n)
{
    std::string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return r;
}
ll prove(ll n,int pn)
{
    FOR(i,0,pn-1)
    {
        if(n%prime[i]==0)return prime[i];
    }
    return -1;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("outs.txt", "w", stdout);
    int T,n,jn;
    scanf("%d",&T);
    int pn=prime_gen(100000001);
    FOR(cs,1,T)
    {
        scanf("%d%d",&n,&jn);
        int s=(1<<15)+1,e=(1<<16)-1;
        int cnt=0;
        printf("Case #1:\n");
        for(int i=s;i<=e;i+=2)
        {
            if(isjam(i))
            {
                printf("%s",toBinary(i).c_str());
                FOR(i,2,10)
                {
                    printf(" %lld",prove(base[i],pn));
                }printf("\n");
                cnt++;
            }

            if(cnt==jn){
                    break;
            }
        }
    }
    return 0;
}

