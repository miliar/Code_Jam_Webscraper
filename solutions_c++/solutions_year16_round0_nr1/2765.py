#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, n;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d", &n);
		bitset<11> seen;
		printf("Case #%d: ", tc);
		for (int i = 1; i <= 2000000; ++i)
		{
			string s = to_string((long long) n * i);
			for (int j = 0; j < s.length(); ++j)
			{
				seen[s[j] - '0'] = 1;
			}
			if (seen.count() == 10)
			{
				printf("%lld\n", (long long) n * i);
				break;
			}
		}
		if (seen.count() < 10)
		{
			printf("INSOMNIA\n");
		}
	}
	return 0;
}