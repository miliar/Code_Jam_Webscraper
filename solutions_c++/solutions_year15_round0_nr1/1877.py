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

ofstream fout("ovationout.txt");
ifstream fin("ovationin.txt");

int maxShyness;
int shynesses[1005];

int solve()
{
	int numAdded = 0;
	int numStanders = 0;
	for (int shyness = 0; shyness <= maxShyness; shyness++)
	{
		int numNeeded = max(0, shyness - numStanders);
		numAdded += numNeeded;
		numStanders += numNeeded;
		numStanders += shynesses[shyness];
	}
	return numAdded;
}

int main()
{
	int numTests;
	fin >> numTests;
	for (int testIndex = 1; testIndex <= numTests; testIndex++)
	{
		fin >> maxShyness;
		for (int i = 0; i <= maxShyness; i++)
		{
			char c;
			fin >> c;
			shynesses[i] = c - '0';
		}
		fout << "Case #" << testIndex << ": " << solve() << endl;
	}
	
	return 0;
}

/*



*/