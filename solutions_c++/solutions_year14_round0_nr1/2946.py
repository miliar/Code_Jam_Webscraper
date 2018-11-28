#include<iostream>
#include<stdio.h>

using namespace std;


int main()
{
	int t,c,ans,n1,n2,a1[17],a2[17];
	
	scanf("%d",&t);
	
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n1);
		
		for(int j=0;j<16;j++)
			scanf("%d", &a1[j]);
	
		scanf("%d",&n2);
		
		for(int j=0;j<16;j++)
			scanf("%d", &a2[j]);
		
		c=0;
	
		for(int j=(n1-1)*4;j<n1*4;j++)
		{			
			for(int k=(n2-1)*4;k<n2*4;k++)
			{				
				if(a1[j] == a2[k])
				{	c++;
					ans = a1[j];
				}	
			}
		}
		if(c==0)
			printf("Case #%d: Volunteer cheated!\n", i);
		else if(c==1)
			printf("Case #%d: %d\n",i,ans );
		else	
			printf("Case #%d: Bad magician!\n",i);
	}

}
