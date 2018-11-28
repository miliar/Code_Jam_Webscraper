#define _CRT_SECURE_NO_WARNINGS
//#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <math.h>
#include <vector>
#include <fstream>
#include <stack>
#include <ctime>
#include <map>
#include <list>
#include <cstdio>
#include <functional>
#include <bitset>
#include <set>
#include <limits.h>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#define scani(s) scanf("%d", &s)

#define epsilon 1e-5
#define D_MAX 1e200

typedef pair<int, int> pii;
typedef pair<int, bool> pib;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
//	READ("input.in");
//	WRITE("output.txt");
#endif
	
	int t, answer, total;
	string a;
	cin >> t;
	for (int z = 0; z < t; z++)
	{
		cin >> answer >> a;
		answer = total = 0;
		for (int i = 0; i < a.length(); i++)
		{
			if (i > total && a[i] != '0')
			{
				answer += i - total;
				total = i;
			}
			total += (a[i] - '0');
		}
		printf("Case #%d: %d\n", z + 1, answer);
	}

	return 0;
}
