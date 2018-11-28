#include <iostream>
#include <fstream>
#include <minmax.h>
using namespace std;
int main()
{
	int T;
	double C, F, X, cur, rnd;
	double speed, mon;
	scanf_s("%d", &T);

	std::ofstream fout("file.out");

	fout.unsetf(std::fstream::floatfield);
	fout.precision(44);
	for (int t = 1; t <= T; ++t)
	{
		cin >> C >> F >> X;
		speed = 2;
		cur = 0;
		mon = 0;
	st:rnd = min(C, X - mon);
		cur += rnd / speed;
		if ((X - (mon + rnd)) / speed < (X - mon) / (speed + F))
		{
			mon += rnd;
		}
		else
		{
			speed += F;
		}
		if (mon == X)
		{
			fout << "Case #" << t << ": " << cur << endl;
			continue;
		}
		goto st;
	}
	return 0;
}