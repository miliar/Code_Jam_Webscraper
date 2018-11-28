#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

long long gcd(long long a, long long b)
{
	while(b)
	{
		a %= b;
		swap(a, b);
	}
	return a;
}

int main()
{
	//freopen("Ainput.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("Aoutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		long long p, q;
		scanf("%lld/%lld", &p, &q);

		long long gc = gcd(p, q);
		p /= gc;
		q /= gc;

		long long pw = 1;
		for(int i = 1; i <= 40; ++i, pw *= 2);
		long long g = gcd(pw, q);
		if(q / g != 1)
		{
			printf("Case #%d: impossible\n", tt);
			continue;
		}
		
		pw = 2;
		int i;
		for(i = 1; i <= 40; ++i, pw *= 2)
		{
			double pp = (double)p*pw;

			if(p * pw >= q || pp > q -1e-10)
				break;
		}

		if(i > 40)
			printf("Case #%d: impossible\n", tt);	
		else
			printf("Case #%d: %d\n", tt, i);		
	}
	
	return 0;
}