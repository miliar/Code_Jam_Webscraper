// googlecj2015a.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("j:\\A-large.in");
	ofstream fout("j:\\output", ios_base::out | ios_base::trunc);
	string t;
	getline(fin, t);
	istringstream ss1(t, istringstream::in);
	int times = 0;
	ss1 >> times;
	for (int i = 0; i<times; ++i)
	{
		string line;
		getline(fin, line);
		istringstream stream1(line, istringstream::in);
		int max = 0;
		string digit;
		stream1 >> max >> digit;
		int *pplnum = new int[max+1]{0};

		int y = 0;//solution

		for (int j = 0; j <= max; ++j)
		{
			pplnum[j] = digit[j]-'0';

			int pplsum = 0;
			for (int k = 0; k < j; ++k)
			{
				pplsum += pplnum[k];
			}
			while (!(pplsum >= j) && pplnum[j]>0)
			{
				++y;
				++pplsum;
				++pplnum[0];
			}				
		}
		fout << "Case #" << i + 1 << ": " << y << endl;
	}
	fout.close();
	system("pause");
	return 0;
}

