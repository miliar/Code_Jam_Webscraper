#include <fstream>
#include <conio.h>
#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");
	double time, ferma, dob, res, time2, sum, ost;
    int count;
	fin >> count;

	for(int i = 0; i < count; ++i)
	{
		sum = 2;
		fin >> ferma >> dob >> res;
		time = res / 2 + 1;
		time2 = res / 2;
		ost = time2;
		while(time2 <= time)
		{
			time = time2;
			time2 = time - ost + ferma / sum;
			sum += dob;
			ost = res / sum;
			time2 += ost;
		}
		fout << "Case #" << i+1 << ": " << fixed << setprecision(8) << time << endl;
	}

	_getch();
	return 0;
}