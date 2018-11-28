#include <algorithm>
#include <cstdio>

#define MAX_R 5
#define MAX_C 5

using namespace std;

int grid[MAX_R][MAX_C];
int neigh[MAX_R][MAX_C];
bool visited[MAX_R][MAX_C];

int dx[] = { -1, -1, -1,  0,  0, +1, +1, +1 };
int dy[] = { -1,  0, +1, -1, +1, -1,  0, +1 };

char cached_grids[MAX_R][MAX_C][MAX_R * MAX_C][MAX_R][MAX_C];
bool cached_results[MAX_R][MAX_C][MAX_R * MAX_C];

#if 0
#define dprintf(fmt, ...) \
	printf(fmt , ##__VA_ARGS__)
#else
#define dprintf(fmt, ...) \
	(void) 0
#endif

int skip_whitespace()
{
	int ch;
	while (true) {
		ch = getchar_unlocked();
		if (ch != ' ' && ch != '\n')
			break;
	}
	return ch;
}

template<typename T>
T read_unsigned_integer()
{
	T result = (T) 0;
	int ch = skip_whitespace();
	while (ch >= '0' && ch <= '9') {
		result = 10 * result + (ch - '0');
		ch = getchar_unlocked();
	}
	return result;
}

template<typename T>
T read_signed_integer()
{
	T result = (T) 0;
	bool flip = false;
	int ch = skip_whitespace();
	if (ch == '-') {
		flip = true;
		ch = skip_whitespace();
	}
	while (ch >= '0' && ch <= '9') {
		result = 10 * result + (ch - '0');
		ch = getchar_unlocked();
	}
	return flip ? -result : result;
}

char read_character()
{
	return skip_whitespace();
}

int count_neighbours(int r, int c, int x, int y)
{
	int result = 0;
	for (size_t i = 0; i < sizeof(dx) / sizeof(*dx); i++) {
		int nx = x + dx[i];
		if (nx >= 0 && nx < r) {
			int ny = y + dy[i];
			if (ny >= 0 && ny < c) {
				result += (grid[nx][ny] != 0);
			}
		}
	}
	return result;
}

pair<int, int> find_empty_cell(int r, int c)
{
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (grid[i][j] == 0) {
				return make_pair(i, j);
			}
	return make_pair(-1, -1);
}

pair<int, int> find_isolated_cell(int r, int c)
{
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (grid[i][j] == 0 && neigh[i][j] == 0) {
				return make_pair(i, j);
			}
	return make_pair(-1, -1);
}

void dfs(int r, int c, int x, int y)
{
	visited[x][y] = true;
	if (neigh[x][y] != 0)
		return;
	for (size_t i = 0; i < sizeof(dx) / sizeof(*dx); i++) {
		int nx = x + dx[i];
		if (nx >= 0 && nx < r) {
			int ny = y + dy[i];
			if (ny >= 0 && ny < c && grid[nx][ny] == 0 && !visited[nx][ny]) {
				dfs(r, c, nx, ny);
			}
		}
	}
}

bool all_covered(int r, int c)
{
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (grid[i][j] == 0 && !visited[i][j]) {
				return false;
			}
	return true;
}

int solve_instance(int r, int c, int m)
{
	int n = r * c;
	int max_mask = 1 << n;

	pair<int, int> start;
	bool found_solution = false;
	for (int i = 0; i < max_mask; i++) {
		int cnt = 0;
		for (int j = 0, k = i; j < n; j++, k >>= 1) {
			int bit = k & 1;
			grid[j / c][j % c] = bit;
			cnt += bit;
		}
		if (cnt != m)
			continue;
		for (int j = 0; j < r; j++)
			for (int k = 0; k < c; k++)
				neigh[j][k] = count_neighbours(r, c, j, k);
		if (m + 1 != r * c) {
			start = find_isolated_cell(r, c);
		} else {
			start = find_empty_cell(r, c);
		}
#if 0
		if (r == 5 && c == 3 && m == 10) {
			printf("i=%d: %d\n", i, cnt);
			printf("grid:\n");
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++)
					printf(" %d", grid[j][k]);
				printf("\n");
			}
			printf("\n");
			printf("neigh:\n");
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++)
					printf(" %d", neigh[j][k]);
				printf("\n");
			}
			printf("\n");
			printf("> %d %d\n", start.first, start.second);
			printf("\n");
		}
