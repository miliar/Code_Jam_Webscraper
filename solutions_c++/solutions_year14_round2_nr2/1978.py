#include<cstdio>
#include<cstdlib>
int main()
{
	int ans,T;
	scanf("%d",&T);
	for (int ri=0;ri<T;ri++)
	{
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);
		ans=0;
		for (int i=0;i<a;i++)
		for (int j=0;j<b;j++)
		if ((i&j)<k)
		ans++;
		printf("Case #%d: %d\n",ri+1,ans);
	}
}
