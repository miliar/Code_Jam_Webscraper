#include <iomanip>
#include <limits>
#include <iostream>
using namespace std;

double time(int f_count, double c, double f, double x)
{
	if (f_count < 0) return numeric_limits<double>::max();

	double ans = 0;
	int now_f = 0;
	while (now_f < f_count)
	{
		ans += c / (2 + (now_f*f));
		now_f++;
	}
	ans += x / (2 + (now_f*f));
	return ans;
}

double cal(double c, double f, double x)
{
	int left = 0, right = 1, mid;
	while (time(right, c, f, x) >= time(right + 1, c, f, x)) right *= 2;

	double mid_left_time, mid_time, mid_right_time;
	while ( true )
	{
		mid = (left + right) / 2;
		mid_left_time = time(mid - 1, c, f, x);
		mid_time = time(mid, c, f, x);
		mid_right_time = time(mid + 1, c, f, x);
		if (mid_left_time < mid_time) right = mid;
		else if (mid_time > mid_right_time) left = mid;
		else if (mid_left_time > mid_time && mid_right_time > mid_time) return mid_time;

		if (right - left < 4)
		{
			double min_time = numeric_limits<double>::max(), this_time;
			int min_count;
			for (int loop = left; loop <= right; loop++)
			{
				this_time = time(loop, c, f, x);
				if (min_time > this_time)
				{
					min_time = this_time;
					min_count = loop;
				}
			}
			return min_time;
		}
	}

	return mid_time;
}

int main()
{
	int t; cin >> t;
	for (int loop = 1; loop <= t; loop++)
	{
		double c, f, x; cin >> c >> f >> x;
		cout << "Case #" << loop << ": " << std::fixed << std::setprecision(7) << cal(c, f, x) << endl;
	}
}