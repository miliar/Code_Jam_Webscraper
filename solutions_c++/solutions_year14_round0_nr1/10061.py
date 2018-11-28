#include<stdio.h>
int main()
{
	int a[4][4],b[4][4],a1,b1,n,c[4],i,j,count=0,k,m;

	scanf("%d",&n);
	for(m=1;m<n+1;m++)
	{
		count=0;

	scanf("%d",&a1);
	
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	scanf("%d",&a[i][j]);
	
	for(i=0;i<4;i++)
	{
		c[i]=a[a1-1][i];
	}
	
	
	scanf("%d",&b1);
	
	
	
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	scanf("%d",&b[i][j]);
	
	
	for(j=0;j<4;j++)
	for(i=0;i<4;i++)
	{
		if(c[i]==b[b1-1][j])
		{
		count++;;
		k=j;
		}
	}
	
	if(count>1)
	printf("Case #%d: Bad magician!",m);
	if(count==0)
	printf("Case #%d: Volunteer cheated!",m);
	if(count==1)
	{
		printf("Case #%d: %d",m,b[b1-1][k]);
	}
}
}
