
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;

vector<double> times;
void getTarget(double short_target, double long_target, double factor, double new_factor, double time)
{
	// go for long target
	double t = time;
	t += long_target / factor;
	if (times.size() && *times.rbegin() < t)
		return;
	times.push_back(t);
	// short first, then remaining
	double short_time = short_target / factor;
	short_time += time;
	factor += new_factor;
	getTarget(short_target, long_target, factor, new_factor, short_time);
}
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w+", stdout);
	int totalTestCases;
	cin >> totalTestCases;
	for (int testCase = 1; testCase <= totalTestCases; testCase++)
	{
		times.clear();
		double c, x, f;
		cin >> c >> f >> x;
		getTarget(c, x, 2.0, f, 0.0);
		cout.setf(ios::fixed, ios::floatfield);
		cout << "Case #" << testCase << ": " << setprecision(7) << *min_element(times.begin(), times.end()) << endl;
	}
	return 0;
}

