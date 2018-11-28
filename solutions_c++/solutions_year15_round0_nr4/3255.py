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

int main()
{
	// constants
	const int MAX_X = 5;	// cannot have 5-omino or larger

	const string FILE = "C:/Users/Huynh/Source/Repos/GoogleCodeJam/OminousOmino/Debug/D-small-attempt0.in";

	// variables
	ifstream input_file(FILE);				// input file stream
	ofstream output_file(FILE + "out");		// output file stream
	int test_cases;							// number of test cases
	int X, R, C;							// input data
	bool solution_exists;					// does a solution exists?
	string winner;							// who wins

	// initialization
	ios::sync_with_stdio(false);

	/****************************************************/

	input_file >> test_cases;	// get test cases

	// since the small input is so small you can easily solve it by hand
	// run all test cases
	for (int i = 1; i <= test_cases; i++)
	{
		input_file >> X >> R >> C;	// get input data

		int area = R * C;	// area of the grid

		switch (X)
		{
		case 1:	// 1 omino will always have a solution
		{
					solution_exists = true;
					break;
		}
		case 2:	// 2 omino has a solution if and only if the area is even
		{
					if ((area) % 2 == 0)
						solution_exists = true;
					else
						solution_exists = false;
					break;
		}
		case 3:	// 3 omino has a solution if the area is divisible by 3 and at least 6
		{
					if (area % 3 == 0 && area >= 6)
						solution_exists = true;
					else
						solution_exists = false;
					break;
		}
		case 4:	// 4 omino has a solution if the area is divisible by 4 and at least 12
		{
					if (area % 4 == 0 && area >= 12)
						solution_exists = true;
					else
						solution_exists = false;
					break;
		}					
		}

		if (solution_exists)
			winner = "GABRIEL";
		else
			winner = "RICHARD";

		// output results
		output_file << "Case #" << i << ": " << winner << endl;
	}

}