#include "bits/stdc++.h"

using namespace std;

int N,K;
int ar[5][5];
int used1[17];
int used2[17];

void read()
{
	scanf(" %d",&N);
	
	for(int i=1;i<=N;i++)
	{
		memset(used1,0,sizeof(used1));
		memset(used2,0,sizeof(used2));
		
		scanf(" %d",&K);
		
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
			{
				scanf(" %d",&ar[j][k]);
				
				if(j==K)
					used1[ar[j][k]]++;
			}
		
		scanf(" %d",&K);
		
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
			{
				scanf(" %d",&ar[j][k]);
				
				if(j==K)
					used2[ar[j][k]]++;
			}
			
		int sum=0;
		int a=0;
		
		for(int j=1,b;j<=16;j++)
			if(min(used1[j],used2[j]))
			{
				a=j;
				sum+=min(used1[j],used2[j]);
			}
		
		printf("Case #%d: ",i);
		
		if(!sum)
			puts("Volunteer cheated!");
		
		else if(sum==1)
			printf("%d\n",a);
		
		else
			puts("Bad magician!");
	}
}

int main()
{
	read();
	
	return 0;
}
