#include <fstream>
#include <vector>
#include <algorithm>


using namespace std;


typedef unsigned int UINT;


int main()
{
	ifstream input("input.in");
	ofstream output("output.txt");
	UINT nCases = 0;
	input >> nCases;
	for (UINT _case = 0; _case < nCases; _case++)
	{
		output << "Case #" << _case + 1 << ": ";
		UINT shy_max = 0;
		input >> shy_max;
		vector<UINT> numShy;
		input.ignore();
		for (UINT i = 0; i < shy_max + 1; i++)
		{
			char c;
			input.read(&c, sizeof(c));
			numShy.push_back((UINT)(c-'0'));
		}
		if (shy_max == 0)
		{
			output << 0 << endl;
		}
		else if (shy_max == 1)
		{
			if (numShy[0] == 0)
			{
				output << 1 << endl;
			}
			else
			{
				output << 0 << endl;
			}
		}
		else
		{
			UINT numNeeded = 0;
			UINT curAudience = 0;
			for (UINT i = 0; i < numShy.size(); i++)
			{
				if (curAudience < i) numNeeded = max(numNeeded, (i - curAudience));
				curAudience += numShy[i];
			}
			output << numNeeded << endl;
		}
	}
	return 0;
}


