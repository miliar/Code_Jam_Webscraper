#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <time.h>
#include <stdio.h>
#include <list>
#include <stdlib.h>
#include <string.h>
#include <list>
#include <functional>
#include <random>
using namespace std;
//#define JUDJE 1488

#ifndef JUDJE

ifstream in("aaa.in");
ofstream out("output.txt");
#define cin in
#define cout out

#endif

#define ll long long
#define MOD 1000000007
#define mp(a, b) make_pair(a, b)
#define PI 3.1415926535
#define EPS 0.00000001
#define pii pair<int, int>
#define INF 1000000000

int main()
{
	int t;
	cin >> t;
	for(int ii = 1; ii <= t; ++ii)
	{
		int n;
		cin >> n;
		vector<int> v(n);
		vector<int> vv(1001);
		for(int i = 0; i < n; ++i)
		{
			cin >> v[i];
			++vv[ v[i] ];
		}

		int ans = 100000;
		int curMin = 0;
		
		for(int i = 1; i <= 1000; ++i)
		{
			int sum = 0;
			for(int j = i; j <= 1000; ++j)
			{
				int c = j / i;
				if(j % i == 0)
					--c;
				sum += c* vv[j];
			}
			sum += i;
			ans = min(ans, sum);
		}

		cout << "Case #" << ii << ": " << ans << "\n";

	}
}
