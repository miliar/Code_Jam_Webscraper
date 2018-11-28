#include "stdafx.h"

#include <fstream>

using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t;// заведение переменных
	ifstream fin("input.txt"); // открытие файла для чтения данных
	ofstream fout("output.txt"); // открытие на запись
	fin >> t; // чтение двух переменных
	
	{
		for (int sss = 1; sss <= t; sss++)
		{
			int rn;
			fin >> rn;
			int s[4], d;

			for (int j = 1; j <= 4; j++)
			{
				if (j != rn)
				for (int k = 0; k < 4; k++)
					fin >> d;
				else
				for (int k = 0; k < 4; k++)
					fin >> s[k];

			}

			fin >> rn;
			for (int j = 1; j <= 4; j++)
			{
				if (j != rn)
				for (int k = 0; k < 4; k++)
					fin >> d;
				else
				for (int k = 0; k < 4; k++)
				{
					fin >> d;
					for (int i = 0; i < 4; i++)
					if (s[i] == d)
						s[i] = -s[i];
				}

			}
			int pos = 0;
			int sch = 0;
			for (int i = 0; i < 4; i++)
			if (s[i] < 0)
			{
				sch++; 
				pos = -s[i];
			}
			if (sch == 1)
				fout << "Case #" << sss << ": " << pos << endl;
			else if (sch > 1)
				fout << "Case #" << sss << ": " << "Bad magician!"<< endl;
			else if (sch < 1)
				fout << "Case #" << sss << ": " << "Volunteer cheated!"<< endl;

		}


	}
}



