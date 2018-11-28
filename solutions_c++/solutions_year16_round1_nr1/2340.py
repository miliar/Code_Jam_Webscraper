#pragma comment(linker, "/STACK:268435456")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <fstream>
#include <functional>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <limits.h>
#include <stack>
using namespace std;

#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;

const ld EPS = 1e-16;

i64 t;
string s, s1;

int main()
{
	cout.precision(50);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cin >> t;

	for (int i = 0; i < t; ++i)
	{
	
		cin >> s;
		s1.clear();

		s1.push_back(s[0]);

		for (int j = 1; j < s.size(); ++j)
			if (s[j] < s1[0])
				s1.push_back(s[j]);
			else
				s1 = s[j] + s1;

		cout << "Case #" << i + 1 << ": " << s1 << endl;
	}


	return 0;
}
