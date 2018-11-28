// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iomanip>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int cnt;

	ifstream fi("in.txt");
	ofstream fo("out.txt");

	fi >> cnt;
	for (int i = 0; i < cnt; i++)
	{
		double c,f,x;
		fi >> c >> f >> x;

		double t_sum = 0.0;
		double t_c = 0.0;
		double t1,t2;
		double cur_f = 2.0 - f;
		do
		{
			t_sum += t_c;
			cur_f += f;
			t_c = c / cur_f;
			t1 = x / cur_f;
			t2 = t_c + x / (cur_f + f);
		} while (t2 < t1);
		t_sum += t1;
		fo << "Case #" << i+1 << ": " << fixed << setprecision(7) << t_sum << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

