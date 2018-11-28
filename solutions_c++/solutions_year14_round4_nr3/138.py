//powered by xpd1  /i love shimokawa_mikuni and i haven't touch my devc for 3 months.
//All of these left only broken history after 12.4.22.sacrifice for my  love.
//on 2012-10-
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<ctime>
#include<cstring>
#include<ctype.h>
#include<memory>
#include<fstream>
#include<string>
#include<utility>
#include<iomanip>
#define oo 2000000000
#define ol 200000000000000000ll
#define md 1000000007
#include<map>
#include<queue>
#include<vector>
#include<list>
#include<set>
//#include<conio.h>
#define oo 2000000000
#define ol 200000000000000000ll//=2E17
#define ooo 1E14
#define EPS 1E-10
#define mp make_pair
#define pb push_back
#define eps EPS
#define mem(x,y)(memset((x),y,sizeof((x))))
#define debug(x)cout<<#x<<"="<<x<<endl;
#ifdef __int64
#define fmt64 "%I64d"
#else
#define fmt64 "%lld"
#endif
#define fi first
#define se second
using namespace std;
using namespace rel_ops;
const double PI=acos((double)-1);
typedef long long LL;
typedef pair<int,int>pii;
typedef pair<LL,LL>pll;
int ts,ts2,ts3,ts4;
int n,m,B,H;
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
class sq
{public:
  int x1,y1,x2,y2;
}a[1005];
int d[1005][1005],h[1005];
int dis[1005];
int getdis(sq a,sq b)
{
	 int t1,t2,t3;
	 if (min(a.x2,b.x2)>=max(a.x1,b.x1))
	  return max(a.y1,b.y1)-min(a.y2,b.y2)-1;
	 if (min(a.y2,b.y2)>=max(a.y1,b.y1))
	  return max(a.x1,b.x1)-min(a.x2,b.x2)-1;
	 return max(max(a.x1,b.x1)-min(a.x2,b.x2),max(a.y1,b.y1)-min(a.y2,b.y2))-1;
}
int main()
{
  int i,j,k,l,t1,t2,t3,t4,t5,t6,t7,t8,t9,t,nw;
  int tt1,tt2,tt3,tt4;
  double u1,u2,u3,u4,u5,u6,u7,u8,u9;
  char c1,c2,c3;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  int T,T2;
		cin>>T2;
		for(T=1;T<=T2;T++)
		{
			printf("Case #%d: ",T);
			cin>>B>>H>>n;
	  for(i=1;i<=n;i++)
			 scanf("%d%d%d%d",&a[i].x1,&a[i].y1,&a[i].x2,&a[i].y2);
			int src=n+1,tar=n+2;
			n++;
			a[n]=(sq){-1,0,-1,H-1};
			n++;
			a[n]=(sq){B,0,B,H-1};
			for(i=1;i<=n;i++) 
			 for(j=i+1;j<=n;j++)
			  d[i][j]=d[j][i]=getdis(a[i],a[j]);
			mem(h,0);
			for(i=1;i<=n;i++)
			 dis[i]=oo,h[i]=0;
			dis[src]=0;
			for(i=1;i<=n;i++)
			{
				t1=oo,t2;
				for(j=1;j<=n;j++)
				{
					if (!h[j]&&dis[j]<t1){t1=dis[j];t2=j;}
				}
				h[t2]=1;
				for(j=1;j<=n;j++)
				 if (j!=t2)
				 {
				 	dis[j]=min(dis[j],dis[t2]+d[t2][j]);
				 }
			}
			printf("%d\n",dis[tar]);
		}
  return 0;
}


