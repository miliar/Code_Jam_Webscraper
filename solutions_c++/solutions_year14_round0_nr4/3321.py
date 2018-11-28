#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

const int MAXN = 1010;
int n;
double a[MAXN];
bool flga[MAXN];
double b[MAXN];
bool flgb[MAXN];

int war()
{
	int ret = 0;
	memset(flgb, 0, sizeof(flgb));
	for (int i = 0; i < n; i++)
	{
		int j = 0;
		for (; j < n; j++)
			if (!flgb[j] && b[j] > a[i])
			{
				flgb[j] = true;
				break;
			}
		
		if (j == n)
		{
			ret += n - i;
			break;
		}
	}
	return ret;
}

int war2()
{
	int ret = 0;
	memset(flgb, 0, sizeof(flgb));
	for (int i = 0; i < n; i++)
	{
		int j = 0;
		for (; j < n; j++)
			if (!flgb[j] && a[i] > b[j])
				break;

		if (j != n)
		{
			flgb[j] = true;
			ret++;
			//printf ("a[%d]=%lf b[j=%d]=%lf\n", i, a[i], j, b[j]);
		}
		else
		{
			//printf ("a[%d]=%lf\n", i, a[i]);
			for (int k = n - 1; k >= 0; k--)
				if (!flgb[k])
				{
					flgb[k] = true;
					break;
				}
		}
	}
	return ret;
}

void pr(double a[])
{
	for (int i = 0; i < n; i++)
		printf ("%.3lf ", a[i]);
	puts ("");
}

int main()
{
	int csnum;
	//freopen ("1.in", "r", stdin);
	//freopen ("b.out", "w", stdout);
	//freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("D-large.in", "r", stdin);
	freopen ("d.out", "w", stdout);
	
	scanf ("%d", &csnum);
	for (int cs = 1; cs <= csnum; cs++)
	{
		scanf ("%d", &n);
		for (int i = 0; i < n; i++)
			scanf ("%lf", &a[i]);
		for (int i = 0; i < n; i++)
			scanf ("%lf", &b[i]);

		sort(a, a + n);
		sort(b, b + n);
	//	pr(a);
	//	pr(b);
		int ans1 = war();
		int ans2 = war2();
		printf ("Case #%d: %d %d\n", cs, ans2, ans1);
	}

	return 0;
}

