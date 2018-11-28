#include <stdio.h>
#define mn(a,b) a<b ? a:b
#define mx(a,b) a>b ? a:b
#define INF 1000000000

using namespace std;

int main()
{
	int i,j,k,c,s,t,loop;
	freopen("../test.in","r",stdin);
	freopen("../test.out","w",stdout);
	scanf("%d",&t);
	for(loop = 1;loop<=t;loop++)
	{
		scanf("%d %d %d",&k,&c,&s);
		printf("Case #%d: ",loop);
		for(i=s;i>=1;i--)
		{
			printf("%d ",i);
		}
		printf("\n");
	}
	return 0;
}