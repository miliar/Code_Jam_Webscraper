
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;

ll rings(ll r, ll t)
{
	int i;
	for (i = 1; (2*(r + i) - 1)*i <= t; i++) {
		// cout << t - (2*(r + i) - 1)*i << endl;
	}
	return i - 1;
}

ll ringsd(ll r, ll t)
{
	ll delta = 4*r*(r - 1) + 1 + 8*t;
	double x1 = -(2*r - 1)/4 + sqrt(delta)/4;
	double x2 = -(2*r - 1)/4 - sqrt(delta)/4;
	double x = max(x1, x2);
	return (ll)x;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	ll r, t;
	for (int i = 0; i < T; ++i)
	{
		cin >> r >> t;
		cout << "Case #" << i  + 1 << ": " << rings(r, t) << endl;
	}
	return 0;
}
