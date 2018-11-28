#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int a[22][22], b[22], ans, r1, r2, t;

int main() {
	//freopen("input.txt", "r", stdin);
	
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		memset(b, 0, sizeof(b));
		
		scanf("%d", &r1);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &a[i][j]);
				if (i == r1) b[a[i][j]]++;
			}
		
		scanf("%d", &r2);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &a[i][j]);
				if (i == r2) b[a[i][j]]++;
			}
		
		int cnt = 0;
		for (int i = 1; i <= 16; i++) if(b[i] == 2) ans = i, cnt++;
		if (cnt == 1) {
			printf("Case #%d: %d\n", tc, ans);
		} else if(cnt > 1) {
			printf("Case #%d: Bad magician!\n", tc);
		} else {
			printf("Case #%d: Volunteer cheated!\n", tc);
		}
	}
	
	return 0;
}