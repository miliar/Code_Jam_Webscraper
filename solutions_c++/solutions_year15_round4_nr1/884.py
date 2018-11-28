#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int R_MAX = 100;
const int C_MAX = 100;

const char no = '.';
const char up = '^';
const char right = '>';
const char left = '<';
const char down = 'v';

char dane[R_MAX][C_MAX];
bool visited[R_MAX][C_MAX];
int wiersz[R_MAX];
int kolumna[C_MAX];

void print_result(int t, int result) {
	if (result == -1) {
		printf("Case #%d: IMPOSSIBLE\n", t);
	} else {
		printf("Case #%d: %d\n", t, result);
	}
}

void print_dane(int R, int C) {
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			printf("%c", dane[i][j]);
		}
		printf("\n");
	}
}

bool check(int R, int C, int i, int j) {
	return i >= 0 && i < R && j >= 0 && j < C;
}

int go(int R, int C, int i, int j) {
	int direction = dane[i][j];
	while (check(R, C, i, j)) {
		if (direction == up) {
			--i;
		} else if (direction == down) {
			++i;
		} else if (direction == left) {
			--j;
		} else {
			++j;
		}
		if (check(R, C, i, j) && dane[i][j] != no) return 0;
	}
	return 1;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int result = 0;
		int R, C;
		scanf("%d %d", &R, &C);
		getchar();
		vector< pair<int, int> > v;
		for (int i = 0; i < R; ++i) { wiersz[i] = 0; }
		for (int i = 0; i < C; ++i) { kolumna[i] = 0; }
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				dane[i][j] = getchar();
				if (dane[i][j] != no) {
					++wiersz[i];
					++kolumna[j];
					v.push_back(make_pair(i, j));
				}
			}
			getchar();
		}
		for (int i = 0; i < v.size() && result != -1; ++i) {
			pair<int, int> el = v[i];
			if (wiersz[el.first] == 1 && kolumna[el.second] == 1) {
				result = -1;
			} else {
				result += go(R, C, el.first, el.second);
			}
		}
		print_result(t, result);
	}
	return 0;
}