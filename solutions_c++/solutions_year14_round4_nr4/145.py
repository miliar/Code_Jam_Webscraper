// powered by xpd1  /i love shimokawa_mikuni and i haven't touch my devc for 3 months. 
// All of these left only broken history after 12.4.22. sacrifice for my  love.
// on 2012-10-
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <memory>
#include <fstream>
#include <string>
#include <utility>
#include <iomanip>
#define oo 2000000000
#define ol 200000000000000000ll
#define md 1000000007 
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <set>
//#include <conio.h>
#define oo 2000000000
#define ol 200000000000000000ll //=2E17
#define ooo 1E14
#define EPS 1E-10
#define mp make_pair
#define pb push_back
#define eps EPS
#define mem(x,y) (memset((x),y,sizeof((x))))
#define debug(x) cout << #x<<" = "<<x<<endl;
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
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
int ts,ts2,ts3,ts4;
int n,m;
char s[1005][10];	
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
int lis[105][1005];
int mina,minb;
int a[1005],b[1005][26],a2;
void work()
{
	 int i,j,k,t1,t2,ans=0;
	 for(i=1;i<=n;i++) if (lis[i][0]==0)break;
	 if (i<=n)return;
	 for(i=1;i<=m;i++)
	 {
	 	a2=1;for(j=0;j<26;j++)b[i][j]=0;
	 	for(j=1;j<=lis[i][0];j++)
	 	{
	 		t1=lis[i][j];
	 		int nw=1;
				for(k=0;k<strlen(s[t1]);k++)
	 		{
	 			if(b[nw][s[t1][k]-65]==0)
	 			{
	 				a2++;b[nw][s[t1][k]-65]=a2;
	 				for(int l=0;l<26;l++)
	 				{
	 					b[a2][l]=0;
	 				}
	 				nw=b[nw][s[t1][k]-65];
	 				
	 			}
	 			
	 		}
	 		ans+=a2;
	 	}
	 }
	 if (ans>mina)
	 {mina=ans;minb=0;}
	 if (ans==mina){minb++;}
	 
}
void dfs(int dep)
{
	 int i;
	 if (dep>m)
   {work();return;}
 	 for(i=1;i<=n;i++)
	 {
	 	lis[i][++lis[i][0]]=dep;
		 dfs(dep+1);
			lis[i][0]--;
	 }
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
  int T,T2,X;
		cin >>T2;
		for(T=1;T<=T2;T++)
		{
			printf("Case #%d: ",T);
			mina=0;minb=0;
			cin>>m>>n;
			for(i=1;i<=m;i++)
			 scanf("%s",s[i]);
			dfs(1);
			
			printf("%d %d\n",mina,minb);
	 }
  return 0;
}
