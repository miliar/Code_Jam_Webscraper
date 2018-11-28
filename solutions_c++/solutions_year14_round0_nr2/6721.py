#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
using namespace std;
double c, f, x;
double solve(double rate)
{
	double result = 0;
	while (x / rate > c / rate + x / (rate + f))
	{
		result += c / rate;
		rate += f;
	}
	return result + x / rate;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> c >> f >> x;
		cout << fixed << setprecision(7) << "Case #" << i << ": " << solve(2) << endl;
	}
	return 0;
}