# include <cstdio>
# include <cmath>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <algorithm>
# include <iostream>

using namespace std;

int r, c, w;

int main ()
{
	int t, t1, ans1, ans2 = 0, i;
	scanf ("%d", &t);
	for (t1 = 1; t1 <= t; t1 ++)
	{
		scanf ("%d%d%d", &r, &c, &w);
		printf ("Case #%d: ", t1);
		ans2 = 0;
		for (i = 0; i < r - 1; i ++)
			ans2 += c / w;
		ans1 = c / w + (w - 1);
		if (c % w > 0)
			ans1 ++;
		printf ("%d\n", ans2 + ans1);
		
	}
	return 0;
}

