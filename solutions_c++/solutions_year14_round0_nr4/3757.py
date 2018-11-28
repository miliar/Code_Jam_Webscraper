#include<stdio.h>
#include <iostream>     // std::cout
#include <algorithm> 
using namespace std;
int main()
{ 
	int T,N,i,j;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%d",&N);
		double Nao1[N],Nao2[N],Ken1[N],Ken2[N];
		for(j=0;j<N;j++)
		{
			scanf("%lf",&Nao1[j]);
		}
		for(j=0;j<N;j++)
		{
			scanf("%lf",&Ken1[j]);
		}
		sort(Nao1,Nao1+N);
		sort(Ken1,Ken1+N);
		for(j=0;j<N;j++)
		{
			Nao2[j]=Nao1[j];
			Ken2[j]=Ken1[j];
		}
		int t=N;
		int lose=0;
		while(t--)
		{
			if(Nao1[0]<Ken1[0])
			{
				lose++;
				for(j=0;j<N-1;j++)
					Nao1[j]=Nao1[j+1];
					
			}
			else
			{
				for(j=0;j<N-1;j++)
					Nao1[j]=Nao1[j+1];
				for(j=0;j<N-1;j++)
					Ken1[j]=Ken1[j+1];
				
			}
		}
		printf("Case #%d: %d ",i+1,N-lose);
		t=N;
		int k;
		lose=0;
		while(t--)
		{
			int flag=0;
			for(j=0;j<=t;j++)
			{
				if(Ken2[j]>Nao2[0])
				{
					for(k=0;k<t;k++)
						Nao2[k]=Nao2[k+1];
					for(k=j;k<t;k++)
						Ken2[k]=Ken2[k+1];
					lose++;
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				for(k=0;k<t;k++)
					Nao2[k]=Nao2[k+1];
				for(k=0;k<t;k++)
					Ken2[k]=Ken2[k+1];
			}
			
		}
		printf("%d\n",N-lose);
	}
    return 0;
}

