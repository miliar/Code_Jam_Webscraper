#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
 
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define PB                      push_back
#define SS                      ({int x;scanf("%d", &x);x;})
#define SSL                     ({LL x;scanf("%lld", &x);x;})
#define SSD                     ({double x;scanf("%lf",&x);x;})
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define swap(a,b)                int temp; temp=a;a=b;b=temp;
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define CASE(T)                 int T;scanf("%d ",&T);while(T--)
#define mp						make_pair
#define ff						first
#define ss       				second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof a)
#define pb				        push_back  
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define SORT(v)			        sort((v).begin(),(v).end())
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
int check_pal(long long int n)
{
char a[20];
int i=0,j;
while(n>0)
{
    a[i++]=n%10;
    n/=10;
}
for(j=0;j<i/2;j++)
{
    if(a[j]!=a[i-j-1])
    return 0;
}
return 1;
}
 main()
 {
        long long int i,j=0,n,k=1,p=0;
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
  long long int b[100];
    for(n=1;n<=10000000;n++)
            {
            if(check_pal(n))
           if(check_pal(n*n))
            b[p++]=n*n;
        }
        
       CASE(T){
            int ans=0;
            scanf("%lld%lld",&i,&j);
           for(n=0;n<p;n++)
           if(b[n]>=i&&b[n]<=j)
            ans++;
            printf("Case #%lld: %d\n",k++,ans);
}
            return 0;
}
            
            
            
            
            
            
            
            
            
            
