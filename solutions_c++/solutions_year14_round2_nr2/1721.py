#include<iostream>
const int MAX_N = 200;
const int MAX_L = 200;

int solve()
{
	int A,B,K;
	int a,b,answer=0;
	scanf("%d%d%d",&A,&B,&K);
	for(a=0;a<A;a++)
	{
		for(b=0;b<B;b++)
		{
			if((a&b)<K)
			{
				//printf("%d %d %d\n",a,b,a&b);
				answer++;
			}
		}
	}
	return answer;
}


int main()
{
	int tests,i,answer;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tests);
	for(i=1;i<=tests;i++)
	{
		
		answer = solve();
		printf("Case #%d: ",i);
		printf("%d\n",answer);
	//	return 0;
	}
	return 0;
}