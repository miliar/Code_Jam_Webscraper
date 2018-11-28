#include <iostream>
#include <fstream>
#include <limits>
#include <iomanip>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
namespace
{
	const double MaxDouble = std::numeric_limits<double>::infinity();
}

using namespace std;


ofstream output("D:\\out.txt");
bool just_Greter_Than(const int& value)
{
	return value < 10;
}
int Optimal(set<double> & Naiome, set<double>& Ken)
{
	int result = 0;
	while (!Naiome.empty())
	{
	
		double j = *(Naiome.begin());
		Naiome.erase(j);
		auto itr = std::find_if(Ken.begin(), Ken.end(), [j](double const & i) { return i >j; });

		if (itr != Ken.end())
		{
			Ken.erase(itr);
		}
		else
		{
			Ken.erase(Ken.begin());
			result++;
		}
	}
	return result;
}



int Deceitful(set<double> & Naiome, set<double>& Ken)
{
	int result = 0;

	while (!Naiome.empty())
	{
		vector<char> status;
		for (auto it = Naiome.begin(), it2 = Ken.begin(); it != Naiome.end(); ++it, ++it2)
		{
			if (*it > *it2)
				status.push_back('N');
			else
				status.push_back('K');
		}
		auto found = std::find(status.begin(), status.end(), 'K');
		if (found == status.end())
		{
			result = status.size();
			break;
		}
		else
		{
			Naiome.erase(Naiome.begin()); 
			Ken.erase(*(Ken.rbegin()));
		}
	}
	return result;
}
int main()
{
	ifstream file;
	file.open("D:\\in.txt");
	int counter;
	char in[8];
	file >> in;
	counter = atoi(in);
	int testnum = 1;
	int dnumber = 0, warnumber = 0;
	while (!file.eof())
	{
		set<double> warnaiome;
		set<double>warken;
		int Nblocks = 0;
		file >> Nblocks;
		for (int i = 0; i < Nblocks; ++i)
		{
			double n;
			file >> n;
			warnaiome.insert(n);
		}
		for (int i = 0; i < Nblocks; ++i)
		{
			double n;
			file >> n;
			warken.insert(n);
		}
		dnumber = 0; warnumber = 0;
		set<double> dwarNaiome = warnaiome;
		set<double> dwarKen = warken;
		dnumber = Deceitful(dwarNaiome, dwarKen);
		warnumber = Optimal(warnaiome, warken);
		
		output << "Case #" << testnum << ": " << dnumber << " " << warnumber << endl;
		
		
		if (counter == testnum)
			break;
		testnum++;
	}
	return 0;
}