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

ofstream fout("pancackesout.txt");
ifstream fin("pancackesin.txt");

const int MAX_NUM_PEOPLE = 1000;
const int MAX_HEIGHT = 1000;

int numPeople;
int heights[MAX_NUM_PEOPLE];

int solve()
{
	int minTime = MAX_HEIGHT;
	for (int allowedHeight = MAX_HEIGHT; allowedHeight > 0; allowedHeight--)
	{
		int curTime = 0;
		for (int p = 0; p < numPeople; p++)
		{
			curTime += (heights[p] - 1) / allowedHeight; 
		}
		curTime += allowedHeight;
		minTime = min(minTime, curTime);
	}
	return minTime;
}

int main()
{
	int numTests;
	fin >> numTests;
	for (int testIndex = 1; testIndex <= numTests; testIndex++)
	{
		fin >> numPeople;
		for (int i = 0; i < numPeople; i++)
		{
			fin >> heights[i];
		}
		fout << "Case #" << testIndex << ": " << solve() << endl;
	}
	
	return 0;
}

/*



*/