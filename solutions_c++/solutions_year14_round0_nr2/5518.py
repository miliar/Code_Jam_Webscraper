#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("B.in");
	ofstream fout("bl.out");
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++)
	{
		double c, f, x;
		fin >> c >> f >> x;
		double time = 0.0, rate = 2.0, ans = 1e18;
		for (int i = 0; i <= 1000000; i++)
		{
			double res = time + x / rate;
			ans = min(ans, res);
			time += c / rate;
			rate += f;
		}
		fout << "Case #" << k << ": " << setprecision(8) << fixed << ans << endl;
	}
	return 0;
}

