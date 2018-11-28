#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007

typedef long long int LL;
typedef unsigned long long int ULL;

const int len=100005;

int main()
{
	LL t, N, c, num, temp;
	scanf("%lld", &t);
	
	c = 1;
	while(t--)
	{
		scanf("%lld", &N);
		
		printf("Case #%lld: ", c);
		
		if(N == 0)printf("INSOMNIA\n");
	
		else
		{
			int dist[10]={0}, d=0;
			for(int i=1; d!=10; ++i)
			{
				num = N*i;
				temp = num;
				
				while(num && d!=10)
				{
					if(dist[num%10] == 0)
					{
						++d;
						dist[num%10]=1;
					}
					
					num /=10;
				}
			}
			
			printf("%lld\n", temp);
		}
		++c;
	}
	
	return 0;
}
