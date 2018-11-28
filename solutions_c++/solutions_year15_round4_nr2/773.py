#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cout.setf(ios::fixed);

	int case_count;
	cin >> case_count;
	for (int case_no = 1; case_no <= case_count; ++case_no)
	{
		cout << "Case #" << case_no << ": ";
		int n;
		double v, x;
		cin >> n >> v >> x;
		vector<double> r(n);
		vector<double> c(n);
		for (int i = 0; i < n; ++i)
			cin >> r[i] >> c[i];

		if (c[0] > x)
		{
			bool larger = true;
			for (int i = 1; i < n; ++i)
				if (c[i] <= x)
				{
					larger = false;
					break;
				}
			if (larger)
			{
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
		}

		if (c[0] < x)
		{
			bool smaller = true;
			for (int i = 1; i < n; ++i)
				if (c[i] >= x)
				{
					smaller = false;
					break;
				}
			if (smaller)
			{
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
		}

		if (n == 2)
		{
			if (c[0] != c[1])
			{
				double t1 = v * (c[0] - x) / (r[1] * (c[0] - c[1]));
				double t0 = v * (c[1] - x) / (r[0] * (c[1] - c[0]));
				cout << max(t1, t0) << endl;
			}
			else
				cout << v / (r[0] + r[1]) << endl;
		}
		else
			cout << v / r[0] << endl;
	}
}