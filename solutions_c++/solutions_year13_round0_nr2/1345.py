#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const int NMax = 110;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int testnum;
	in >> testnum;

	int a[NMax][NMax] = {0};
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		int n, m;
		in >> n >> m;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				in >> a[i][j];


		bool res = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				int c1 = 0;
				for (int t = 0; t < m; t++)
					if (a[i][t] <= a[i][j])
						c1++;
					else
						break;


				int c2 = 0;
				for (int t = 0; t < n; t++)
					if (a[t][j] <= a[i][j])
						c2++;
					else
						break;

				if (c1 < m && c2 < n)
					res = false;
			}

		out << "Case #" << testcase << ": ";
		if (res)
			out << "YES" << endl;
		else
			out << "NO" << endl;
	}
	return 0;
}
