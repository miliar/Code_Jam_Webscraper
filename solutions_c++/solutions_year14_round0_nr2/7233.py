#include<iomanip>
#include<iostream>
using namespace std;

long double solve()
{
	long double c, f, x;
	cin >> c >> f >> x;
	long double y(2.0);
	long double ans(x / y);
	if(x < c) return ans;
	long double base(0);
	long double best;
	do
	{
		best = ans;
		base += c / y;
		y += f;
		ans = base + x / y;
	} while(ans < best);
	return best;
}

int main()
{
	int t;
	cin >> t;
	cout << fixed << setprecision(7);
	for(int i(1); i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
}
