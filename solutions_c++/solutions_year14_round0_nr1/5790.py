#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

using namespace std;

int T;
int a[17][2];

int main(void) {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		for(int i = 0; i < 17; i++) {
			a[i][0] = a[i][1] = 0;
		}
		int row;
		scanf("%d", &row);
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				int x;
				scanf("%d", &x);
				if(i == row) {
					a[x][0] = 1;
				}
			}
		}
		scanf("%d", &row);
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				int x;
				scanf("%d", &x);
				if(i == row) {
					a[x][1] = 1;
				}
			}
		}
		int cnt = 0;
		int v;
		for(int i = 1; i <= 16; i++) {
			if(a[i][0] == 1 && a[i][1] == 1) {
				cnt++;
				v = i;
			}
		}
		if(cnt == 0) {
			printf("Case #%d: Volunteer cheated!\n", t);
		}else if(cnt > 1) {
			printf("Case #%d: Bad magician!\n", t);
		}else {
			printf("Case #%d: %d\n", t, v);
		}
	}
	return 0;
}
