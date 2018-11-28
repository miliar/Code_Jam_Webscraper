#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int d[1010],n;

int deal(int fen)
{	
	int sum=0,ans=0;
	for(int i=1;i<=n;i++)
	{
		if(d[i]>fen)
		{
//			d[i]+=sum;
			sum=d[i]%fen;
			ans+=d[i]/fen-1+(sum!=0);
		}
	}
// 	if(sum)ans++;
//	printf("%d %d %d\n",fen,sum,ans);
	return ans;
}
bool cmp(int a,int b)
{return a>b;}

int main()
{
//	freopen("b.in","r",stdin);
//	freopen("b.out","w",stdout);
	int T ;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		scanf("%d",&n);
		int sum=0;
		memset(d,0,sizeof(d));
		int tt=0,ans=0;
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&d[i]);
			sum+=d[i];
			ans=max(ans,d[i]);
		}
		std::sort(1+d,1+d+n,cmp);
	//	printf("%d\n",ans);
	int t=ans; 
		for(int i=1;i<=t;i++)
		{
			tt=0;
			ans=min(ans,i+deal(i));
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
	return 0;
}

