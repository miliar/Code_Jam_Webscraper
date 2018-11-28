#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main()
{
	freopen("D-small-attempt3.in","r",stdin);
	freopen("data31.out","w",stdout);
	int T;
	float w1[1000];
	float w2[1000];
	int over[1000];
	int mark[1001];
	int over2[1000];
	int mark2[1001];
	int N;
	int count=0;
	int count2=0;
	bool flag=true;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d",&N);
		for(int j=0;j<N;j++)
		{
			scanf("%f",w1+j);
		
		}
		for(int j=0;j<N;j++)
		{
			scanf("%f",w2+j);
		}
		count=0;
		count2=0;
		mark[N]=0;
		mark2[N]=0;
		for(int j=0;j<N;j++)
		{

			over[j]=0;
			mark[j]=0;
			over2[j]=0;
			mark2[j]=0;

		}
		for(int k=0;k<N;k++)
		{
			for(int j=0;j<N;j++)
			{
				if(w2[k]>w1[j])
				{
					over2[k]+=1;
				}
				if(w1[k]>w2[j])
				{
					over[k]+=1;
				}
			}
			if(over2[k]>0)
				mark2[over2[k]]+=1;
			if(over[k]>0)
				mark[over[k]]+=1;	
		}
		for(int k=1;k<=N;k++)
		{
			count+=mark[k];
			if(count>k) count=k;
			count2+=mark2[k];
			if(count2>k) count2=k;
		}
		printf("Case #%d: %d %d\n",i+1,count,N-count2);
	}

	return 0;
}


