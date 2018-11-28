#include<iostream>

using namespace std;

int main()

{

	int t,n,i,j,flag1,flag,k,a,b,c,d,freq[20];

	scanf("%d",&t);

	for(i=1;i<=t;i++)

	{
		
		for(j=1;j<=16;j++)

		freq[j]=2;
		
		scanf("%d",&n);

		for(j=1;j<=4;j++)

		{
		
			scanf("%d %d %d %d",&a,&b,&c,&d);

			if(j==n)
			
				{

					freq[a]--;
	
				freq[b]--;

					freq[c]--;

					freq[d]--;
			
				}

		}
	
		scanf("%d",&n);

		for(j=1;j<=4;j++)

		{
		
			scanf("%d %d %d %d",&a,&b,&c,&d);

			if(j==n)
			
			{

				freq[a]--;

				freq[b]--;

				freq[c]--;

				freq[d]--;

			}
		
		}

		flag=flag1=0;

		for(j=1;j<=16;j++)

		{
			
			if(freq[j]==0)

			{
	
				flag=1;
				
				for(k=j+1;k<=16;k++)

				if(freq[k]==0)
	
				{
		
					flag1=1;

					break;
					
				
				}

				if(flag1==1)

				printf("Case #%d: Bad magician!\n",i);

				else
				
				printf("Case #%d: %d\n",i,j);

				break;
		
			}

		}

		if(!flag)
		
		printf("Case #%d: Volunteer cheated!\n",i);
		

		}

	return 0;

}