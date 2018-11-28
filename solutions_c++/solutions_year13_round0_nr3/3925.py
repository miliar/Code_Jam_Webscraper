#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <math.h>

using namespace std;

typedef unsigned long long u64;

u64 CountFandS(u64 low,u64 high);
bool IsFandS(u64 i);
bool IsPaly(u64 i);
u64 IsFair(u64 i);

int main (void)
{
	string line;
	getline(cin,line);
	
	int cases = atoi(line.c_str()); // First line

	for (int i = 0; i < cases; i++)
	{
		u64 low, high;
		cin >> low;
		cin >> high;
			
		u64 result = CountFandS(low,high);		

		cout << "Case #" << i+1 << ": " << result << endl;
	}	

	return 0;
}

u64 CountFandS(u64 low,u64 high)
{
	u64 result = 0;

	for (u64 i = low; i <= high; i++)
		if (IsFandS(i))
			result ++;

	return result;
}

bool IsFandS(u64 i)
{
	if (!IsPaly(i))
		return false;

	u64 fairResult = IsFair(i);
	if (fairResult == 0)
		return false;

	if (!IsPaly(fairResult))
		return false;

	return true;
}

bool IsPaly(u64 i)
{
	stringstream ss;
	ss << i;
	string input = ss.str();
	string reverse = string(input.rbegin(), input.rend());

	if (input == reverse)
		return true;
	else
		return false;
}

u64 IsFair(u64 i)
{
	double casted = (double) i;
	double result = sqrt(casted);
	u64 recasted = (u64) result;

	if ((recasted*recasted) != i)
		return 0;
	else
		return recasted;
}


