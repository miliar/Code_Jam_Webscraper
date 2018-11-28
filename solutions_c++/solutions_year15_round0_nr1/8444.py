//chiragjn
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
	int t,n,smax,i,k;
	long long sum,ans;
	string dump;
	scanf("%d\n",&t);
	k=1;
	while(t--)
	{
		ans=0;
		scanf("%d",&smax);
		getchar_unlocked();
		smax++;
		int levels[smax];
		i=0;
		while(smax--)
			levels[i++]=getchar_unlocked()-48;
		smax=i;
		sum=levels[0];
		for(i=1;i<smax;i++)
		{
			if(i>sum)
			{
				ans++;
				sum++;
			}
			sum+=levels[i];
		}
		printf("Case #%d: %lld\n",k,ans);
		getline(std::cin,dump);
		k++;
	}
	return 0;
}