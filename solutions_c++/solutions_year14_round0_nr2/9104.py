#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;


int main()
{
	cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++)
	{
		double C, F, X;

		cin >> C >> F >> X;
		double ans = 1e18;

		double time = 0.0;
		double speed = 2.0;

		for (int i = 0; i <= 100000; i++)
		{
			ans = min(ans, time + X / speed);
			time += C / speed;
			speed += F;
		}
		cout << "Case #" << tc << ": " << setprecision(7) << ans << endl;
	}

}