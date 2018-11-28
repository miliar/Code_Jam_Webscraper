// GCJ2015_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
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

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int qq=1;qq<=tt;qq++) {
		printf("Case #%d: ", qq);
		int row;
		scanf("%d", &row);

		int* values = new int[row + 1];
		
		char c = 'a';
		scanf("%c", &c);

		for(int i = 0; i < row + 1; i++)
		{
			scanf("%c", &c);
			int value = c - '0';
			values[i] = value;
		}
/*		int line;
		scanf("%d", &line);
		int* values = new int[row + 1];
		for(int i = 0; i < row + 1; i++)
		{
			values[row - i] = line%10;
			line = line/10;
		}*/

		int people_Standing = 0;
		int people_Needed = 0;

		for(int i = 0; i < row + 1; i++)
		{
			int value = values[i];

			if(values[i] > 0)
			{
				if(people_Standing>= i)
				{
					people_Standing+= values[i];
				}
				else
				{
					people_Needed += i - people_Standing;
					people_Standing += i - people_Standing + values[i];
				}
			}
		}
		printf("%d\n", people_Needed);
	}
	return 0;
}

