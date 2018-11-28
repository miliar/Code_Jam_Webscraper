#include<stdio.h>
int main()
{
	long long int t,i,j,g1,g2,arr1[4][4],arr2[4][4],m1[4],c=0,no,test=1;
	scanf("%lld",&t);
	while(t--)
	{
		c=0;
		scanf("%lld",&g1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				
				scanf("%lld",&arr1[i][j]);
			}
		}
		scanf("%lld",&g2);
			for(i=0;i<4;i++)
	          {
			    for(j=0;j<4;j++)
			      {
			      	
				    scanf("%lld",&arr2[i][j]);
			      }
              }
              
              for(i=0;i<4;i++)
              {
              	for(j=0;j<4;j++)
              	{
              		
              		if(arr1[g1-1][i]==arr2[g2-1][j])
              		{
              		//	printf("searching for matching");
              			no=arr1[g1-1][i];
              			c++;
              		}
              	}
              }
              
              if(c==0)printf("Case #%lld: Volunteer cheated!\n",test++);
             else if(c==1)printf("Case #%lld: %lld\n",test++,no);
             else printf("Case #%lld: Bad magician!\n",test++);
              
		
	}
	return 0;
}
