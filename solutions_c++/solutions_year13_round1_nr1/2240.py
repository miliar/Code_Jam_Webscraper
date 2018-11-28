#include<cstdio>
#include<cmath>
using namespace std;

int main()
{
	int t;
	long long int sum, r, p, i, count;
	
	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%lld %lld", &r, &p);
		
		count = 0;
		sum = 0;
		for(i=1; ; i+=2)
		{
			sum += (r+i)*(r+i) - (r+i-1)*(r+i-1);
			if(sum > p)
				break;
			++count;
		}
		
		printf("Case #%d: %lld\n", tc, (long long int)((i-1)*0.5));
	}
	
	return 0;
}