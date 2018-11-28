#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("testin.in");
	ofstream fout("testout.out");

	int tests; fin >> tests;

	for (int i = 0; i < tests; i++)
	{
		int n; fin >> n;
		vector <double> naomi(n), ken(n);

		for (int j = 0; j < n; j++)
		{
			fin >> naomi[j];
		}
		for (int j = 0; j < n; j++)
		{
			fin >> ken[j];
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int n_D = 0, n_D1 = 0, n_D2 = 0, n_W = 0;

		for (int j = 0; j < n; j++)
		{
			if (naomi[j]>ken[n - j - 1])
			{
				n_D1++;
			}
		}

		vector<double> naomi2, ken2;
		for (int j = 0; j < n; j++)
		{
			naomi2.push_back(naomi[j]);
			ken2.push_back(ken[j]);
		}

		for (int j = 0; j < n; j++)
		{
			double x = ken2[j];
			bool naomiWins = false;
			for (int k = 0; k < n; k++)
			{
				if (naomi2[k]>x)
				{
					naomi2[k] = 0;
					naomiWins = true;
					break;
				}
			}
			if (naomiWins)
				n_D2++;
			sort(naomi2.begin(), naomi2.end());
		}

		if (n_D1 > n_D2)
			n_D = n_D1;
		else
			n_D = n_D2;

		for (int j = 0; j < n; j++)
		{
			double x = naomi[j];
			bool kenWins = false;
			for (int k = 0; k < n; k++)
			{
				if (ken[k]>x)
				{
					ken[k] = 0;
					kenWins = true;
					break;
				}
			}
			if (!kenWins)
				n_W++;
			sort(ken.begin(), ken.end());
		}

		fout << "Case #" << i + 1 << ": " << n_D << ' ' << n_W << endl;
	}

	return 0;
}