#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int i,j,tc,m,n,a[4][4],b[4][4],c[4],x,q=0;
	scanf("%d",&tc);
	while(tc--)
	{	q++;
		scanf("%d",&m);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&a[i][j]);
		
		scanf("%d",&n);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&b[i][j]);
		
		for(i=0;i<4;i++)
		c[i]=0;
		x=0;
		for(i=0;i<4;i++)
		{
			
			for(j=0;j<4;j++)
			if(a[m-1][i]==b[n-1][j])
			c[x++]=a[m-1][i];
		}
		
		if(x==1)
		printf("Case #%d: %d\n",q,c[0]);
		if(x>1)
		printf("Case #%d: Bad magician!\n",q);
		if(x==0)
		
		printf("Case #%d: Volunteer cheated!\n",q);
	}
	
	return 0;
}
