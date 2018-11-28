#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<ctime>
#include<cstdlib>
#include<iomanip>
#include<utility>
#define pb push_back
#define mp make_pair
#define CLR(x) memset(x,0,sizeof(x))
#define _CLR(x) memset(x,-1,sizeof(x))
#define REP(i,n) for(int i=0;i<n;i++)
#define Debug(x) cout<<#x<<"="<<x<<" "<<endl
#define REP(i,l,r) for(int i=l;i<=r;i++)
#define rep(i,l,r) for(int i=l;i<r;i++)
#define RREP(i,l,r) for(int i=l;i>=r;i--)
#define rrep(i,l,r) for(int i=l;i>r;i--)
#define read(x) scanf("%d",&x)
#define put(x) printf("%d\n",x)
#define ll long long
#define lson l,m,rt<<1
#define rson m+1,r,rt<<11
using namespace std;

char a[1010];
int sum[1010];

int main()
{
   int t;
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   while(~scanf("%d",&t))
   {
       REP(k,1,t)
       {
           int n;
           scanf("%d %s",&n,a);
           sum[0]=a[0]-'0';
           int ans=0;
           REP(i,1,n)
           {
               if(sum[i-1]<i)
               {
                   ans+=(i-sum[i-1]);
                   sum[i-1]+=(i-sum[i-1]);
               }
               sum[i]=sum[i-1]+a[i]-'0';
           }
           printf("Case #%d: %d\n",k,ans);
       }
   }
}
