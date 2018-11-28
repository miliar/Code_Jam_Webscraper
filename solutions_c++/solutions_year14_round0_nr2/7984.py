#include <iostream>
#include <cstdio>

using namespace std;

int T;
double C, F, X, ans, p;

void solve ()
{
	p = 2.;
	ans = X / p;
	double time = 0;
	while (1)
	{
		time += C / p;
		p += F;
		if (time + X / p< ans)
			ans = time + X / p;
		else
			break;
	}
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> T;
	for (int i=1; i <= T; ++i)
	{
		cin >> C >> F >> X;
		solve ();
		//cout << "Case #" << i << ": " << ans << endl;
		printf ("Case #%d: %.7f\n", i, ans);
	}
	return 0;
}