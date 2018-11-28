#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
int T;
double C, F, X, f, t;
void solve()
{
	f = 2;
	t = 0;
	while (1) {
		double ub = X / f;
		double b = C / f + X / (f + F);
		if (ub < b)
		{
			t += ub;
			return;
		}
		t += C / f;
		f += F;
	}

}
int main()
{
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cin >> C >> F >> X;
		solve();
		cout << "Case #" << i << ": " << fixed << setprecision(7) << t << endl;
	}
}