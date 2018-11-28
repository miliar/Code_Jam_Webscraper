#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)

const int MAX_N = 128;

int grid[MAX_N][MAX_N];
int max_in_row[MAX_N];
int max_in_col[MAX_N];
int TC, N, M;

int main()
{
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> M;

		fill_n(max_in_row, N, 1);
		fill_n(max_in_col, M, 1);

		FOR(r,0,N) FOR(c,0,M) cin >> grid[r][c];
		FOR(r,0,N) FOR(c,0,M) {
			max_in_row[r] = max(max_in_row[r], grid[r][c]);
			max_in_col[c] = max(max_in_col[c], grid[r][c]);
		}

		bool result = true;
		FOR(r,0,N) FOR(c,0,M) {
			if (grid[r][c] != min(max_in_row[r], max_in_col[c])) {
				result = false;
				break;
			}
			if (!result) break;
		}

		printf("Case #%d: %s\n", tc, (result ? "YES" : "NO"));
	}
}
