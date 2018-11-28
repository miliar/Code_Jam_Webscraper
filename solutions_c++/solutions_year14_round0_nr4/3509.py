#include "stdafx.h"

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t, n;// заведение переменных
	ifstream fin("input.txt"); // открытие файла для чтения данных
	ofstream fout("output.txt"); // открытие на запись
	fin >> t; // чтение двух переменны
	
	for (int hhh = 1; hhh <= t; hhh++)
	{	
		fin >> n ;
		vector<double> a(n);
		for (int i = 0; i < n; i++)
			fin >> a[i];
		vector<double> b(n);
		for (int i = 0; i < n; i++)
			fin >> b[i];

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int n1 = 0, n2 = 0;

		for (int i = 0; i + n1 < n;)
		{
			if (a[i] > b[i + n1]) n1++;
			else i++;
		}


		for (int i = 0; i + n2 < n;)
		{
			if (b[i] > a[i + n2]) n2++;
			else i++;
		}

		fout << "Case #" << hhh << ": " << n-n2 << " " << n1 << endl;


	}
}

