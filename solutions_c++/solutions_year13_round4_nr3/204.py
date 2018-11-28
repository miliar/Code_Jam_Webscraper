#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>
#include <windows.h>

using namespace std;

#pragma comment(linker, "/STACK:167772160")
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;
int N;
bool used[50];
int P[50];
int A[50];
int B[50];

bool check(int pos)
{
	int t = 1;
	for (int i = 0; i < pos; ++i)
	{
		if (P[i] < P[pos])
			t = max(t, A[i] + 1);
		if (P[i] > P[pos] && B[pos] + 1 > B[i])
			return false;
	}
	if (A[pos] != t)
		return false;
	if (P[pos] + 1 < B[pos])
		return false;
	return true;
}

bool check2()
{
	for (int i = 0; i < N; ++i)
	{
		int t = 1;
		for (int j = i + 1; j < N; ++j)
		{
			if (P[j] < P[i])
				t = max(t, B[j] + 1);
		}
		if (B[i] != t)
			return false;
	}
	return true;
}

bool find(int pos)
{
	if (pos == N)
		return check2();
	for (int i = 0; i < N; ++i)
	{
		if (used[i])
			continue;
		P[pos] = i;
		if (!check(pos))
			continue;
		used[i] = true;
		bool f = find(pos + 1);
		used[i] = false;
		if (f)
			return true;
	}
	return false;
}

void solve()
{
	scanf("%d", &N);
	memset(used, false, sizeof(used));
	memset(P, 0, sizeof(P));
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &A[i]);
	}

	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &B[i]);
	}
	find(0);
	for (int i = 0; i < N; ++i)
	{
		int t = 1;
		for (int j = 0; j < i; ++j)
		{
			if (P[j] < P[i])
				t = max(t, A[j] + 1);
		}
		if (A[i] != t)
			printf("!!");
	}
	for (int i = 0; i < N; ++i)
	{
		int t = 1;
		for (int j = i + 1; j < N; ++j)
		{
			if (P[j] < P[i])
				t = max(t, B[j] + 1);
		}
		if (B[i] != t)
			printf("!!");
	}
	for (int i = 0; i < N; ++i)
	{
		printf("%d ", P[i] + 1);
	}
	puts("");
}
int main()
{
	int curTime = GetTickCount();
	freopen("Ctest.txt", "r", stdin);
	freopen("Cout.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	int nxt = 0;
	int step = (T + 999)/1000;
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		if (i < 1000 || i == nxt)
		{
			fprintf(stderr, "\rTest: %3d/%d     Time: %4d ms", i+1, T, (int)(GetTickCount() - curTime));
			if (i == nxt)
				nxt += step;
		}
		solve();
	}
	fprintf(stderr, "\rTest: Done/%d     Time: %4d ms         \n", T, (int)(GetTickCount() - curTime));
	return 0;
}