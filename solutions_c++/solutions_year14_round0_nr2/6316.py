#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("output2.out");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	int testCases;
	in >> testCases;
	long double c, f, x;
	long double totalCookies, cookiesPerSecond;
	long double totalTime;
	for (int cases = 1; cases <= testCases; cases++)
	{
		totalCookies = 0;
		cookiesPerSecond = 2.0;
		totalTime = 0.0;
		in >> c >> f >> x;
		if (x < c)
			totalTime = x / 2;
		else
		{
			
			totalTime += c / cookiesPerSecond;

			while (1)
			{
				totalCookies = c;
				double way1, way2;
				way1 = (x - totalCookies) / cookiesPerSecond;
				way2 = x /( cookiesPerSecond + f);
				if (way1 < way2)
				{
					totalTime += way1;
					break;
				}
				else
				{
					totalCookies -=c;
					cookiesPerSecond += f;
					totalTime += (c/cookiesPerSecond);
				}
				totalCookies += f;
			}
		}
		out << "Case #" << cases << ": " << totalTime << endl;
		

	}
	return 0;
}