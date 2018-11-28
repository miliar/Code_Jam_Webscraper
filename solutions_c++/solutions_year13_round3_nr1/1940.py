// CodeJamTemplate.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void initialize()
{
}

void solve_case(int test_case)
{
	string name;
	int cConst;
	uint64_t count = 0;

	cin >> name;
	cin >> cConst;

	vector<int> convertedName;

	convertedName.reserve(name.length());

	uint64_t curCount = 0;

	for(auto it = name.rbegin(); it != name.rend(); it++)
	{
		if(*it == 'a' ||
		   *it == 'o' ||
		   *it == 'e' ||
		   *it == 'i' ||
		   *it == 'u')
		{
			curCount = 0;
			convertedName.push_back(0);
		}
		else
		{
			convertedName.push_back(++curCount);
		}


	}

	std::reverse(convertedName.begin(), convertedName.end());

	vector <set <int>> subStrs;
	subStrs.resize(convertedName.size());

	for(int i = 0; i < convertedName.size(); i++)
	{
		if(convertedName[i] < cConst)
			continue;
		else 
		{
			int start = 0;
			int end = convertedName.size() -1;

			while(start <= i)
			{
				while(end >= i + cConst - 1)
				{
					subStrs[start].insert(end);
					end--;
				}
				end = convertedName.size() -1;
				start++;
			}
		}
	}

	for(auto it = subStrs.begin(); it != subStrs.end(); it++)
	{
		count += (*it).size();
	}

	cout << "Case #" << test_case << ": " << count << endl;
	// printf("Case #%d: %.6f\n", test_case, *minIt);
}

int _tmain(int argc, _TCHAR* argv[])
{
	initialize();

	int iCases;
	cin >> iCases;

	for (int i = 1; i <= iCases; i++)
		solve_case(i);

	return 0;
}
