#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility> 
using namespace std;
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MAX = 20000;
const int MAX2 = 7000;
const int BASE = 1000000000;

int T, n;
int A[MAX];
int Q[MAX];
int B[MAX];

void Init()
{
	
}

void SolveTest(int test)
{
	scanf("%d", &n);
	FOR (i,0,n)
		scanf("%d", &A[i]);
	FOR (i,0,n)
		Q[i] = i;
	int res = INF;
	do
	{
		FOR (i,0,n)
			B[Q[i]] = A[i];
		bool was = 0;
		bool ok = 1;
		FOR (i,1,n)
		{
			if (B[i] < B[i-1])
				was = 1;
			else
				if (was)
					ok = 0;
		}
		if (ok)
		{
			int cnt = 0;
			FOR (i,0,n)
				FOR (j,0,i)
					if (Q[j] > Q[i])
						++ cnt;
			res = min(res, cnt);
		}
	}
	while (next_permutation(Q, Q+n));

	printf("Case #%d: %d\n", test+1, res);
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("B-small-attempt0 (2).in", "r", stdin);
		//freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif

	scanf("%d", &T);
	FOR (test,0,T)
	{
		Init();
		SolveTest(test);
		cerr << test << endl;
	}

	return 0;
}