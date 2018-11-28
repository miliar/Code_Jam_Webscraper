#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,n,m,count,val,cases=0,i,j,k;
	int a[4][4],b[4][4],c[4],d[4];
	scanf("%d",&t);
	while(t--)
 {
  cases++;
		count=0;
		k=0;
		scanf("%d",&n);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==n-1)
				{
					c[k]=a[i][j];
					k++;
				}
			}
		k=0;
		scanf("%d",&m);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
				if(i==m-1)
				{
					d[k]=b[i][j];
					k++;
				}
			}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(c[i]==d[j])
				{
					count++;
					val=c[i];
				}
			}
		}
		
		if(!count)
			printf("Case #%d: Volunteer cheated!\n",cases);
		else if(count==1)
			printf("Case #%d: %d\n",cases,val);
		else
			printf("Case #%d: Bad magician!\n",cases);
	}
	return 0;
}
