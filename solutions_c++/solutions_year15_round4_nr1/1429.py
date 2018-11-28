#include <bits/stdc++.h>
#include <stdint.h>
using namespace std;

typedef uint8_t byte;
typedef int16_t i16;
typedef uint16_t ui16;
typedef int32_t i32;
typedef uint32_t ui32;
typedef int64_t i64;
typedef uint64_t ui64;

#define MOD 1000000007
#define ADD_MOD(a, b) (((a) + (b)) % MOD)
#define MUL_MOD(a, b) i32((i64(a) * i64(b)) % MOD)
#define SUB_MOD(a, b) ((a) >= (b) ? (a) - (b) : (a) + MOD - (b))

int w, h;
char m[100][100];
bool solved[100][100];

char ars[4] = {'>', '<', '^', 'v'};

bool solve(int x, int y, int &res) {
	solved[y][x] = true;

	char ar0 = m[y][x];
	for (int i = 0; i < 5; ++i) {
		char ar = i == 0 ? ar0 : ars[i - 1];
		int dx = 0, dy = 0;

		if (ar == '>') dx = 1;
		else if (ar == '<') dx = -1;
		else if (ar == '^') dy = -1;
		else if (ar == 'v') dy = 1;

		int x1 = x, y1 = y;
		bool s = false;

		int r = 0;
		while (true) {
			x1 += dx;
			y1 += dy;

			if (x1 >= w || x1 < 0 ||
				y1 >= h || y1 < 0) {
				break;
			}

			if (m[y1][x1] != '.') {
				if (solved[y1][x1]) {
					s = true;
				} else {
					s = solve(x1, y1, r);
					if (!s) {
						solved[y][x] = false;
						return false;
					}	
				}
				break;
			}
		}

		if (s) {
			res += r + (ar == ar0 ? 0 : 1);
			return true;
		}
	}

	solved[y][x] = false;
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);

	int testCount;
	cin >> testCount;

	for (int testIndex = 0; testIndex < testCount; ++testIndex) {
		cin >> h >> w;

		for (int y = 0; y < h; ++y) {
			for (int x = 0; x < w; ++x) {
				cin >> m[y][x];
				solved[y][x] = false;
			}
		}

		int res = 0;
		bool failed = false;

		for (int y = 0; y < h; ++y) {
			for (int x = 0; x < w; ++x) {
				if (m[y][x] != '.' && !solved[y][x]) {
					if (!solve(x, y, res)) {
						failed = true;
						break;
					}
				}
			}
			
			if (failed) {
				break;
			}
		}

		cout << "Case #" << testIndex + 1 << ": ";
		if (failed) {
			cout << "IMPOSSIBLE";
		} else {
			cout << res;
		}
		cout << endl;
	}

	return 0;
}
