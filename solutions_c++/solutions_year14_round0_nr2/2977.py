

#include<iostream>
#include<iomanip>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

double time(int n, double x, double c, double f)
{
	double t = 0;
	for (int i = 0; i < n; ++i)
	{
		t = t + c / (2 + f*i);
	}
	t = t + x / (2 + n*f);
	return t;
}
int main()
{
	errno_t err1;
	errno_t err2;
	FILE *fin, *fout;
	err1 = freopen_s(&fin, "in.txt", "r", stdin);
	err2 = freopen_s(&fout, "out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int z = 0; z < T; ++z)
	{
		double x, c, f;
		cin >> c >> f >> x;
		double min_time = 10000000000;
		int l = 0; int r = x;
		while (r-l>10)
		{
			double lt = time(l, x, c, f);
			double rt = time(r, x, c, f);
			double lm = time(l * 2 / 3 + r / 3, x, c, f);
			double rm = time(l / 3 + r * 2 / 3, x, c, f);
			if (lm < rm)
				r = l / 3 + r * 2 / 3;
			else l = l * 2 / 3 + r / 3;
		}
		for (int i = l; i <= r; ++i)
		{
			double t = time(i, x, c, f);
			if (min_time>t)min_time = t;
		}
		cout << "Case #" << z + 1 << ": ";
		printf("%.7lf\n", min_time);
	}

}

