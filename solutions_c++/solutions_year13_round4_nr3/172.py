#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cstdio>
#include <ctime>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>
#include <complex>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<pii,int> piii;
typedef pair<pii,pii> piiii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;

const int MAXN = 21;

int put;
int nt;
int n;
int A[MAXN];
int B[MAXN];
int a[MAXN];
piii order[MAXN];

inline void init()
{
	memset(a, 0, sizeof a);
	put = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", &A[i]);
	for (int j = 0; j < n; ++j)
	{
		scanf("%d", &B[j]);
		order[j] = piii(pii(A[j], B[j]), j);
	}
	sort(order, order + n);
}

inline int check2()
{
	for (int i = 0; i < n; ++i)
	{
		if (!a[i]) continue;
		int maxA = 0;
		int maxB = 0;
		for (int j = 0; j < i; ++j)
			if (a[j] && a[j] < a[i]) maxA = max(maxA, A[j]);
		for (int j = i + 1; j < n; ++j)
			if (a[j] && a[j] < a[i]) maxB = max(maxB, B[j]);
		if (maxA + 1 != A[i]) return 0;
		if (maxB + 1 != B[i]) return 0;
	}
	return 1;
}

int rec(int x)
{
	if (!check2()) return 0;
	if (put == n) return 1;

	for (int i = 0; i < n; ++i)
	{
		if (a[i]) continue;
		int maxA = 0;
		int maxB = 0;
		for (int j = 0; j < i; ++j)
		{
			if (a[j] && a[j] < x) maxA = max(maxA, A[j]);
		}
		for (int j = i + 1; j < n; ++j)
		{
			if (a[j] && a[j] < x) maxB = max(maxB, B[j]);
		}
		if (maxA + 1 != A[i]) continue;
		if (maxB + 1 != B[i]) continue;
		a[i] = x;
		++put;
		int cur = rec(x + 1);
		if (cur) return 1;
		/*
		cur = rec(x + 1);
		if (cur) return 1;
		*/
		a[i] = 0;
		--put;
	}
	return 0;
}

int MASK;

inline int check()
{
	for (int it = 0; it < n; ++it)
	{
		int i = order[it].second;
		a[i] = it ? a[order[it - 1].second] : 1;
		if (MASK & (1 << it)) ++a[i];
	}
	for (int i = 0; i < n; ++i)
	{
		int maxA = 0;
		int maxB = 0;
		for (int j = 0; j < i; ++j)
			if (a[j] < a[i]) maxA = max(maxA, A[j]);
		for (int j = i + 1; j < n; ++j)
			if (a[j] < a[i]) maxB = max(maxB, B[j]);
		if (maxA + 1 != A[i]) return 0;
		if (maxB + 1 != B[i]) return 0;
	}
	return 1;
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		
		printf("Case #%d: ", tn);
		memset(a, 0, sizeof a);
		put = 0;
		rec(1);
		for (int i = 0; i < n; ++i)
		{
			if (i) printf(" ");
			printf("%d", a[i]);
		}
		/*
		int fnd = 0;
		for (int mask = 0; mask < (1 << n); ++mask)
		{
			MASK = mask;
			if (!check()) continue;
			for (int i = 0; i < n; ++i)
			{
				if (i) printf(" ");
				printf("%d", a[i]);
			}
			fnd = 1;
			break;
		}
		if (!fnd)
		{
			memset(a, 0, sizeof a);
			put = 0;
			for (int i = 0; i < n; ++i)
			{
				if (A[i] == 1 && B[i] == 1)
				{
					++put;
					a[i] = 1;
				}
			}
			int cur = rec(2);
			if (cur)
			{
				for (int i = 0; i < n; ++i)
				{
					if (i) printf(" ");
					printf("%d", a[i]);
				}
			}
		}
		*/
		cerr << check2() << endl;
		printf("\n");
	}

    return 0;
}