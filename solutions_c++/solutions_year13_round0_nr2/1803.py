#pragma comment (linker, "/STACK:214721677")
#define _CRT_SECURE_NO_WARNINGS
#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <string>
using namespace std;
#define REP(i,n) for (int i=0, _n=(n)-1; i <= _n; ++i)
#define FOR(i,a,b) for (int i=(a), _b=(b); i <= _b; ++i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) ((a).size()))
const double Pi = acos(-1.0);
const double eps = 1e-10;
const double phi = 0.5 + sqrt(1.25);
const int INF = 1000*1000*1000 + 7;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;
typedef bool BOOL;
template < typename T > T sqr (T a) { return (a) * (a); }
template < typename T > T abs (T a) { return (a < 0) ? -(a) : (a); }
template < typename T > T gcd (T a, T b) { return (b) ? gcd(b, a % b) : a; }

#define YES 1
#define NO 0

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int Tests;
	scanf("%d\n", &Tests);
	int a[110][110];
	for (int testNumber = 1; testNumber <= Tests; ++testNumber)
	{
		
		int N, M;
		int highest = 0;
		scanf("%d%d\n", &N, &M);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				scanf("%d", &a[i][j]);
				highest = max(highest, a[i][j]);	
			}
			scanf("\n");
		}

		vector<int> maxInRow (N);
		vector<int> maxInCol (M);

		for (int i = 0; i < N; ++i)
		{
			maxInRow[i] = 0;
			for (int j = 0; j < M; ++j)
				maxInRow[i] = max(maxInRow[i], a[i][j]);
		}
		for (int i = 0; i < M; ++i)
		{
			maxInCol[i] = 0;
			for (int j = 0; j < N; ++j)
				maxInCol[i] = max(maxInCol[i], a[j][i]);
		}

		BOOL capable = YES;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
			{
				if (a[i][j] == highest)
					continue;
				capable &= (a[i][j] == maxInRow[i] || a[i][j] == maxInCol[j]);
			}

		printf("Case #%d: ", testNumber);
		if (capable)
			printf("YES");
		else
			printf("NO");
		printf("\n");
	}
	return EXIT_SUCCESS;
}
