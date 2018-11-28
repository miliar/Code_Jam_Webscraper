#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector< pair<double, double> > farms; // pair<time, rate>
double C, F, X;

double solve();

int main()
{
	ifstream cin("CookieClicker.in");
	ofstream cout("CookieClicker.txt");

	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		cin >> C >> F >> X;
		cout << "Case #" << t + 1 << ": ";
		cout << fixed << showpoint << setprecision(7) << solve() << endl;
	}

	return 0;
}

double solve()
{
	farms.clear();

	pair<double, double> p = make_pair(0, 2);
	farms.push_back(p);

	for(int i = 1; i < 100000; i++)
	{
		double old_time = farms[i - 1].first;
		double old_rate = farms[i - 1].second;
		pair<double, double> p;
		p.first = C / old_rate + old_time;
		p.second = old_rate + F;
		farms.push_back(p);
	}

	double result = 1000 * 1000;
	for(int i = 0; i < 100000; i++)
	{
		double sol = farms[i].first + X / farms[i].second;
		result = min(result, sol);
	}

	return result;
}
