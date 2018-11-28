#include <stdio.h>
#include <string.h>
#define mn(a,b) a<b ? a:b
#define mx(a,b) a>b ? a:b
#define INF 1000000000

using namespace std;

int mark[11];

int main()
{
	int i,j,loop,t,n,cnt;
	// freopen("../test.in","r",stdin);
	// freopen("../test.out","w",stdout);
	scanf("%d",&t);
	for(loop = 1;loop <= t;loop++)
	{
		cnt = 0;
		printf("Case #%d: ",loop);
		scanf("%d",&n);
		if(n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		cnt = 0;
		memset(mark,0,sizeof(mark));
		for(i=n;;i+=n)
		{
			j = i;
			while(j!=0)
			{
				if(mark[j%10] == 0)
				{
					mark[j%10] = 1;
					// printf("%d\n",j%10);
					cnt++;
				}
				j/=10;
			}
			if(cnt == 10)
				break;
		}
		printf("%d\n",i);
	}
	return 0;
}