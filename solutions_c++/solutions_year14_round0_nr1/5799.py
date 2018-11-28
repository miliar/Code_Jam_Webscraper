// ConsoleApplication2.cpp : Defines the entry point for the console application.
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
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int a[5][5], b[4][4];

void solve_case(int test_case)
{
	int i1 = 0, i2;
	cin >> i1; i1--;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> a[i][j];
	cin >> i2; i2--;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> b[i][j];

		int c = 0;
		int res = 0;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; ++j)
		if (a[i1][i] == b[i2][j])
		{
			res = a[i1][i];
			c++;
		}

	if (c == 0)
		printf("Case #%d: Volunteer cheated!\n", test_case);
	else if (c == 1)
		printf("Case #%d: %d\n", test_case, res);
	else
		printf("Case #%d: Bad magician!\n", test_case);
}

int main()
{
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}
