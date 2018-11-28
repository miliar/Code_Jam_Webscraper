#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("c:\\11.in","r",stdin);
	freopen("c:\\out.txt","w",stdout);
	int t, tt=1;
	scanf("%d", &t);
	while (tt<=t)
	{
		int m,n=0;
		int i,j;
		int x[17];
		scanf("%d", &m);
		for (i=0;i<17;i++) x[i]=0;
		for (i=0;i<(m-1)*4;i++) scanf("%d",&j);
		for (i=0;i<4;i++) 
		{
			scanf("%d",&j);
			x[j]++;
		}
		for (i=0;i<(4-m)*4;i++) scanf("%d",&j);
		scanf("%d", &m);
		for (i=0;i<(m-1)*4;i++) scanf("%d",&j);
		for (i=0;i<4;i++) 
		{
			scanf("%d",&j);
			x[j]++;
		}
		for (i=0;i<(4-m)*4;i++) scanf("%d",&j);
		int c=0;
		for (i=1;i<17;i++)
		{
			if (x[i]>1) {
				n++;
				c =i;
			}
		}
		if (n==1) printf("Case #%d: %d\n",tt,c);
		else if (n==0) printf("Case #%d: Volunteer cheated!\n", tt);
		else printf("Case #%d: Bad magician!\n",tt);
		tt++;
	}
}