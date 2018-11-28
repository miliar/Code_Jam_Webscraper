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
	const string FILE = "C:/Users/Huynh/Source/Repos/GoogleCodeJam/StandingOvation/Debug/A-large.in";

	// variables
	ifstream input_file(FILE);				// input file stream
	ofstream output_file(FILE + "out.txt");	// output file stream
	int test_cases;							// number of test cases
	int max_shyness;						// the maximum shyness level
	string audience;						// shyness level of audience as a string

	// initialization
	ios::sync_with_stdio(false);

	/****************************************************/

	if (input_file.fail())
		cout << "FAILURE\n";
	input_file >> test_cases;	// get test cases

	// run all test cases
	for (int i = 1; i <= test_cases; i++)
	{
		input_file >> max_shyness;	// get max shyness
		input_file >> audience;		// get audience

		int standing = audience[0] - '0';	// people who will always stand up
		int extra = 0;						// amount of extra people we need for everyone to stand up

		// check the rest of the people
		for (int j = 1; j <= max_shyness; j++)
		{
			// we have enough standing for this shyness level
			if (standing >= j)
			{
				standing += audience[j] - '0';	// people of this shyness level will stand up
			}

			// we need more people
			else
			{
				// find how many more we need
				int extra_needed = j - standing;	
				extra += extra_needed;						
				standing += extra_needed;		//invite friends
				standing += audience[j] - '0';	// add the people who were too shy before we had friends
			}
		}

		output_file << "Case #" << i << ": " << extra << endl;
	}

}