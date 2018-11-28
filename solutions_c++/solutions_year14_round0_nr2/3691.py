#include "stdafx.h"

#include <fstream>
#include <iomanip>

using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	double c, f, x;// заведение переменных
	ifstream fin("input.txt"); // открытие файла для чтения данных
	ofstream fout("output.txt"); // открытие на запись
	fin >> t; // чтение двух переменных

	for (int hhh = 1; hhh <= t; hhh++)
	{ 
		fin >> c >> f >> x;
		double time = 0;
		double speed = 2;

		while (x/speed > c/speed + x/(speed+f))
		{
			time += c / speed;
			speed += f;
		}

		time += x / speed;
		fout << "Case #" << hhh << ": " << setprecision(7) << std::fixed << time << endl;
	}
		
}

