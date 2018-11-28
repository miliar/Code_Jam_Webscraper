#include <iostream>
#include <stdio.h>
using namespace std;

int a1,a2;
int m1[4][4], m2[4][4];
		
void solve() {
	int i, j, ans, cnt = 0;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (m1[a1-1][i] == m2[a2-1][j]) {
				cnt++;
				ans = m1[a1-1][i];
			}
		}
	}
	switch (cnt) {
	case 0:
		printf ("Volunteer cheated!\n");
		break;	
	case 1:
		printf ("%d\n", ans);
		break;
	default:
		printf ("Bad magician!\n");
	}
}


int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &a1);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &m1[i][j]);
			}
		}
		
		scanf("%d", &a2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
			scanf("%d", &m2[i][j]);
		}
		
		printf("Case #%d: ", t);
		
		solve();
	}
	return 0;
}