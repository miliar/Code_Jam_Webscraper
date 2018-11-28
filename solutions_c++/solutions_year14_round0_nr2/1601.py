#include <cstdio>
#include <iostream>
using namespace std;

int n;

void solve();

int main()
{
	cin >> n;
	for (int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

void solve()
{
	double inc = 2.0, c, f, x;
	cin >> c >> f >> x;
	double t = 0, t1, t2;
	while (true)
	{
		t1 = x / inc;
		t2 = c / inc + x / (f + inc);
		if (t1 > t2)
		{
			t += c / inc;
			inc += f;
		}
		else
		{
			t += t1;
			break;
		}
	}
	printf("%.7f\n", t);
	return;
}
