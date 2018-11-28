#include <stdio.h>


int main()
{
	freopen("res.txt","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);
	int T,m,n;
	scanf("%d",&T);
	int count = 0;
	for (;T;--T)
	{
		int result = 0;
		scanf("%d",&m);
		short pBox[4][4];
		short *p = (short *)pBox;
		short *pEnd = (short *)pBox+16;
		for (;p<pEnd;++p)
		{
			scanf("%d",p);
		}
		scanf("%d",&n);
		short pBox1[4][4];
		short *p1 = (short *)pBox1;
		short *pEnd1 = (short *)pBox1+16;
		for (;p1<pEnd1;++p1)
		{
			scanf("%d",p1);
		}
		for each (short i in pBox[m-1])
		{
			for each (short j in pBox1[n-1])
			{
				if (i==j)
				{
					if (result!=0)
					{
						printf("Case #%d: Bad magician!\n",++count);
						goto next;
					}
					result = i;
				}
			}
		}
		if (result)
		{
			printf("Case #%d: %d\n",++count,result);
		}
		else
			printf("Case #%d: Volunteer cheated!\n",++count);
next:
		;
	}
	return 0;
}

