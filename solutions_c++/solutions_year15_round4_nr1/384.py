#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

int firstRow[200], lastRow[200], firstCol[200], lastCol[200];

int R, C;

char grid[200][200];

bool can(int r, int c) {
	return (firstRow[r] != lastRow[r]) || (firstCol[c] != lastCol[c]);
}

int solve() {
	memset(firstRow, -1, sizeof firstRow);
	memset(lastRow, -1, sizeof lastRow);
	memset(firstCol, -1, sizeof firstCol);
	memset(lastCol, -1, sizeof lastCol);
	GI2(R, C);
	FIR(R) scanf("%s", &grid[i][0]);
	REP(r, R) REP(c, C) {
		if (grid[r][c] != '.') {
			if (firstRow[r] == -1)
				firstRow[r] = c;
			lastRow[r] = c;

			if (firstCol[c] == -1)
				firstCol[c] = r;
			lastCol[c] = r;
		}
	}

	int res = 0;
	REP(r, R) REP(c, C) if (grid[r][c] != '.') {
		bool ok = true;
		if (grid[r][c] == '<') {
			if (firstRow[r] == c)
				ok = false;;
		}
		if (grid[r][c] == '>') {
			if (lastRow[r] == c)
				ok = false;;
		}
		
		if (grid[r][c] == '^') {
			if (firstCol[c] == r)
				ok = false;;
		}
		if (grid[r][c] == 'v') {
			if (lastCol[c] == r)
				ok = false;;
		}

		if (ok) continue;
		if (can(r, c))
			++res;
		else
			return -1;
	}


	return res;
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();
		
		if (res >=0 )
			printf("Case #%d: %d\n", tc, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'A';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 0;
		bool LARGE = true;

		if (LARGE) {
			sprintf(in_file, "%c-large.in", TASK);
			sprintf(out_file, "%c-large.out", TASK);
		} else {
			sprintf(in_file, "%c-small-attempt%d.in", TASK,  ATTEMPT);
			sprintf(out_file, "%c-small-attempt%d.out", TASK,  ATTEMPT);
		}

		cerr << in_file <<  endl; freopen(in_file, "rt", stdin);
		cerr << out_file << endl; freopen(out_file, "w", stdout);
	}
}
