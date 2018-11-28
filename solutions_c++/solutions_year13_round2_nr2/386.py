#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
using namespace std;

void InitFiles() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int X, Y;
double ans;
int X_NULL = 100;
int Y_NULL = 100;
bool field[200][200];

void Mark(int x, int y) {
	field[x][y] = 1;
}

void Unmark(int x, int y) {
	field[x][y] = 0;
}

bool CanSlideLeft(int xc, int yc) {
	return yc > Y_NULL && field[xc - 1][yc -1] == 0;
}

bool CanSlideRight(int xc, int yc) {
	return yc > Y_NULL && field[xc + 1][yc -1] == 0;
}

void SlideLeft(int xc, int yc, int& xst, int& yst) {
	while (CanSlideLeft(xc, yc)) {
		--xc;
		--yc;
	}
	xst = xc;
	yst = yc;
}

void SlideRight(int xc, int yc, int& xst, int& yst) {
	while (CanSlideRight(xc, yc)) {
		++xc;
		--yc;
	}
	xst = xc;
	yst = yc;
}

bool Check() {
	return field[X][Y] == 1;
}

void dfs(int n, double pr) {
	if (n == 0) {
		if (Check()) {
			ans += pr;
		}
		return;
	}
	for (int i = 10 + Y_NULL; i >= Y_NULL; --i) {
		if (field[X_NULL][i] == 1) {
			int xc = X_NULL;
			int yc = i + 2;
			if (CanSlideLeft(xc, yc) && !CanSlideRight(xc, yc)) {
				int xst, yst;
				SlideLeft(xc, yc, xst, yst);
				Mark(xst, yst);
				dfs(n - 1, pr);
				Unmark(xst, yst);
			}
			if (!CanSlideLeft(xc, yc) && CanSlideRight(xc, yc)) {
				int xst, yst;
				SlideRight(xc, yc, xst, yst);
				Mark(xst, yst);
				dfs(n - 1, pr);
				Unmark(xst, yst);
			}
			if (CanSlideLeft(xc, yc) && CanSlideRight(xc, yc)) {
				{
					int xst, yst;
					SlideLeft(xc, yc, xst, yst);
					Mark(xst, yst);
					dfs(n - 1, pr * 0.5);
					Unmark(xst, yst);
				}
				{
					int xst, yst;
					SlideRight(xc, yc, xst, yst);
					Mark(xst, yst);
					dfs(n - 1, pr * 0.5);
					Unmark(xst, yst);
				}
			}
			if (!CanSlideLeft(xc, yc) && !CanSlideRight(xc, yc)) {
				Mark(xc, yc);
				dfs(n - 1, pr);
				Unmark(xc, yc);
			}
			return;
		}
	}
	Mark(X_NULL, Y_NULL);
	dfs(n - 1, pr);
	Unmark(X_NULL, Y_NULL);
}

void Solve() {
	int n;
	scanf("%d%d%d", &n, &X, &Y);
	X += X_NULL;
	Y += Y_NULL;
	ans = 0.;
	memset(field, 0, sizeof(field));
	dfs(n, 1);
	printf("%.6lf\n", ans);
}

int main() {
	InitFiles();
	int t;
	char buf[100];
	gets(buf);
	t = atoi(buf);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}