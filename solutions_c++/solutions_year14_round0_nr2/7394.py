//#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>

void mofile(), solve(), input(), output(int t);
int test;
double c, f, x, res;

void mofile()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
}

int main()
{
	mofile();
	scanf("%d\n", &test);
	for (int i = 1; i <= test; i++)
	{
		input(); solve(); output(i);
	}
}

void input()
{
	scanf("%lf %lf %lf\n", &c, &f, &x);
}

void solve()
{
	double t =2, h=0, s=0, k=0;
	res = (x / t);
	while (k <= res)
	{
		if (h == 0)
		{
			res = x / t;
		}
		else
		{
			k += (c / t);
			t += f;
			s = (k + x / t );
			if (res > s)
			{
				res = s;
			}
		}
		h += f;
	}
}

void output(int t)
{
	printf("Case #%d: %.7lf\n", t, res);
}