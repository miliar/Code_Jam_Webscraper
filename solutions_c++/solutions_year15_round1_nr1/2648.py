#include <cstdio>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, a[1005];
	int one, two;
	scanf("%d", &t);

	for(int i = 1; i <= t; i++)
	{
		one = two = 0;
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
			scanf("%d", &a[j]);

		for(int j = 0; j < n-1; j++)
			one += max(0, a[j]-a[j+1]);

		int rate = 0;
		for(int j = 0; j < n-1; j++)
			rate = max(rate, a[j]-a[j+1]);
		for(int j = 0; j < n-1; j++)
			two += min(rate, a[j]);

		printf("Case #%d: %d %d\n", i, one, two);
	}

	return 0;
}