#include <cstdio>
#define FOR(i,n) for (int i = 0; i < n; i++)

int d1[5][5], d2[5][5];

void test() {
	int r1,r2;
	scanf("%d", &r1);
	FOR(i,4) FOR(j,4) scanf("%d", &d1[i][j]);
	scanf("%d", &r2);
	FOR(i,4) FOR(j,4) scanf("%d", &d2[i][j]);
	r1--; r2--;
	int who=0, cnt=0;
	FOR(i,4) FOR(j,4) if (d1[r1][i] == d2[r2][j]) {
		cnt++;
		who = d1[r1][i];
	}
	if (cnt == 1) printf("%d\n", who);
	else if (cnt > 1) printf("Bad magician!\n");
	else printf("Volunteer cheated!\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		test();
	}
	return 0;
}
