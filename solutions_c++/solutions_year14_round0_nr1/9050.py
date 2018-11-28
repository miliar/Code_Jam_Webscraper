#include<cstdio>
#include<cstdlib>

FILE *file_output;

int t, a, b, c[20], d[20], e, ans;

int main() {
//	file_output = fopen("A-S.out", "w");
	scanf("%d", &t);
	for (int zzz = 1 ; zzz <= t ; zzz++) {
		ans = 0;
		scanf("%d", &a);
		for (int i = 1 ; i < 5 ; i++) {
			for (int j = 1 ; j < 5 ; j++) {
				scanf("%d", &e);
				c[e] = i;
			}
		}
		scanf("%d", &b);
		for (int i = 1 ; i < 5 ; i++) {
			for (int j = 1 ; j < 5 ; j++) {
				scanf("%d", &e);
				d[e] = i;
			}
		}
		for (int i = 1 ; i < 17 ; i++) {
			if (c[i] == a && d[i] == b) {
				if (!ans) ans = i;
				else ans = -1;
			}
		}
		fprintf(file_output, "Case #%d: ", zzz);
		if (ans > 0) fprintf(file_output, "%d\n", ans);
		else if (ans) fprintf(file_output, "Bad magician!\n");
		else fprintf(file_output, "Volunteer cheated!\n");
	}
	scanf("\n");
	return 0;
}
