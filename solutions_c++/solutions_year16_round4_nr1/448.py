#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#define lson i<<1
#define rson i<<1|1
#define LL long long
#define MAXN 100050
using namespace std;
char a[3][1 << 17];
void cal(char *s, char cc) {
	s[1] = cc;
	for (int i = 1; i <= (1 << 12); ++i) {
		if (s[i] == 'P') {
			s[lson] = 'P';
			s[rson] = 'R';
		}
		if (s[i] == 'R') {
			s[lson] = 'R';
			s[rson] = 'S';
		}
		if (s[i] == 'S') {
			s[lson] = 'P';
			s[rson] = 'S';
		}
	}

}
int c[200];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	cal(a[0], 'P');
	cal(a[1], 'R');
	cal(a[2], 'S');
	int tt, ri = 0;
	scanf("%d", &tt);
//	for(int i=0;i<3;++i){
//		for(int j=1;j<=8;++j)
//			printf("%c",a[i][j]);
//		puts("");
//	}
	while (tt--) {
		memset(c, 0, sizeof(c));
		int n, cnt[3];
		scanf("%d%d%d%d", &n, &cnt[0], &cnt[1], &cnt[2]);
		int w = (1 << n), flag = 0;
		printf("Case #%d: ", ++ri);
		for (int i = 0; i < 3; ++i) {
			int y[200];
			memset(y, 0, sizeof(y));
			for (int j = w; j < 2 * w; ++j) {
				y[a[i][j]]++;
			}
			if (y['R'] == cnt[0] && y['P'] == cnt[1] && y['S'] == cnt[2]) {
				flag = 1;
				for (int j = w; j < 2 * w; ++j) {
					printf("%c", a[i][j]);
				}
				puts("");
			}
		}
		if (flag == 0)
			puts("IMPOSSIBLE");
	}
	return 0;
}
