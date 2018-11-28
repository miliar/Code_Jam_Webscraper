#include<cstdio>
#include<iostream>
using namespace std;
int a,b,k;
int calc(int a,int b,int k)
{
	int ans=0;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
		{
		//	if(i!=j)
		//	{
				if((i&j)<k)ans++;
			//}
			//if((i==j) && (i&i)<=k)ans++;
		}
	return ans;
}
int main()
{
  //  freopen("B-small-attempt0.in","r",stdin);
   // freopen("b.out","w",stdout);
    int T,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&a,&b,&k);
		int ans=calc(a,b,k);
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}
