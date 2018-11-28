#include <cstdio>
#include <queue>
#include <utility>

using namespace std;

int R, C;
int lawn[100][100];

/*
typedef pair<int,int> Point;

struct OrderSmallToBig {
	bool operator() (const Point& lhs, const Point& rhs) const {
		return lawn[rhs.first][rhs.second] < lawn[lhs.first][lhs.second];
	}
};*/

bool can_go_across_row (int r, int c)
{
	for (int col = 0; col < C; col++)
		if (lawn[r][col] > lawn[r][c])
			return false;
	return true;
}

bool can_go_across_col (int r, int c)
{
	for (int row = 0; row < R; row++)
		if (lawn[row][c] > lawn[r][c])
			return false;
	return true;
}

bool ispossible ()
{
	for (int row = 0; row < R; row++) {
		for (int col = 0; col < C; col++) {
			if ((!can_go_across_col(row, col)) && (!can_go_across_row(row, col)))
				return false;
		}
	}
	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("lmower.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%d %d", &R, &C);
		for (int row = 0; row < R; row++)
			for (int col = 0; col < C; col++)
				scanf("%d", &lawn[row][col]);
		if (ispossible())
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}

	return 0;
}