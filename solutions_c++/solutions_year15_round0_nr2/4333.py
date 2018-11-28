#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	 int i,t,n,j,ans,mint,k,maxn;
	 int a[1005];
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
	 while(scanf("%d",&t)!=EOF)
	 {
	 	for(k=1;k<=t;k++)
	 	{
	 		scanf("%d",&n);
	 		maxn=0;
	 		for(i=1;i<=n;i++)
	 		{
	 			scanf("%d",&a[i]);
	 			maxn=max(maxn,ans);
	 		}
	 		mint=0x7fffffff;
	 		//ans=0;
	 		for(i=1;i<=maxn;i++)
	 		{
	 			ans=0;
	 			for(j=1;j<=n;j++)
	 			{
	 				ans=ans+(a[j]-1)/i;		
	 			}
	 			ans+=i;
	 			mint=min(mint,ans);
	 		}
	 		printf("Case #%d: %d\n",k,mint);
	 	}
	 }            
    fclose(stdin);
    fclose(stdout);
    return 0;
}
