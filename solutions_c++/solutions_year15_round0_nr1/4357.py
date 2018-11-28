#include "stdio.h"

#if 1

#define F	"A-large"

#define P	printf

#define N	1000

char s[N+1];

int main(void)
{
	freopen("IO/"F".in","r",stdin);
	freopen("IO/"F".out.txt","w",stdout);

	int t,tst;
	scanf("%d", &tst);
	for(t=1 ; t<=tst ; ++t)
	{
		int n,i,j,c;
		scanf("%d %s", &n, s);

		c = s[0]-'0';
		j = 0;
		for(i=1 ; i<=n ; ++i)
		{
			int val = s[i]-'0';
			if(val)
			{
				if(c<i)
				{
					j += i-c;
					c = i;
				}
				c += val;
			}
		}
		P("Case #%d: %d\n",t,j);
	}
	return 0;
}
#endif
