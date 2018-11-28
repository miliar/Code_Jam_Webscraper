#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream infile("B-small-attempt1.in");
	ofstream outfile("B-s.out", ios::out);
	int T;
	infile >> T;
	int testcase;
	for (testcase = 1;testcase <= T;testcase++)
	{

		int n, m;
		int x[110][110];
		infile >> n >> m;
		int i, j;
		for (i = 0;i < n;i++)
		{
			for (j = 0;j < m;j++)
			{
				infile >> x[i][j];
			}
		}

		int Minx[100];
		int cntx[100] = {0};
		for (i = 0;i < n;i++)
		{
			Minx[i] = 999;
			for (j = 0;j < m;j++)
			{
				if (x[i][j] < Minx[i])
					Minx[i] = x[i][j];
			}

			for (j = 0;j < m;j++)
				if (x[i][j] == Minx[i])
					cntx[i]++;
		}

		int Miny[100];
		int cnty[100] = {0};
		for (i = 0;i < m;i++)
		{
			Miny[i] = 999;
			for (j = 0;j < n;j++)
			{
				if (x[j][i] < Miny[i])
					Miny[i] = x[j][i];
			}

			for (j = 0;j < n;j++)
			{
				if (Miny[i] == x[j][i])
					cnty[i] ++;
			}
		}

		bool flag = true;
		for (i = 0;i < n;i++)
		{
			for (j = 0;j < m;j++)
			{
				if (x[i][j] == Minx[i] && x[i][j] == Miny[j] && (cntx[i] < m && cnty[j] < n))
				{
					flag = false;
				}
			}
		}

		outfile << "Case #" << testcase << ": ";
		if (flag)
			outfile << "YES";
		else
			outfile << "NO";
		outfile << endl;
	}
	return 0;
}