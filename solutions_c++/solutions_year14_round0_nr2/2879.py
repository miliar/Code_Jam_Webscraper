#include <cstdio>
#include <iostream>

using namespace std;

void solve()
{
	double c, f, x;
	cin >> c >> f >> x;

	double t0 = x / 2.0;
	double base_time = 0;

	double r = 2.0;

	for(int iter = 0; iter < 1000000; ++iter) {

		int farm = 1;
		double t1 = base_time + c/r + x/(r+f);
		if(t0 < t1) {
			cout.precision(11);
			cout << t0 << endl;
			return;
		}
		t0 = t1;
		base_time += c/r;
		r += f;
	}


}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}