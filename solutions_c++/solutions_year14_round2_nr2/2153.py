#include <stdio.h>

int main()
{
	int T,a,b,k,i,j,l;
	int ans = 0;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(i=1; i<=T; i++)
	{
		ans = 0;
		scanf("%d%d%d",&a,&b,&k);
		for(j=0; j<a; j++)
		{
			for(l=0;l<b; l++)
			{
				if((j&l) < k )
					ans++;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}

}