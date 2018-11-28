#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#if 1

#define P	printf
#define F	"D-small-attempt3"
#ifndef F
#define F	"R0-4"
#endif

#define N	20

const char* ans[] = {"GABRIEL","RICHARD",""};

int main(void)
{
	freopen("IO/"F".in","r",stdin);
	freopen("IO/"F".out.txt","w",stdout);

	int t,tst;
	scanf("%d", &tst);
	for(t=1 ; t<=tst ; ++t)
	{
		int j=1,r,c,x;
		scanf("%d %d %d", &x, &r, &c);

		if(r<c)
		{
			int v = r;
			r = c;
			c = v;
		}

		do{
			if(x>=7)
				break;

			if((r*c)%x)
			{
				//j = 2;
				break;
			}

			if(x>r)
				break;

			if(x<=c)
			{
				j = 0;
				break;
			}

			if(r==x)
			{
				if(x<=3 || c>=3)
				{
					int v = (x+1)>>1;
					if(v<=c)
						j = 0;
				}
				break;
			}
			j = 0;

		}while(0);

		//P("Case #%d: %d %d %d = %s\n",t,x,r,c,ans[j]);
		P("Case #%d: %s\n",t,ans[j]);
	}
	return 0;
}
#endif

#if 0
Case #3: 4 4 1 = RICHARD
Case #4: 3 3 2 = GABRIEL
Case #6: 4 4 2 = GABRIEL
Case #11: 4 4 1 = RICHARD
Case #12: 3 3 1 = RICHARD
Case #13: 4 4 2 = GABRIEL
Case #16: 3 3 1 = RICHARD
Case #17: 4 4 3 = GABRIEL
Case #33: 3 3 2 = GABRIEL
Case #36: 4 4 3 = GABRIEL
Case #54: 2 2 1 = GABRIEL
Case #56: 2 2 1 = GABRIEL
#endif
