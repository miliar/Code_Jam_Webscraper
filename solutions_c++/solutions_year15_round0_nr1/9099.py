#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

namespace
{
	unsigned sumElem (const vector<unsigned> & vect, const unsigned begin, const unsigned end)
	{
		unsigned sum (0);
		for (size_t i(begin); i < end; ++i)
			sum += vect [i];
		return sum;
	}
}

int main ()
{
	ifstream input ("input.txt");

	string line;

	getline (input, line);
	unsigned testCases (stoul (line));

	for (unsigned caseNb (1); caseNb <= testCases; ++caseNb)
	{
		getline (input, line);
		istringstream iss (line);
		unsigned SMax (0);
		iss >> SMax;
		++SMax;

		string shyness = string ();
		iss >> shyness;
		vector<unsigned> spectators (SMax);
		unsigned specSupp (0);

		for (size_t i(0); i < SMax; ++i)
		{
			spectators[i] = shyness[i] - '0';

			unsigned sum = sumElem (spectators, 0, i);
			if (sum < i)
			{
				specSupp += i - sum;
				spectators[i-1] += i - sum;
			}
		}
		cout << "Case #" << caseNb << ": " << specSupp << endl;
	}
}
