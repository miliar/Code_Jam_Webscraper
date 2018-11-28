#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<utility>
#include<cmath>

using namespace std;

int GCD(int n1, int remainder)
{
	if (remainder == 0)
		return(n1);
	else { return(GCD(remainder, n1%remainder)); }
}

void reduce(int &n, int &d)
{
	int rdc = 0;
	if (d>n)
		rdc = GCD(d, n);
	else if (d<n)
		rdc = GCD(n, d);
	else
		rdc = GCD(n, d);
	n /= rdc;
	d /= rdc;
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");


	int T = 0;

	fin >> T;

	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << "...\n";
		int P = 1, Q = 1;
		fin >> P >> Q;

		reduce(P, Q);

		cout << P << " " << Q << '\n';

		double temp = log2(Q);
		if (temp != (int)(temp))
		{
			fout << "Case #" << i + 1 << ": impossible\n";
		}
		else if (P == 1)
		{
			fout << "Case #" << i + 1 << ": " << temp << "\n";
		}
		else
		{
			int q = 1, j = 0;
			float tp = (float)P / (float)Q;
			while (1 / (float)q > tp)
			{
				q *= 2;
				j++;
			}
			fout << "Case #" << i + 1 << ": " << j << "\n";
		}

		cout << "Done!\n";
	}

	fin.close();
	fout.close();
	system("pause");

	return 0;
}