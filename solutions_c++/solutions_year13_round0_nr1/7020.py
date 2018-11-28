//#pragma comment(linker, "/stack:16777216")
#include <ctime>
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

#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define FILL(a,v) memset(a,v,sizeof(a))

const double PI = acos(-1.0);
const double EPS = 1e-7;

typedef long long ll;
typedef unsigned long long ull;

char s[4][4];

char checkRows()
{
	for (int i = 0; i != 4; ++i)
	{
		int T=0,X=0,O=0;
		for (int j = 0; j != 4; ++j)
		{
			if (s[i][j] =='T')++T;
			if (s[i][j] =='X')++X;
			if (s[i][j] =='O')++O;
		}
		if ((X == 3 && T == 1) || (X == 4))
			return 'X';
		if ((O == 3 && T == 1) || (O == 4))
			return 'O';
	}
	return '-';
}
char checkCols()
{
	for (int i = 0; i != 4; ++i)
	{
		int T=0,X=0,O=0;
		for (int j = 0; j != 4; ++j)
		{
			if (s[j][i] =='T')++T;
			if (s[j][i] =='X')++X;
			if (s[j][i] =='O')++O;
		}
		if ((X == 3 && T == 1) || (X == 4))
			return 'X';
		if ((O == 3 && T == 1) || (O == 4))
			return 'O';
	}
	return '-';
}
char checkDiags()
{
	int T=0,X=0,O=0;
	for (int j = 0; j != 4; ++j)
	{
		if (s[j][j] =='T')++T;
		if (s[j][j] =='X')++X;
		if (s[j][j] =='O')++O;
	}
	if ((X == 3 && T == 1) || (X == 4))
		return 'X';
	if ((O == 3 && T == 1) || (O == 4))
		return 'O';

	T=0,X=0,O=0;
	for (int j = 0; j != 4; ++j)
	{
		if (s[j][3-j] =='T')++T;
		if (s[j][3-j] =='X')++X;
		if (s[j][3-j] =='O')++O;
	}
	if ((X == 3 && T == 1) || (X == 4))
		return 'X';
	if ((O == 3 && T == 1) || (O == 4))
		return 'O';
	return '-';
}
void solve()
{
	
	getchar();
	gets(s[0]);
	gets(s[1]);
	gets(s[2]);
	gets(s[3]);

	int dots = 0;
	for (int i = 0; i != 16; ++i)
		if (s[i & 3][i >> 2] == '.')
			++dots;
	char resRows = checkRows();
	char resCols = checkCols();
	char resDiags= checkDiags();

	if (resRows == 'X' || resCols == 'X' || resDiags == 'X')
	{
		printf("X won\n");
	}else
	if (resRows == 'O' || resCols == 'O' || resDiags == 'O')
	{
		printf("O won\n");
	}else
	{
		if (dots)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	scanf("%d", &tests);
	++tests;
	for (int i = 1; i != tests; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}





















/*
2
3
11
22
101
111
121
202
212
1001
1111
2002
10001
10101
10201
11011
11111
11211
20002
20102
3948493
5355535
554323455
677707776
691090196
803333308
886898688
*/