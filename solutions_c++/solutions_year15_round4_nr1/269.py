#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N(111);
char a[N][N];
int main() {
	int tst;
	scanf("%d", &tst);
	for(int qq(1); qq <= tst; qq++) {
		int r, c;
		bool flag(true);
		int ans(0);
		scanf("%d%d", &r, &c);
		for(int i(0); i < r; i++) {
			scanf("%s", a[i]);
		}
		for(int i(0); i < r; i++) {
			for(int j(0); j < c; j++) {
				bool up(true);
				for(int k(i - 1); k >= 0; k--) {
					if(a[k][j] != '.') {
						up = false;
						break;
					}
				}
				bool down(true);
				for(int k(i + 1); k < r; k++) {
					if(a[k][j] != '.') {
						down = false;
						break;
					}
				}
				bool left(true);
				for(int k(j - 1); k >= 0; k--) {
					if(a[i][k] != '.') {
						left = false;
						break;
					}
				}
				bool right(true);
				for(int k(j + 1); k < c; k++) {
					if(a[i][k] != '.') {
						right = false;
						break;
					}
				}
				if(a[i][j] != '.' && up && down && right && left) {
					flag = false;
				}
				if(a[i][j] == '<' && left || a[i][j] == 'v' && down || a[i][j] == '>' && right || a[i][j] == '^' && up) {
					ans++;
				}
			}
		}

		printf("Case #%d: ", qq);
		if(flag) {
			printf("%d\n", ans);
		}else {
			printf("IMPOSSIBLE\n");
		}

	}
}
