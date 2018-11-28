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
	double C, F, X;
	cin >> C >> F >> X;

	double cur_count = 0;
	double cur_rate = 2;
	double cur_time = 0;
	while (cur_count < X - 1e-10)
	{

		double cur_end = cur_time + (X - cur_count) / cur_rate;
		double cur_farm = cur_time + (C - cur_count) / cur_rate;
		double after_farm = cur_farm + (X - cur_count) / (cur_rate + F);

		if (after_farm < cur_end)
		{
			cur_time = cur_farm;
			cur_rate += F;
			cur_count = 0;
		}
		else
		{
			cur_count = X;
			cur_time = cur_end;
		}

	}
	printf("Case #%d: %lf\n", test_case, cur_time);
}

int main()
{
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}
