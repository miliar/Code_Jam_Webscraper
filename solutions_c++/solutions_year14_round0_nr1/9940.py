#include<stdio.h>
using namespace std;
int main()
{
	int k,t;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
    {
	
	int a[4][4],b[4][4];
	int i,j,x,y,m;
	scanf("%d ",&x);
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		 {
		   scanf("%d ",&a[i][j]);	
		 }
		
	}
	
	scanf("%d ",&y);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		 {
		   scanf("%d ",&b[i][j]);	
		 }

	}
	int c=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a[x-1][i]==b[y-1][j])
		    {
		    	c++;
		    
		    if(c==1)
		    {
		    	m=i;
		    }
		    }
		}
	}
	
	if(c==1)
	printf("Case #%d: %d\n",k,a[x-1][m]);
	if(c==0)
	printf("Case #%d: Volunteer cheated!\n",k);
	if(c>1)
	printf("Case #%d: Bad magician!\n",k);
	
   }
	return 0;
}
