#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream inf("B-large.in");
	ofstream outf("14q2.txt");
	//ifstream inf("test.in");
	//ofstream outf("test.txt");
	int T;
	inf >> T;
	int k;
	for (k = 1;k <= T;k++)
	{
		double c, f, x;
		inf >> c >> f >> x;
		double s = 2;
		double t = 0;
		double cur = 0;
		while (cur < x)
		{
			if (x - cur < c)
			{
				t += (x - cur)/s;
				break;
			}
			else
			{
				t += (c - cur)/s;
				cur = c;
				if ((x - cur)/s > (x)/(s+f))
				{
					cur = 0;
					s += f;
				}
				else
				{
					t += (x - cur)/s;
					break;
				}
			}
		}
		outf << "Case #" << k << ": ";
		outf << fixed << setprecision(7) << t;
		outf << endl;
	}
	return 0;
}
