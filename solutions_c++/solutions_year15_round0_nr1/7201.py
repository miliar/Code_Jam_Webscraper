#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <hash_map>
#include <queue>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	int cases = 1;
	int N, ans, c;
	char s[2000];

	scanf("%d", &T);
	while (T--)
	{
		ans = c = 0;
		scanf("%d %s", &N, s);
		int L = strlen(s);
		for (int i = 0; i < L; ++i)
		{
			if (s[i] > '0')
			{
				ans += max(0, i - c);
				c = max(c, i) + s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", cases++, ans);
	}

	return 0;
}