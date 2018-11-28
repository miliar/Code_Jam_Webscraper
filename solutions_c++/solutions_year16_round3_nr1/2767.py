#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main()
{
	freopen("5.82.in","r",stdin);  
	freopen("5.82.out","w",stdout);
	int T;
	scanf("%d",&T);
	int k=1;
	while(T--)
	{
		int N;
		scanf("%d",&N);
		int p[N];
		//int sum=0;
		for(int i=0;i<N;i++)
		{
			scanf("%d",&p[i]);
			//sum+=p[i];
		}
		printf("Case #%d: ",k++);
		if(N==2)
		{
			while(p[0]--)
			{
				printf("AB ");
			} 
		}
		else 
		{
			int max=0,max1,max2=-1;
			
			for(int i=0;i<N;i++)
			{
				max=max>p[i]?max:p[i];
				if(p[i]==max)
				max1=i;
			}
			for(int i=0;i<N;i++)
			{
				if(i==max1)
					continue;
				if(p[i]==p[max1])
					max2=i;
			}
			//cout<<max1<<' '<<max2;
			while(p[max1]!=1)
			{
				if(max2==-1)
				{
					char c='A'+max1;
					printf("%c%c ",c,c);
					p[max1]=p[max1]-2;
				}
				else
				{
					char c='A'+max1,c1='A'+max2;
					printf("%c%c ",c,c1);
					p[max1]--;
					p[max2]--;
				}
				max=0;
				max2=-1;
				for(int i=0;i<N;i++)
				{
					max=max>p[i]?max:p[i];
					if(p[i]==max)
						max1=i;
				}
				for(int i=0;i<N;i++)
				{
					if(i==max1)
						continue;
					if(p[i]==p[max1])
						max2=i;
				}
				
			}
			int sum=0;
			for(int i=0;i<N;i++)
			{
				if(p[i]>0)
					sum++;
			}
			int j=0;
			while(sum>2)
			{
				while(p[j]==0)
					j++;
				char c='A'+j; 
				printf("%c ",c);
				p[j]--;
				sum--;
			}
			for(int i=0;i<N;i++)
				if(p[i]!=0)
				{
					char c='A'+i;
					printf("%c",c);
				}	
			 
			
		}
		printf("\n");
	}
} 
