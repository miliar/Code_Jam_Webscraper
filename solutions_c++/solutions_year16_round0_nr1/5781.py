#include <cstdio>

using namespace std;

int main()
{
	bool check[10];
	long long int t,T,N,i,n,tmp,cnt;

	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld",&N);
		printf("Case #%lld: ",t);
		if(N==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		for(i=0;i<10;i++)
			check[i]=false;
		cnt=0;
		for(n=N;;n+=N)
		{
			tmp=n;
			while(tmp!=0)
			{
				if(!check[tmp%10])
				{
					check[tmp%10]=true;
					cnt++;
				}
				tmp/=10;
				if(cnt==10)
					break;
			}
			if(cnt==10)
				break;
		}
		printf("%lld\n",n);
	}
	return 0;
}
