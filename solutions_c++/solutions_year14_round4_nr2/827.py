# include <stdio.h>


int a[1010];
int min(int a, int b){return a<b?a:b;}


int main ()
{
	int T, cas, n, i, j;
	freopen ("B-large.in", "r", stdin);
	freopen ("blarge.txt", "w", stdout);
	scanf ("%d", &T);
	for (cas = 1; cas <= T; cas++)
	{
		scanf ("%d", &n);
		for (i = 0; i < n; i++)
			scanf ("%d", &a[i]);
		int ans = 0;
		int nn = n;
		for (i = 0; i < n-1; i++)
		{
			int idx = 0;
			for (j = 1; j < nn; j++) if (a[j] < a[idx])idx = j;
			ans += min(idx, nn-1-idx);
			for (j = idx ; j < nn-1 ; j++) a[j] = a[j+1];
			nn--;
		}
		printf ("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
