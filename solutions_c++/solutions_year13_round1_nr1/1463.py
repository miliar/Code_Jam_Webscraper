#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>

#define PI 3.1415926535

std::ofstream out;
double get_paint(double r)
{
	// return (PI*(r+1)*(r+1) - PI*r*r) / PI;
	return ((r+1)*(r+1) - r*r);
}
int main()
{	
	out.open("out.txt");
	int T;
	std::cin >> T;
	for (int cases=1; cases<=T; cases++)
	{
		out << "Case #" << cases << ": ";
		double used = 0;
		double r, t;
		std::cin >> r >> t;
		int cnt = 0;
		while (true)
		{
			used += get_paint(r);
			if (used > t)
				break;
			r += 2;
			cnt ++;
		}
		out << cnt << std::endl;
	}
	out.close();
	system("pause");
}