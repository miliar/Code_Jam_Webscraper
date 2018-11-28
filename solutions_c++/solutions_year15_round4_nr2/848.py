/*
ID: tupcuham1
PROG: prime3
LANG: C++11
*/
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>

using namespace std;

typedef long long ll;
typedef long double real;

ofstream fout("water.out");
ifstream fin("water.in");

real targetVol, targetTemp;
int numSources;
real rates[2];
real temps[2];

bool isImpossible()
{
	if (numSources == 1)
	{
		return temps[0] != targetTemp;
	}
	if (temps[0] < targetTemp && temps[1] < targetTemp) return true;
	if (temps[0] > targetTemp && temps[1] > targetTemp) return true;
	return false;
}

real f()
{
	if (temps[0] == targetTemp)
	{
		real speed = rates[0];
		if (temps[1] == targetTemp) speed += rates[1];
		return targetVol / speed;
	}
	if (temps[1] == targetTemp)
	{
		return targetVol / rates[1];
	}

	if (temps[0] > temps[1])
	{
		swap(temps[0], temps[1]);
		swap(rates[0], rates[1]);
	}

	real tempDiffs[2];
	tempDiffs[0] = targetTemp - temps[0];
	tempDiffs[1] = temps[1] - targetTemp;
	real ttdif = tempDiffs[0] + tempDiffs[1];

	real vol0 = targetVol * tempDiffs[1] / ttdif;
	real vol1 = targetVol * tempDiffs[0] / ttdif;

	return max(vol0 / rates[0], vol1 / rates[1]);
}

int main()
{
	fout << fixed << setprecision(9);

	int numTests;
	fin >> numTests;
	for (int t = 1; t <= numTests; t++)
	{
		fin >> numSources >> targetVol >> targetTemp;
		for (int i = 0; i < numSources; i++)
		{
			fin >> rates[i] >> temps[i];
		}

		fout << "Case #" << t << ": ";
		if (isImpossible())
		{
			fout << "IMPOSSIBLE";
		}
		else
		{
			fout << f();
		}
		fout << endl;
	}

	return 0;
}

/*
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>

using namespace std;

typedef long long ll;


*/