#include <iostream>

#pragma warning(disable : 4996)

using namespace std;

double f(double cost, double delta, double goal, int n)
{
	double s = goal / (2.0 + (double)n*delta);
	for (int i = 0; i < n; i++)
		s += cost / (2.0 + (double)i*delta);
	return s;
}

double solve(double cost, double delta, double goal)
{
	for (int n = 0;; n++) {
		double t = f(cost, delta, goal, n);
		if (t<f(cost, delta, goal, n + 1))
			return t;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	double c, f, x;
	cin >> t;
	cout.setf(ios::fixed);
	cout.precision(7);
	for (int i = 0; i < t; i++) {
		cin >> c >> f >> x;
		cout << "Case #" << i + 1 << ": " << solve(c, f, x) << endl;
	}
	return 0;
}