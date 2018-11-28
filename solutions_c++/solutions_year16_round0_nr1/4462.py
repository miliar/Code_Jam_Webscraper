#include <stdio.h>
#include <set>
using namespace std;
set<long long int> check;
set<long long int> power_ten;
int main()
{
	long long int T,i,num,N,ori;
	scanf("%lld",&T);
	for(i=1;i<=T;i++)
	{
		check.clear();
		scanf("%lld",&N);
		if(N == 0)
			printf("Case #%lld: INSOMNIA\n",i);
		else
		{
			ori = N;
			while(check.size()!=10)	
			{
				num = N;
				while(num!=0)
				{
					check.insert(num%10);
					num/=10;
				}
				N += ori;
			}
			printf("Case #%lld: %lld\n",i,N-ori);
		}
		
	}
	return 0;
}
