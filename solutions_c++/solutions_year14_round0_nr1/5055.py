#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int t, ans1, ans2, a[4][4], b[4][4], count, c[4], d[4], i, j, k, res, flag;
	scanf("%d", &t);
	for(k=1; k<=t; k++)
	{
		count=0;
		scanf("%d", &ans1);
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d", &a[i][j]);
		for(i=0; i<4; i++)
			c[i]=a[ans1-1][i];
		scanf("%d", &ans2);
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d", &b[i][j]);
		for(i=0; i<4; i++)
			d[i]=b[ans2-1][i];
		flag=2;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				if(c[i] == d[j] && count==0)
				{
					count++;
					res=c[i];
					flag=0;
				}
				else if(c[i] == d[j] && count>0)
				{
					flag=1;
					break;
				}
			}
		}
		if(flag==0)
			printf("Case #%d: %d\n", k, res);
		else if(flag==1)
			printf("Case #%d: Bad magician!\n", k);
		else
			printf("Case #%d: Volunteer cheated!\n", k);
	}
	return 0;
}
