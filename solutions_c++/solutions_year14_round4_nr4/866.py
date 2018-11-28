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
const int MAX = 256;
const int MAX2 = 7000;
const int BASE = 1000000000;

int T, n, m, res, resCnt;
string A[MAX];
int P[MAX];
int C[MAX];
int Next[MAX][MAX][26];
int Cnt[MAX];

void Init()
{
	
}

void Add(int x, int y)
{
	int cur = 0;
	FOR (i,0,SZ(A[x]))
	{
		int c = A[x][i] - 'A';
		if (Next[y][cur][c] == -1)
		{
			FILL(Next[y][Cnt[y]], -1);
			Next[y][cur][c] = Cnt[y] ++;
		}
		cur = Next[y][cur][c];	
	}
}

void Gen(int pos)
{
	if (pos == n)
	{
		FOR (i,0,m)
			if (C[i] == 0)
				return;
		FOR (i,0,m)
		{
			Cnt[i] = 1;
			FOR (j,0,26)
				Next[i][0][j] = -1;
		}
		FOR (i,0,n)
			Add(i, P[i]);
		int sum = 0;
		FOR (i,0,m)
			sum += Cnt[i];
		if (sum > res)
		{
			res = sum;
			resCnt = 1;
		}
		else
		if (sum == res)
			++ resCnt;
	}
	else
	{
		FOR (i,0,m)
		{
			P[pos] = i;
			++ C[i];
			Gen(pos+1);
			-- C[i];
		}
	}
}

void SolveTest(int test)
{
	scanf("%d %d", &n, &m);
	FOR (i,0,n)
		cin >> A[i];
	res = -1;
	resCnt = 0;
	Gen(0);

	printf("Case #%d: %d %d\n", test+1, res, resCnt);
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("D-small-attempt0.in", "r", stdin);
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