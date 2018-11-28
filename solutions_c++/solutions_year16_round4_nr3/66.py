#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int dir[999][999];
int a[999], go[999];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int r, c;
		scanf("%d%d", &r, &c);
		for(int i(0); i < 2 * (r + c); i++) {
			scanf("%d", &a[i]);
		}
		bool ans = false;
		printf("Case #%d:\n", qq);
		for(int msk(0); msk < (1 << (r * c)); msk++) {
			int x(msk);
			for(int i(0); i < r; i++) {
				for(int j(0); j < c; j++) {
					dir[i][j] = x % 2;
					x /= 2;
				}
			}
			for(int i(0); i < 2 * (r + c); i++) {
				int x, y, dx, dy, dest;
				if(i >= 0 && i < c) {
					x = -1; y = i;
					dx = 1; dy = 0;
				}else if(i < c + r) {
					x = i - c; y = c;
					dx = 0; dy = -1;
				}else if(i < c + r + c) {
					x = r; y = c - 1 - (i - c - r);
					dx = -1; dy = 0;
				}else {
					x = r - 1 - (i - c - r - c); y = -1;
					dx = 0; dy = 1;
				}
				for(;;) {
					if(dir[x + dx][y + dy] == 0) {
						x += dx; y += dy;
						swap(dx, dy);
					}else {
						x += dx; y += dy;
						swap(dx, dy);
						dx = -dx; dy = -dy;
					}
					if(x < 0 || x >= r || y < 0 || y >= c) {
						go[i] = x < 0 ? y : y == c ? c + x : x == r ? r + c + (c - y - 1) : r + c + c + (r - x - 1);
						break;
					}
				}
			}
			/*for(int i(0); i < 2 * (r + c); i++) {
				printf("%d: go[%d] = %d\n", msk, i, go[i]);
			}*/
			bool flag(true);
			for(int i(0); i < 2 * (r + c); i++) {
				if(go[a[i] - 1] != a[i ^ 1] - 1) {
					flag = false;
					break;
				}
			}
			if(flag) {
				int x(msk);
				ans = true;
				for(int i(0); i < r; i++) {
					for(int j(0); j < c; j++) {
						if(x % 2 == 0) {
							printf("\\");
						}else {
							printf("/");
						}
						x /= 2;
					}
					printf("\n");
				}
				break;
			}
		}
		if(ans) {
		}else {
			printf("IMPOSSIBLE\n");
		}
	}
}
