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
		UINT numIntervals = 0;
		input >> numIntervals;
		vector<int> intervals;
		intervals.reserve(numIntervals);
		for (UINT i = 0; i < numIntervals; i++)
		{
			UINT x;
			input >> x;
			intervals.push_back(x);
		}

		int firstMethodResult = 0;
		for (UINT i = 0; i < numIntervals; i++)
		{
			if (i == 0) continue;
			if (intervals[i] < intervals[i - 1])
			{
				firstMethodResult += (intervals[i - 1] - intervals[i]);
			}
		}

		int secondMethodResult = 0;
		int BiggestDifference = 0;
		for (UINT i = 0; i < numIntervals; i++)
		{
			if (i == 0) continue;
			if (intervals[i] < intervals[i - 1])
			{
				BiggestDifference = max(BiggestDifference, (intervals[i - 1] - intervals[i]));
			}
		}
		for (UINT i = 0; i < numIntervals - 1; i++)
		{
			if (intervals[i] <= BiggestDifference)
			{
				secondMethodResult += intervals[i];
			}
			else
			{
				secondMethodResult += BiggestDifference;
			}
		}

		output << firstMethodResult << " " << secondMethodResult << endl;
	}
	input.close();
	output.close();
	return 0;
}


