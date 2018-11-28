#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int T;
int lawn[101][101];
int N, M;
int Max = 0;
bool check(int r, int c)
{
	bool res = true;
	int now = lawn[r][c];
	int row = r;
	int col = c;
	bool is_col_same = true;
	bool is_row_same = true;
	while(row >= 0) {
		if (now != lawn[row][col]) {
			is_col_same = false;
			break;
		}
		row--;
	}
	row = r;
	if (is_col_same) {
		while(row < N) {
			if (now != lawn[row][col]) {
				is_col_same = false;
				break;
			}
			row++;
		}
	}
	row = r;
	while(col >= 0) {
		if (now != lawn[row][col]) {
			is_row_same = false;
			break;
		}
		col--;
	}
	col = c;
	if (is_row_same) {
		while(col < M) {
			if (now != lawn[row][col]) {
				is_row_same = false;
				break;
			}
			col++;
		}
	}
	if (!is_row_same && !is_col_same)
		return false;
	return true;
}
int main()
{
	freopen("..\\B-small-attempt2.in","r",stdin);
	freopen("..\\B-small-attempt2.out","w",stdout);
	scanf("%d",&T);

	for(int t = 1;t <= T;t++)
	{
		
		scanf("%d", &N);
		scanf("%d", &M);
		
		for(int i = 0;i < N;++i) {
			for(int j = 0;j < M; ++j) {
				scanf("%d", &lawn[i][j]);
				if (lawn[i][j] > Max)
					Max = lawn[i][j];
			}
		}
		bool is_ok = true;
		for (int i = 0;i < N; ++i) 
		{
			for(int j = 0;j < M; ++j) 
			{
				if (lawn[i][j] != Max && !check(i, j)) {
					is_ok = false;
					break;
				}
			}
			if (!is_ok)
				break;
		}
		if (is_ok) {
			printf("Case #%d: YES\n", t);
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}