#include "stdafx.h"

#include <fstream>
#include <iomanip>

using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	double c, f, x;// ��������� ����������
	ifstream fin("input.txt"); // �������� ����� ��� ������ ������
	ofstream fout("output.txt"); // �������� �� ������
	fin >> t; // ������ ���� ����������

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

