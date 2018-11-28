#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
bool ary[10];
int flag;

long long int count(long long int N)
{
	int i;
	for(i=1;flag<10 &&  i<200;++i)
	{
		long long int K = N*i;
		while(K)
		{
			long long int tmp = K % 10;
			if(ary[tmp]==false)
			{
				ary[tmp]=true;
				++flag;
			}
			K /= 10;
		}
	}
	if(i==200 && flag!=10)
		return -1;
	else
		return N*(i-1);
}



int main()
{
	int tc;
	while(scanf("%d",&tc)==1)
	{
		for(int i=1;i<=tc;++i)
		{
			long long int N,ans;
			flag=0;
			scanf("%lld",&N);
			memset(ary,false,sizeof(ary));
			ans = count(N);
			if(ans == -1)
				printf("Case #%d: INSOMNIA\n",i);
			else
				printf("Case #%d: %lld\n",i,ans);
		}
	}
}
