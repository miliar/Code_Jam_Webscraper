/*
ID: eoart2
PROG: transform
LANG: C++
*/
//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:134217728")
#include <cstdio>
#include <iostream>
#include <iomanip> 
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <functional>
#include <cassert>
#include <random>

const long long MOD = 1000000007;
const int INF = 2000000000;
const int MAXN = 200000;
const double EPS = 1e-9;
const int HASH_POW = 7;
const double PI = acos(-1.0);

using namespace std;

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << double(clock()) / CLOCKS_PER_SEC << endl;
#endif
	exit(code);
}

int main()
{
	//cin.sync_with_stdio(0);
	mt19937 mt_rand(time(NULL));
	#ifdef MYDEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	#else
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	#endif

	int CASE;
	scanf("%d", &CASE);
	for (int T = 1; T <= CASE; ++T)
	{
		int n;
		double v, c;
		scanf("%d %lf %lf", &n, &v, &c);
		double r0, c0, r1, c1;
		if (n == 1)
		{
			scanf("%lf %lf", &r0, &c0);
			if (fabs(c - c0) > EPS)
				printf("Case #%d: IMPOSSIBLE\n", T);
			else
				printf("Case #%d: %.7lf\n", T, v/r0);
		}
		else
		{
			scanf("%lf %lf", &r0, &c0);
			scanf("%lf %lf", &r1, &c1);
			if (fabs(c1 - c0) < EPS)
			{
				if (fabs(c - c0) > EPS)
					printf("Case #%d: IMPOSSIBLE\n", T);
				else
					printf("Case #%d: %.7lf\n", T, v/(r0 + r1));
			}
			else
			{
				double v0 = v*(c1 - c)/(c1 - c0), v1 = v*(c - c0)/(c1 - c0);
				if (v0 + EPS <= 0 || v1 + EPS <= 0)
					printf("Case #%d: IMPOSSIBLE\n", T);
				else
					printf("Case #%d: %.7lf\n", T, max(v0/r0, v1/r1));
			}
		}
	}

	my_return(0);
}