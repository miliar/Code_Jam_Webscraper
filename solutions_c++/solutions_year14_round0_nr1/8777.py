#include<stdio.h>
int main()
{
	int n,r1,r2,i=0,j=0,k=0,a[4][4],b[4][4],no=0,c=0,f=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&r1);
        scanf("%d %d %d %d",&a[0][0],&a[0][1],&a[0][2],&a[0][3]);
		scanf("%d %d %d %d",&a[1][0],&a[1][1],&a[1][2],&a[1][3]);
		scanf("%d %d %d %d",&a[2][0],&a[2][1],&a[2][2],&a[2][3]);
		scanf("%d %d %d %d",&a[3][0],&a[3][1],&a[3][2],&a[3][3]);
		scanf("%d",&r2);
        scanf("%d %d %d %d",&b[0][0],&b[0][1],&b[0][2],&b[0][3]);
		scanf("%d %d %d %d",&b[1][0],&b[1][1],&b[1][2],&b[1][3]);
		scanf("%d %d %d %d",&b[2][0],&b[2][1],&b[2][2],&b[2][3]);
		scanf("%d %d %d %d",&b[3][0],&b[3][1],&b[3][2],&b[3][3]);
		c=0;
		f=0;
		no=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
		    if(a[r1-1][j]==b[r2-1][k])
		    {
		    
		    no=a[r1-1][j];
		    c++;
		    f=1;
		}
		}
	}
	if(f!=1)
	{
	c=0;
	}
	if(c==1)
	printf("Case #%d: %d\n",i+1,no);
	if(c>1)
	printf("Case #%d: Bad magician!\n",i+1);
	if(c==0)
	{
	
    printf("Case #%d: Volunteer cheated!\n",i+1);
}
	}
	return (0);
}
