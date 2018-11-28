#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

double calc(double speed, double cost, double add, double dist, double res)
{
	if (res < cost/speed)
		return res;
	double innr = calc(speed + add, cost, add, dist, min(res - cost / speed, dist / (speed + add)));
	return min(cost / speed + innr, res);
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		//double res = calc(2, c, f, x, x/2);
		double med = x / c - 2 / f - 1;
		double res = x / 2;
		if (med > 0)
		{
			res = 0;
			int n = (int)floor(med);
			if (med == n)
				n = n - 1;
			double s = 2;
			for (int j = 0; j <= n; j++, s+=f)
			{
				res += c / s;
			}
			res += x / s;
		}
		cout << "Case #" << i << ": " << fixed << setprecision(7) << res << "\n";
	}
	return 0;
}