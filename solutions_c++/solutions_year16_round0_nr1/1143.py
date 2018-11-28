#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
	int cases, c[10];
	scanf("%d", &cases);
	for (int i = 0; i < cases; ++i)
	{
		bool asleep = false;
		long long n;
		scanf("%lld", &n);
		for (int k = 0; k < 10; ++k) c[k] = 0;
		for (int j = 1; j <= 1000; ++j)
		{
			long long r = n * j;
			while (r) c[r % 10]++, r /= 10;
			bool done = true;
			for (int k = 0; k < 10; ++k)
				if (!c[k]) done = false;
			if (done) 
			{
				printf("Case #%d: %lld\n", i + 1, n * j);
				asleep = true;
				break;
			}
		}
		if (!asleep)
			printf("Case #%d: INSOMNIA\n", i + 1);
	}
	
	return 0;
}
