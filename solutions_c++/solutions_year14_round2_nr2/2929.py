#include "stdio.h"
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
int main()
{
	read;
	write;
	int t;
	int i,j,n;
	int a,b,k,m;
	scanf("%d",&t);
	for (i = 1; i < t+1; ++i)
	{
		scanf("%d%d%d",&a,&b,&k);
		m=0;
		for(j=0;j<a;++j)
		{
			for(n=0;n<b;++n)
			{
				//printf("%d %d %d\n",n,j,n&j );
				if((n&j)<k)
				{
					//printf("yes\n" );
					m++;
				}
					
			}
		}
		printf("Case #%d: %d\n",i,m);
	}
	return 0;
}