# include <cstdio>

using namespace std;

int n;

int main ()
{
	int i, t, t1, cnt = 0, ans = 0;
	char c;
	scanf ("%d", &t);
	for (t1 = 1; t1 <= t; t1 ++)
	{
		scanf ("%d", &n);
		cnt = 0;
		ans = 0;
		
		scanf ("%c", &c);
		
		for (i = 0; i <= n; i ++)
		{
			scanf ("%c", &c);
			if (i <= cnt)
				cnt += (c - '0');
			else
			{
				ans += (i - cnt);
				cnt = i;
				cnt += (c - '0');
			}
		}
		printf ("Case #%d: ", t1);
		printf ("%d\n", ans);
	}
	return 0;
}

