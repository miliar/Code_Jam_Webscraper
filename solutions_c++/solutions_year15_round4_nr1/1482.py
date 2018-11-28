#include <iostream>
#include <cstdio>

#pragma warning(disable : 4996)

using namespace std;

char V[101][101];
int OR[101], OC[101];
int R, C;

int get_direction(char c)
{
	if (c == '^')
		return 0;
	else if (c == '>')
		return 1;
	else if (c == 'v')
		return 2;
	else if (c == '<')
		return 3;
	return -1;
}

bool check(int r, int c)
{
	static int dx[] = { 0, 1, 0, -1 };
	static int dy[] = { -1, 0, 1, 0 };
	if (V[r][c] == '.')
		return true;
	int d = get_direction(V[r][c]);
	for (int y = r + dy[d], x = c + dx[d]; y >= 0 && x >= 0 && y < R && x < C; y += dy[d], x += dx[d]) {
		if (V[y][x] != '.')
			return true;
	}
	return false;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	size_t __; cin >> __;
	for (size_t _ = 0; _ < __; ++_) {
		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			cin >> V[i];
		for (int i = 0; i < R; ++i)
			OR[i] = 0;
		for (int i = 0; i < C; ++i)
			OC[i] = 0;
		size_t cnt = 0;
		for (int y = 0; y < R; ++y) {
			for (int x = 0; x < C; ++x) {
				if (V[y][x] != '.') {
					if (!check(y, x))
						++cnt;
					++OR[y];
					++OC[x];
				}
			}
		}
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (V[i][j] != '.' && OR[i] == 1 && OC[j] == 1)
					goto failure;
			}
		}
		
	sucess:
		cout << "Case #" << (_ + 1) << ": ";
		cout << cnt << endl;
		goto end;
	failure:
		cout << "Case #" << (_ + 1) << ": ";
		cout << "IMPOSSIBLE" << endl;
		goto end;
	end:
		;
	}
	return 0;
}