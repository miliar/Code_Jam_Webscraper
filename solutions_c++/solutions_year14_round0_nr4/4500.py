# include <iostream>
# include <algorithm>

using namespace std;

int n;

double naomi[1024], ken[1024];

int used[1024], ans1, ans2, p , q;

void read ()
{
	int i;
	cin >> n;
	for (i = 0; i < n; i ++)
	cin >> naomi[i];
	for (i = 0; i < n; i ++)
	cin >> ken[i];
}

int main ()
{
	int i, j, mi, r, l, t, k;
	cin >> t;
	for (k = 1; k <= t; k ++)
	{
		ans2 = ans1 = 0;
		for (i = 0; i < 1001; i ++)
		{
			naomi[i] = ken[i] = 0.0;
			used[i] = 0;
		}
		read ();
		sort (naomi, naomi + n);
		sort (ken, ken + n);
		for (i = 0; i < n; i ++)
		{
			l = 0;
			for (j = 0; j < n - i; j ++)
			if (naomi[j + i] < ken[j]) l = 1;
			if (l == 0)
			{
				ans2 = (n - i);
				break;
			}
		}
		for (i = 0; i < n; i ++)
		{
			r = -1;
			mi = 2.0;
			for (j = 0; j < n; j ++)
			if (ken[j] < mi && ken[j] > naomi[i] && used[j] == 0)
			{
				r = j;
				mi = ken[j];
			}
			if (r == -1) ans1 ++;
			else used[r] = 1;
		}
		cout << "Case #" << k << ": ";
		cout << ans2 << " " << ans1 << endl;
	}
	return 0;
}
