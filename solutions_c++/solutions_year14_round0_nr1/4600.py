#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int r1, r2;
int grid1[4][4], grid2[4][4];

void input() {
	scanf("%d", &r1); -- r1;
	for(int i = 0;i < 4;i ++) for(int j = 0;j < 4;j ++) scanf("%d", &grid1[i][j]);

	scanf("%d", &r2); -- r2;
	for(int i = 0;i < 4;i ++) for(int j = 0;j < 4;j ++) scanf("%d", &grid2[i][j]);
}

void output() {
	int cnt = 0, id;
	for(int i = 0;i < 4;i ++) for(int j = 0;j < 4;j ++) if(grid1[r1][i] == grid2[r2][j]) {
		++ cnt;
		id = grid1[r1][i];
	}

	if(cnt == 1) printf("%d\n", id);
	if(cnt > 1) printf("Bad magician!\n");
	if(cnt < 1) printf("Volunteer cheated!\n");
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		output();
	}
	return 0;
}