#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>


using namespace std;

ifstream in("small.in");
ofstream out("small.out");

int main()
{
	int test, t, i, j, x, y;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		in >> x >> y;

		string ans;

		int step = 1, curX = 0;

		if (x < 0)
		{
			for (i = 0 ; i < -x; ++i)
			{
				ans = ans + "EW";
				step+=2;
			}
		}
		if (x > 0)
		{
			for (i = 0 ; i < x; ++i)
			{
				ans = ans + "WE";
				step+=2;
			}
		}

		if (y < 0)
		{
			for (i = 0 ; i < -y; ++i)
			{
				ans = ans + "NS";
				step+=2;
			}
		}
		if (y > 0)
		{
			for (i = 0 ; i < y; ++i)
			{
				ans = ans + "SN";
				step+=2;
			}
		}
		
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}