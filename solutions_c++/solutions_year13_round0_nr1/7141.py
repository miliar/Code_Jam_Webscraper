#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

inline void inp2(int *n) {
	register char c = 0;
	*n = 0;

	while (c < 33)
		c = getchar_unlocked();

	while (c > 33) {
		*n = *n * 10 + c - '0';
		c = getchar_unlocked();
	}
}

int _main() {

	int T, N;
	inp2(&T);
	N = 0;
	int zc, xc, tc, dc;
	//printf("%d",T);
	char res[][30] = { "X won\n", "O won\n", "Draw\n",
			"Game has not completed\n" };
	while (T-- > 0) {
		N++;
		char brd[16] = { ' ' };
		for (int i = 1; i <= 16; i++) {
			brd[i - 1] = getchar_unlocked();
			if (i % 4 == 0) {
				getchar_unlocked(); // read \n
			}

		}
		getchar_unlocked();
		bool w = false, df = false;
		;

		// CHECK HORI

		for (int i = 0; i < 16; i += 4) {
			zc = xc = tc = dc = 0;
			for (int j = i; j < i + 4; j++) {
				if (brd[j] == '.') {
					df = true;
					zc = xc = 30;
					break;
				} else if (brd[j] == 'X')
					xc++;
				else if (brd[j] == 'O')
					zc++;
				else if (brd[j] == 'T')
					tc++;
			}

			if (!(zc > 0 && xc > 0)) {

				if (zc == 4 || (zc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[1]);
					//printf(res[1]);
					w = true;
				} else if (xc == 4 || (xc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[0]);
					w = true;
				}
			}
		}

		// CHECK VER
		if (!w) {
			for (int i = 0; i <= 3; i++) {
				zc = xc = tc = dc = 0;
				for (int j = 0 + i; j < 16; j += 4) {

					if (brd[j] == '.') {
						zc = xc = 30;
						break;
					} else if (brd[j] == 'X')
						xc++;
					else if (brd[j] == 'O')
						zc++;
					else if (brd[j] == 'T')
						tc++;
				}

				if (!(zc > 0 && xc > 0)) {

					if (zc == 4 || (zc == 3 && tc == 1)) {
						printf("Case #%d: %s", N, res[1]);
						w = true;
						//printf(res[1]);
					} else if (xc == 4 || (xc == 3 && tc == 1)) {
						printf("Case #%d: %s", N, res[0]);
						w = true;
					}
				}
			}
		} else
			continue;
		if (!w) {
			zc = xc = tc = dc = 0;
			for (int j = 0; j < 16; j += 5) {

				if (brd[j] == 'X')
					xc++;
				else if (brd[j] == 'O')
					zc++;
				else if (brd[j] == 'T')
					tc++;
			}

			if (!(zc > 0 && xc > 0)) {

				if (zc == 4 || (zc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[1]);
					w = true;
					//printf(res[1]);
				} else if (xc == 4 || (xc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[0]);
					w = true;
				}
			}
		} else
			continue;

		if (!w) {
			zc = xc = tc = dc = 0;
			for (int j = 3; j < 13; j += 3) {

				if (brd[j] == 'X')
					xc++;
				else if (brd[j] == 'O')
					zc++;
				else if (brd[j] == 'T')
					tc++;
			}
			//cout << zc << xc << tc;
			if (!(zc > 0 && xc > 0)) {

				if (zc == 4 || (zc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[1]);
					w = true;
					//printf(res[1]);
				} else if (xc == 4 || (xc == 3 && tc == 1)) {
					printf("Case #%d: %s", N, res[0]);
					w = true;
				}
			}
		} else
			continue;

		if (!w) {
			if (df) {
				printf("Case #%d: %s", N, res[3]);
			} else {
				printf("Case #%d: %s", N, res[2]);
			}
		}

	}

	return 0;
}

int main() {
	return _main();
}
