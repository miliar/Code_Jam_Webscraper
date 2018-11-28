#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstdlib>

#include <iostream>

//#include <cctype>
#include <cmath>

#include <fstream>

using namespace std;

//-----------------------------------------------------------------------------------------------//
inline bool ispalindrom(string s)
{
	if (equal(s.begin(), s.begin() + s.size()/2, s.rbegin())) return true;

	return false;

}

//-----------------------------------------------------------------------------------------------//
unsigned long long SolveCaseFFF()
{
	unsigned long long a = 0;
	unsigned long long b = 0;
	cin >> a >> b;

	//cout << "--------------------------------------" << endl;

	unsigned long long lower = sqrt(a);
	if (lower*lower < a) lower++;

	unsigned long long upper = sqrt(b);
	if (upper*upper > b) upper--;

	//cout << "lower = " << lower << endl;
	//cout << "upper = " << upper << endl;


	unsigned long long ans = 0;

	ostringstream ss;
	string s;
	for (unsigned long long i = lower; i <= upper; i++)
	{
		ss.str("");
		ss << i;
		s = ss.str();

		if (ispalindrom(s))
		{
			ss.str("");
			ss << i*i;
			s = ss.str();
			if (ispalindrom(s)) 
			{ 
				//cout << "palindrom is : " << i << " and  " << i*i << endl;
				ans++;
			}
		}
	}

	return ans;
}

//-----------------------------------------------------------------------------------------------//

void FFF()
{
	char line[1000] = {0};
	cin.getline(line,1000);
	
	int testCases = atoi(line);
	for(int i = 0; i < testCases; ++i)
	{
		cout << "Case #" << (i + 1) << ": " << SolveCaseFFF();
		cout << endl;
	}
}


//-----------------------------------------------------------------------------------------------//
//----- main function ---------------------------------------------------------------------------//
//-----------------------------------------------------------------------------------------------//
int main()
{
	FFF();
	return 0;
}
