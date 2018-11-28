#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;

int main()
{
	int T;
	double B[1100],C[1100];
	int i,j,k,N;
	scanf("%d",&T);
	double sp;
	int ans1,ans2;
	for(k=1;k<=T;k++)
	{
		ans1 = 0;
		ans2 = 0;	
		scanf("%d",&N);
		for(i=0;i<N;i++)
		scanf("%lf",&B[i]);
		for(i=0;i<N;i++)
		scanf("%lf",&C[i]);
		sort(B,B+N);
		sort(C,C+N);
		int t;
		j = N-1;
		t = 0;
		for(i=N-1;i>=0;i--)
		{
			if(B[i]>C[j])
			{
				ans2++,t++;
			}
			else
			j--;
			
		}
		
		
		j = N-1;
		t = 0;
		for(i=0;i<N;i++)
		{
			if(B[i]>C[t])
			ans1++,t++;
			else
			C[j]=0,j--;
			
		}
		printf("Case #%d: %d %d\n",k,ans1,ans2);
		
	}
	return 0;
}
