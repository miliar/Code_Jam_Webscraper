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
const int MAX = 64;
const int MAX2 = 7000;
const int BASE = 1000000000;

int T;
int n, m, k, w;
VI P;
VI R;
char C[MAX][MAX];
bool B[MAX][MAX];
int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

void Init()
{
	P.clear();
	R.clear();
	FILL(C, 0);
	FILL(B, 0);
}

bool OK(int x, int y)
{
	return (x >= 0 && x < n && y >= 0 && y < m);
}

void dfs(int x, int y)
{
	++ w;
	B[x][y] = 1;
	int cnt = 0;
	FOR (i,0,8)
	{
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (OK(xx, yy))
			if (xx < P[yy])
				++ cnt;
	}
	if (cnt == 0)
	{
		FOR (i,0,8)
		{
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (OK(xx, yy))
				if (B[xx][yy] == 0)
					dfs(xx, yy);
		}
	}
}

void Gen(int pos, int sum)
{
	if (!R.empty())
		return;
	if (pos == m)
	{
		if (sum == k)
		{
			FILL(B, 0);
			w = 0;
			dfs(n-1, 0);
			if (w == n*m-k)
			{
				R = P;
				return;
			}
		}
	}
	else
	{
		int d = (pos == 0);
		FOR (i,0,n+1-d)
			if (sum+i <= k)
			{
				P.PB(i);
				Gen(pos+1, sum+i);
				P.pop_back();
			}
	}
}

void SolveTest(int test)
{
	scanf("%d %d %d", &n, &m, &k);
	Gen(0, 0);
	printf("Case #%d:\n", test+1);
	if (R.empty())
		printf("Impossible\n");
	else
	{
		FOR (i,0,n)
			FOR (j,0,m)
				if (i < R[j])
					C[i][j] = '*';
				else
					C[i][j] = '.';
		C[n-1][0] = 'c';
		FOR (i,0,n)
		{
			FOR (j,0,m)
				printf("%c", C[i][j]);
			printf("\n");
		}
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C-small-attempt0.in", "r", stdin);
		//freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif

	scanf("%d", &T);
	FOR (test,0,T)
	{
		Init();
		SolveTest(test);
	}

	return 0;
}