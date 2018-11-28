# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <algorithm>
# include <vector>

using namespace std;

int test, kase = 0;
vector<int> v;

bool palin(int x)
{
	int t = x;
	int a = 0;

	while (t)
	{
		a += t % 10;
		a *= 10;
		t /= 10;
	}

	a /= 10;

	return a == x;
}

int main()
{
	// freopen("a.txt", "r", stdin);

	scanf("%d", &test);


	for (int i = 1; i * i <= 1000; i ++)
		if (palin(i * i) && palin(i)) v.push_back(i * i);

	// for (int i = 0; i < v.size(); i ++) printf("%d\n", v[i]);

	while (test --)
	{
		printf("Case #%d: ", ++ kase);
		int a, b;
		scanf("%d%d", &a, &b);

		int t = lower_bound(v.begin(), v.end(), a) - v.begin();
		int tt = lower_bound(v.begin(), v.end(), b) - v.begin();

		// printf("%d %d\n", t, tt);

		if (v[tt] > b || tt == 5) tt --;

		printf("%d\n", tt - t + 1);
	}
}