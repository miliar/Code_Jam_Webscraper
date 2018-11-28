#include <stdio.h>

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define MAX_N	16
#define INF_V	0x7FFFFFFF

int gn, gr, gc, gmin;
int board[MAX_N][MAX_N];

int countCells()
{
	int i, j, count = 0;
	for(i=0; i<gr; i++)
	for(j=1; j<gc; j++)
		if(board[i][j] && board[i][j-1])
			count++;

	for(j=0; j<gc; j++)
	for(i=1; i<gr; i++)
		if(board[i][j] && board[i-1][j])
			count++;
	return count;
}

void calc(int y, int x, int remains, int items)
{
	if(y == gr)
	{
		if(items == gn) {
			int n = countCells();
			gmin = min(gmin, n);
		}
		return;
	}

	if( (gn - items) > remains)
		return;

	if(items == gn) {
		// counts.
		int n = countCells();
		gmin = min(gmin, n);
	} else {
		int ny = y, nx = x + 1;
		if(nx >= gc) {
			ny++;
			nx = 0;
		}

		board[y][x] = 1;
		calc(ny, nx, remains-1, items + 1);
		board[y][x] = 0;
	}

	// try next items.
	int ny = y, nx = x + 1;
	if(nx >= gc) {
		ny++;
		nx = 0;
	}
	calc(ny, nx, remains-1, items);
}

void solve(int nCase) {
	cin >> gr >> gc >> gn;

	int cells = (gr * gc);
	int hcells = (cells/2) + (cells % 2);
	if(gn <= hcells) {
		printf("Case #%d: 0\n", nCase);
		return;
	}

	gmin = INF_V;
	memset(board, 0, sizeof(board));
	calc(0, 0, cells, 0);
	printf("Case #%d: %d\n", nCase, gmin);
}

int main(int argc, char *argv[])
{
	// freopen("02.in", "r", stdin);

	int i, t;
	cin >> t;
	for(i=0; i<t; i++)
		solve(i+1);
	return 0;
}