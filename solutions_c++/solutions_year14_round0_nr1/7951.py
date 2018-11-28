// To infinity and beyond...
// \m/ W!LSP! \m/

#include<stdio.h>

int main()
{
	int t,a1,a2,a[10],b[10],count,no,x=0,g;
	scanf("%d",&t);
	while(t--)
	{
		x++;
		scanf("%d",&a1);
		for(int i= 1 ; i<=4 ;i++ )
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&g);
				if(i==a1)
				{
					a[j] = g;
				}	
			}			
		}
		
		scanf("%d",&a2);
		for(int i= 1 ; i<=4 ;i++ )
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&g);
				if(i==a2)
				{
					b[j] = g;
				}	
			}			
		}
		
		count=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i]==b[j])
				{
					count++;
					no = a[i];
				}
			}
		}
		
		if(count==1)
		{
			printf("Case #%d: %d\n",x,no);
		}
		else
		{
			if(count>1)
			{
				printf("Case #%d: Bad magician!\n",x);
			}
			else
			{
				printf("Case #%d: Volunteer cheated!\n",x);
			}
		}
	}
	return 0;
}