#endif
		if (start.first >= 0 && start.second >= 0) {
			for (int j = 0; j < r; j++)
				fill(visited[j], visited[j] + c, false);
			dfs(r, c, start.first, start.second);
#if 0
			if (r == 5 && c == 3 && m == 10) {
				printf("visited:\n");
				for (int j = 0; j < r; j++) {
					for (int k = 0; k < c; k++)
						printf(" %d", visited[j][k]);
					printf("\n");
				}
				printf("\n");
			}
#endif
			if (all_covered(r, c)) {
				//dprintf("cnt=%d i=%d: good\n", cnt, i);
				found_solution = true;
				break;
			}
		}
	}

	cached_results[r - 1][c - 1][m] = found_solution;
	if (found_solution) {
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (grid[i][j] != 0) {
					cached_grids[r - 1][c - 1][m][i][j] = '*';
				} else {
					cached_grids[r - 1][c - 1][m][i][j] =
						(i == start.first && j == start.second) ? 'c' : '.';
				}
			}
		}
	}

	if (r == 5 && c == 3 && m == 10) {
		dprintf("> r=%d c=%d m=%d: %d\n", r, c, m, cached_results[r - 1][c - 1][m]);
	}

	return 0;
}

int solve_problem(int num_case)
{
	int r, c, m;

	r = read_unsigned_integer<int>();
	c = read_unsigned_integer<int>();
	m = read_unsigned_integer<int>();
/*
	int n = r * c;
	int max_mask = 1 << n;

	pair<int, int> start;
	bool found_solution = false;
	for (int i = 0; i < max_mask; i++) {
		int cnt = 0;
		for (int j = 0, k = i; j < n; j++, k >>= 1) {
			int bit = k & 1;
			grid[j / c][j % c] = bit;
			cnt += bit;
		}
		if (cnt != m)
			continue;
		for (int j = 0; j < r; j++)
			for (int k = 0; k < c; k++)
				neigh[j][k] = count_neighbours(r, c, j, k);
		if (m + 1 != r * c) {
			start = find_isolated_cell(r, c);
		} else {
			start = find_empty_cell(r, c);
		}
#if 0
		printf("i=%d: %d\n", i, cnt);
		printf("neigh:\n");
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++)
				printf(" %d", neigh[j][k]);
			printf("\n");
		}
		printf("\n");
		printf("> %d %d\n", start.first, start.second);
		printf("\n");
#endif
		if (start.first >= 0 && start.second >= 0) {
			for (int j = 0; j < r; j++)
				fill(visited[j], visited[j] + c, false);
			dfs(r, c, start.first, start.second);
#if 0
			printf("visited:\n");
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++)
					printf(" %d", visited[j][k]);
				printf("\n");
			}
			printf("\n");
#endif
			if (all_covered(r, c)) {
				dprintf("cnt=%d i=%d: good\n", cnt, i);
				found_solution = true;
				break;
			}
		}
	}

	printf("Case #%d:\n", num_case);
	if (found_solution) {
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (grid[i][j] != 0)
					printf("*");
				else
					printf("%c", (i == start.first && j == start.second) ? 'c' : '.');
			}
			printf("\n");
		}
	} else {
		printf("Impossible\n");
	}
*/
	printf("Case #%d:\n", num_case);
	if (cached_results[r - 1][c - 1][m]) {
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				printf("%c", cached_grids[r - 1][c - 1][m][i][j]);
			}
			printf("\n");
		}
	} else {
		printf("Impossible\n");
	}

	return 0;
}

int main()
{
	int num_tests;

	for (int r = 1; r <= MAX_R; r++)
		for (int c = 1; c <= MAX_C; c++)
			for (int m = 0; m < r * c; m++)
				solve_instance(r, c, m);

	num_tests = read_unsigned_integer<int>();
	for (int i = 0; i < num_tests; i++)
		solve_problem(i + 1);

	return 0;
}
