#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int test ,a[4][4],casa=0,i,j,t1,t2,b[4],c[4],temp;
	scanf("%d",&test);
	while(test--)
	{
		casa++;
		scanf("%d",&t1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
			t1=t1-1;
			for(i=0;i<4;i++)
			{
				b[i]=a[t1][i];
			}
		scanf("%d",&t2);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
			t2=t2-1;
			
			for(i=0;i<4;i++)
			c[i]=a[t2][i];
			int count=0;
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(b[i]==c[j])
					{
						count++;
						temp=b[i];
						
					}
					if(count>1)
					break;
				}
				if(count>1)
					break;
			}
				if(count==1)
				printf("case #%d: %d\n",casa,temp);
				else if(count==0)
				printf("Case #%d: Volunteer cheated!\n",casa);
				else 
				printf("Case #%d: Bad magician!\n",casa);
	}
	return 0;
}
