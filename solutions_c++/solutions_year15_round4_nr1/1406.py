#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>
#include <numeric>

using namespace std;

const int MAXN = 111;
const int DIRT[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

char s[MAXN][MAXN];

int direct(char c) {
	if (c == '>') {
		return 0;
	}
	if (c == '<') {
		return 1;
	}
	if (c == 'v') {
		return 2;
	}
	return 3;
}

bool valid[4];

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++task_index) {
		int r, c;
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; ++i) {
			scanf("%s", s[i]);
		}
		int ret = 0;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (s[i][j] != '.') {
					for (int d = 0; d < 4; ++d) {
						valid[d] = false;
						int x = i + DIRT[d][0], y = j + DIRT[d][1];
						while (0 <= x && x < r && 0 <= y && y < c) {
							if (s[x][y] != '.') {
								valid[d] = true;
								break;
							}
							x += DIRT[d][0];
							y += DIRT[d][1];
						}
					}
					int d = direct(s[i][j]);
					if (!valid[d]) {
						int cnt = 0;
						for (int _ = 0; _ < 4; ++_) {
							if (valid[_]) {
								++cnt;
							}
						}
						if (cnt > 0) {
							++ret;
						}
						else {
							ret = 0x80000000;
						}
					}
				}
			}
		}

		printf("Case #%d: ", task_index);
		if (ret < -1) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n", ret);
		}
	}
	return 0;
}

