#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("D.in");
	ofstream fout("D.out");
	int t, n;
	fin >> t;
	for (int urns = 0; urns < t; ++urns)
	{
		fout << "Case #" << urns+1 << ": ";
		int optW = 0, optD = 0;
		fin >> n;
		double nao[n], ken[n];
		for (int j = 0; j < n; ++j)
			fin >> nao[j];
		for (int i = 0; i < n; ++i)
			fin >> ken[i];

		//war
		sort(nao,nao+n);
		sort(ken,ken+n);

		int k = n-1;
		for (int j = n-1; j >= 0; --j)
		{
			if (nao[j] > ken[k]) ++optW;
			else --k;
		}

		//deceitful war
		k = 0;
		for (int j = 0; j < n; ++j)
		{
			if (nao[j] > ken[k])
			{
				++optD;
				++k;
			}
		}
		fout << optD << " " << optW << endl;

	}
}
