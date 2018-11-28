#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

long long t, i, j, k, n, l, sz, ans;
char s[1000001];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%lld", &t);
	for ( i = 1; i <= t; i++)
	{
		scanf("%s", &s);
		scanf("%lld", &n);
		sz = strlen(s);
		for (j = k = l = ans = 0; j < sz; j++)
		{
			if (s[j] != 'a' && s[j] != 'e' && s[j] != 'i' && s[j] != 'o' && s[j] != 'u') k++;
			else k = 0;
			if (k >= n)
			{
				ans += (sz - j) * (j + 2 - n - l);
				l = j + 2 - n;
				
			}
		}
		printf("Case #%lld: %lld\n", i, ans);
	}

	return 0;
}