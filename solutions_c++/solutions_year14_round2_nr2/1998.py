#include <cstdio>

using namespace std;

int a, b, k, t, x, ans;

void solve ()
{
	for (int i=0; i < a; ++i)
		for (int j=0; j < b; ++j)
			if ((i & j) < k)
				ans ++;
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf ("%d", &t);
	for (x = 1; x <= t; ++x)
	{
		ans = 0;
		scanf ("%d%d%d", &a, &b, &k);
		solve ();
		printf ("Case #%d: %d\n", x, ans);
	}
	return 0;
}