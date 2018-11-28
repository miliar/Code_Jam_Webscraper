#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>
#include <math.h>
#include <map>
#include <utility>


int war(std::vector<double> naomis, std::vector<double> kens)
{
	int nresult = 0;

	for (int i = 0; i < naomis.size(); ++i)
	{
		double s = naomis[i];
		auto gr = std::upper_bound(kens.begin(), kens.end(), s);
		if (gr != kens.end())
			kens.erase(gr);
		else
		{
			kens.erase(kens.begin());
			nresult++;
		}
	}
	return nresult;
}

int dwar(std::vector<double> naomis, std::vector<double> kens)
{
	int nresult = 0;

	for (int i = 0; i < naomis.size(); ++i)
	{
		double s = naomis[i];
		if (s < kens[0])
			s = *(kens.end() - 1) - 0.0000001;
		else
			s = 0.999999999;
		auto gr = std::upper_bound(kens.begin(), kens.end(), s);
		if (gr != kens.end())
			kens.erase(gr);
		else
		{
			kens.erase(kens.begin());
			nresult++;
		}
	}
	return nresult;
}

void solveonecase(std::ifstream& in, std::ofstream& out, int casenumber)
{
	int n;
	in >> n;
	std::vector<double> naomis(n);
	std::vector<double> kens(n);
	for(int i = 0; i < n; ++i)
		in >> naomis[i];
	for(int i = 0; i < n; ++i)
		in >> kens[i];

	std::sort(naomis.begin(), naomis.end());
	std::sort(kens.begin(), kens.end());

	int nresult = war(naomis, kens);
	int nresultd = dwar(naomis, kens);

	out << "Case #" << casenumber <<": " << nresultd << " " << nresult << "\n";

}





void main(void)
{
	std::ifstream in("D-large.in");
	std::ofstream out("D-large.out");
	

	int n;
	in >> n;

	for (int i = 0; i < n; ++i)
	{
		solveonecase(in, out, i + 1);
	}
//	std::cout << "ggg";
	
//	std::system("pause");
}