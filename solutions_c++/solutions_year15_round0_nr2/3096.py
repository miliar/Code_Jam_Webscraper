#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	int t,n,k,MAX,ans;
	int a[2000];
	scanf("%d",&t);
	for (int TT=1;TT<=t;TT++)
	{
		MAX=0;
		ans=9999;
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&k);
			a[k]++;
			if (k>MAX) MAX=k;
		}
		int cnt=0;
		for (int i=MAX;i>0;i--)
		{
			cnt=i;
			for(int j=i+1;j<=MAX;j++) cnt=cnt+a[j]*((j+i-1)/i-1);
			if (cnt<ans) ans=cnt;
		}
		printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}