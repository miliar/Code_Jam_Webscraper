#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
//nyu hn667
int main()
{
	// constants
	const string FILE = "C:/Users/Huynh/Source/Repos/GoogleCodeJam/1A/Debug/A-large.in";

	// variables
	ifstream input_file(FILE);				// input file stream
	ofstream output_file(FILE + "out");		// output file stream
	int test_cases;							// number of test cases
	int ans1;
	int ans2;
	int intervals;
	int mushroom;
	vector<int> mushrooms;

	// initialization
	ios::sync_with_stdio(false);

	/****************************************************/

	input_file >> test_cases;	// get test cases

	// run all test cases
	for (int i = 1; i <= test_cases; i++)
	{
		ans1 = 0;
		ans2 = 0;

		input_file >> intervals;
		mushrooms.clear();

		for (int j = 0; j < intervals; j++)
		{
			input_file >> mushroom;
			mushrooms.push_back(mushroom);
		}

		for (int j = 0; j < intervals - 1; j++)
		{
			int first = mushrooms[j];
			int second = mushrooms[j + 1];
			int change = first - second;

			if (change > 0)
				ans1 += change;
		}

		int rate = -INT_MAX;
		for (int j = 0; j < intervals - 1; j++)
		{
			int first = mushrooms[j];
			int second = mushrooms[j + 1];
			int change = first - second;
			if (change > rate)
				rate = change;
		}

		for (int j = 0; j < intervals - 1; j++)
		{
			int first = mushrooms[j];
			int second = mushrooms[j + 1];
			int change = first - second;

			if (first - rate < 0)
				ans2 += first;
			else 
				ans2 += rate;
			cout << ans2 << endl;
		}
		

		// output results
		output_file << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}

}