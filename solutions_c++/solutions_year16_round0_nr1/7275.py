#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int mask = 0;
	for (int j = 0; j < 10; j++)
		mask |= (1 << j);
	long long test;
	scanf("%lld", &test);
	for (int t = 1; t <= test; t++)
	{
		long long n;
		scanf("%lld", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		long long i = 0; 
		int tmask = 0, num;
		while (tmask != mask)
		{
			i++;
			num = i * n;
			while (num > 0)
			{
				int rem = num % 10;
				tmask |= (1 << rem);
				num /= 10;
			}
		}
		printf("Case #%d: %d\n", t,  i * n);
	}
	return 0;
}
