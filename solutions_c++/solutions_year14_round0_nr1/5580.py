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
const int MAX = 74;
const int MAX2 = 7000;
const int BASE = 1000000000;

int T, a, b;
int A[4][4];
int B[4][4];
int RA[64];
int RB[64];

void Init()
{
	FILL(A, 0);
	FILL(B, 0);
	FILL(RA, 0);
	FILL(RB, 0);
}

void SolveTest(int test)
{
	scanf("%d", &a);
	-- a;
	FOR (i,0,4)
		FOR (j,0,4)
			scanf("%d", &A[i][j]);
	scanf("%d", &b);
	-- b;
	FOR (i,0,4)
		FOR (j,0,4)
			scanf("%d", &B[i][j]);
	FOR (i,0,4)
		FOR (j,0,4)
		{
			RA[A[i][j] - 1] = i;
			RB[B[i][j] - 1] = i;
		}
	VI R;
	FOR (i,0,16)
		if (a == RA[i] && b == RB[i])
			R.PB(i);
	printf("Case #%d: ", test+1);
	if (R.empty())
		printf("Volunteer cheated!\n");
	else
	if (SZ(R) > 1)
		printf("Bad magician!\n");
	else
		printf("%d\n", R[0] + 1);
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("A-small-attempt0.in", "r", stdin);
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