#include<cstdio>
#include<set>
#include<map>
#include<iostream>
#include<queue>
#include<stack>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<ctime>
#define read freopen("in.txt","r",stdin)
#define maxlongint 2147483647
typedef  long long LL;
typedef  unsigned long long ULL;
#define fori for(i=1;i<=n;i++)
#define forj for(j=1;j<=m;j++)
#define FOR(i,n) for(i=1;i<=n;i++)
#define REP(i,a,b) for(i=a;i<=b;i++)
#define DREP(i,a,b) for(i=a;i>=b;i--)
#define DOWN(i,n) for(i=n;i>=1;i--)
#define enter cout<<endl;
#define in push_back
#define out pop_back
#define ll long long
#define lson 2*k
#define rson 2*k+1
#define left l,mid,lson
#define offcin ios::sync_with_stdio(false)
#define right mid+1,r,rson
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sd(x,y) scanf("%d%d",&x,&y)
#define sch(s) scanf("%s",s)
#define fillfalse(v) memset(v,false,sizeof(v))
#define filltrue(v) memset(v,true,sizeof(v))
#define Fill0(a)    memset(a,0,sizeof(a))
#define Fillplus(a)    memset(a,-1,sizeof(a))
#define lowbit(x) x&(-x)
using namespace std;
string ss;
int n,k,i,j,l,x,y,ans;
char c;
int main()
{
freopen("B-large.in","r",stdin);
freopen("out.txt","w",stdout);
  int ii,TT;
  cin>>TT;
  FOR(ii,TT)
  {
   cin>>ss;
   n=ss.size();
   ans=1; c=ss[0];
   REP(i,1,n-1) if (c!=ss[i]) {c=ss[i]; ans++;}
   if (ss[n-1]=='+') ans--;
    printf("Case #%d: %lld\n",ii,ans);
  }
}
