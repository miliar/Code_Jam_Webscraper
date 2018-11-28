#include <bits/stdc++.h>

using namespace std;

int t;
long long n;
set<int> s;

void parse(long long n)
{
	while (n)
	{
		s.insert(n%10LL);
		n /= 10LL;
	}
}

int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		s.clear();
		scanf("%lld",&n);
		long long iter = 1;
		while (iter < 1000000 && s.size() < 10)
		{
			parse(iter * n);
			iter++;
		}
		if (s.size() < 10)
			printf("Case #%d: INSOMNIA\n",cases);
		else
			printf("Case #%d: %lld\n",cases, (iter-1) * n);
	}
	return 0;
}