#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
	int tc = 0, T;
	long long r, t;
	long double n;
	long long n_floor;
	scanf("%d", &T);

	while(tc<T)
	{
		tc++;
		scanf("%lld %lld", &r, &t);
		n = (2*t)/(sqrt(4*r*(r-1)+8*t+1) + 2*r - 1);
		//cout<<n<<endl;
		//n_floor = n;
		//cout<<n_floor<<endl;
		printf("Case #%d: %lld\n", tc, (long long int)n);
	}
	return 0;
}
