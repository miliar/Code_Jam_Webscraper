#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

static const int MAXN = 212;

int N, K;
double P[MAXN];

double Result;
int Index[MAXN];
double Y[MAXN][MAXN];

bool Compare(int i, int j)
{
	return P[i] < P[j];
}

void Work()
{
	int i, j, k, n;
	for (i = 0; i < N; ++i)
		Index[i] = i;
	sort(Index, Index+N, Compare);
	Result = 0;
	for (i = 0; i <= K; ++i)
	{
		double p = 1;
		Y[0][0] = 1;
		k = 1;
		for (j = 0; j < i; ++j, ++k) {
			for (n = 0; n <= k; ++n)
				Y[k][n] = Y[k - 1][n - 1] * P[Index[j]] + Y[k - 1][n] * (1 - P[Index[j]]);
		}
		for (j = 0; j < K - i; ++j, ++k) {
			for (n = 0; n <= k; ++n)
				Y[k][n] = Y[k - 1][n - 1] * P[Index[N - j - 1]] + Y[k - 1][n] * (1 - P[Index[N - j - 1]]);
		}
		if (Result < Y[K][K/2])
			Result = Y[K][K / 2];
	}
}

void Read()
{
	int i;
	scanf("%d%d", &N, &K);
	for (i = 0; i < N; ++i)
		scanf("%lf", &P[i]);
}

void Write(int t)
{
	printf("Case #%d: %.9lf\n", t, Result);
}

int main()
{
	int i, t;
	scanf("%d", &t);
	for (i = 0; i < t; ++i)
	{
		Read();
		Work();
		Write(i + 1);
	}
	return 0;
}
