# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <string>
# include <iostream>
# include <map>
# include <set>
# include <algorithm>

using namespace std;

int r, t, test;

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);

	scanf("%d", &test);

	int kase = 0;

	while (test --)
	{
		printf("Case #%d: ", ++kase);

		scanf("%d%d\n", &r, &t);

		int x = r;
		int s = (r + 1) * (r + 1) - r * r;
		int c = 0;

		while (s <= t)
		{
			c ++;
			x += 2;
			s += (x + 1) * (x + 1) - x * x;
		}

		printf("%d\n", c);
	}
}