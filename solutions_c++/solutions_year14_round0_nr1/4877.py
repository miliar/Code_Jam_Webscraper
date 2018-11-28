#include<stdio.h>
int main()
{
	int t,x=1;
	scanf("%d",&t);
	while(t--)
	{
	int a[5][5],i,j,n,m,b[5][5],c=0,k,z;
	
	scanf("%d",&n);
	 for ( i = 0; i <4; i++ )
   {
      for ( j = 0; j < 4; j++ )
      {
         scanf("%d",&a[i][j]);
      }
    }
    scanf("%d",&m);
	 for ( i = 0; i <4; i++ )
   {
      for ( j = 0; j < 4; j++ )
      {
         scanf("%d",&b[i][j]);
      }
    }
	
    for(j=0;j<4;j++)
    {
    	for(z=0;z<4;z++)
    	{
    	if(a[n-1][j]==b[m-1][z])
    	{
    		c++;
    			if(c==1)
    			k=a[n-1][j];
    	}	
    }
    }
    if(c==1)
    printf("Case #%d: %d\n",x,k);
    else if(c>1)
    printf("Case #%d: Bad magician!\n",x);
    else 
    printf("Case #%d: Volunteer cheated!\n",x);
    x++;
}
   return 0;
}
