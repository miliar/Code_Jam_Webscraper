#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

typedef long long int64;
const int inf = (int)1.05e9;


int main()
{
	int test_case;

	scanf("%d", &test_case);

	for(int case_num = 1; case_num <= test_case; ++case_num) {

		int r, c;
		vector<vector<char> > field;

		scanf("%d%d", &r, &c);
		field.resize(r);
		for(int i = 0; i < r; ++i) {
			field[i].resize(c);
			char buf[128];
			scanf("%s", buf);
			for(int j = 0; j < c; ++j)
				field[i][j] = buf[j];
		}

		int ans = 0;
		bool impossible = false;

		for(int sx = 0; sx < r; sx++) {
			for(int sy = 0; sy < c; ++sy) {

				if(field[sx][sy] == '.')
					continue;

				const char dircs[] = {'^', '>', 'v', '<'};
				const int dxs[] = {-1, 0, 1, 0};
				const int dys[] = {0, 1, 0, -1};
				bool oks[] = {false, false, false, false};

				for(int dir_idx = 0; dir_idx < 4; ++dir_idx) {

					const int dx = dxs[dir_idx];
					const int dy = dys[dir_idx];

					int x = sx + dx;
					int y = sy + dy;

					while(0 <= x && x < r && 0 <= y && y < c) {

						if(field[x][y] != '.') {
							oks[dir_idx] = true;
						}

						x += dx;
						y += dy;
					}
				}

				bool any_ok = false;
				int dir = -1;

				for(int i = 0; i < 4; ++i) {
					if(oks[i])
						any_ok = true;
				}

				for(int i = 0; i < 4; ++i) {
					if(dircs[i] == field[sx][sy])
						dir = i;
				}

				if(!any_ok) {
					impossible = true;
				} else {
					if(dir == -1) {
						fprintf(stderr, "Something wrong...\n");
						return -1;
					}
					if(!oks[dir])
						ans += 1;
				}

			}
		}

		if(impossible)
			printf("Case #%d: IMPOSSIBLE\n", case_num);
		else
			printf("Case #%d: %d\n", case_num, ans);
	}

	return 0;
}
