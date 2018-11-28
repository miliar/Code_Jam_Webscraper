#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,m,n,i,j,k=0,c=0;
	int a[4][4],b[4][4];
//	freopen("input.txt",stdin);
	scanf("%d",&t);
	while(t--)
	{	k++;
		c=0;
		int x=-1;
		scanf("%d",&m);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&n);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		m--;
		n--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[m][i]==b[n][j])
				{
					x=a[m][i];
					c++;
				}
			}
		}
		if(c==1)
		{
			printf("Case #%d: %d\n",k,x);
		}
		else if(c==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else
			printf("Case #%d: Bad magician!\n",k);
	}
	return 0;
}
