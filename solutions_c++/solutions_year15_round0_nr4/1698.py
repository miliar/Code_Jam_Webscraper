#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) v.begin(), v.end()


void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tt, n, r, c;
	cin >> tt;
	int used[5][5][5];
	memset(used, 0, sizeof used);
	used[2][1][1] = 
	used[2][1][3] = 
	used[2][3][1] = 
	used[2][3][3] = 
	used[3][1][1] = 
	used[3][1][2] = 
	used[3][2][1] = 
	used[3][1][3] = 
	used[3][3][1] = 
	used[3][2][2] = 
	used[3][1][4] = 
	used[3][4][1] = 
	used[3][2][4] = 
	used[3][4][2] = 
	used[3][4][4] =
	used[4][4][1] = 
	used[4][1][4] = 
	used[4][4][2] = 
	used[4][2][4] = 
	1;
	forn(i, 4)
		forn(j, 4)
			used[4][i][j] = 1;

	forn(tc, tt) {
		cin >> n >> r >> c;
		string res = used[n][r][c] ? "RICHARD" : "GABRIEL";
		printf("Case #%d: %s\n", tc+1, res.c_str());
	}
	
}