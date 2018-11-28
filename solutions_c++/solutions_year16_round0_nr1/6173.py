#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#define MAX 1000000
using namespace std;

int main()
{
	int T,cnt;
	long long int N,ans,n,round,preN;
	set<long long int> number;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%lld",&N);
		number.clear();
		cnt=10;
		round=1;
		preN=N;
		if(N==0)
		{
			ans=0;
		}
		else
		{
			while(cnt!=0)
			{
				//printf("*%lld\n",cnt);
				N=preN*round;
				ans=N;
				round++;
				while(N!=0)
				{
					n=N%10;
					N=N/10;
					if(number.find(n)==number.end())
					{
						//printf("%lld %lld\n",n,cnt);
						number.insert(n);
						cnt--;
						if(cnt==0)
							break;
					}
				}
			}
		}
		printf("Case #%d: ",t);
		if(ans==0)
			printf("INSOMNIA\n");
		else 
			printf("%lld\n",ans);
	}
	return 0;
}