# include <stdio.h>
# include <algorithm>


using namespace std;


int a[10010];


int main ()
{
	int T, n;
	int i, j, x;
	freopen ("A-large.in", "r", stdin);
	freopen ("abigout.txt", "w", stdout);
	scanf ("%d", &T);
	for (int cas = 1; cas <= T; cas++)
	{
		scanf ("%d%d", &n, &x);
		for (i = 0; i < n; i++)
			scanf ("%d", &a[i]);
		sort (a, a+n);
		int ans = 0;
		for (i = 0, j = n-1; i < j;)
		{
			while (j > i && a[j]+a[i] > x) j--, ans++;
			
			if (i != j) i++, j--, ans++;
		}
		if (i == j) ans++;
		printf ("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
