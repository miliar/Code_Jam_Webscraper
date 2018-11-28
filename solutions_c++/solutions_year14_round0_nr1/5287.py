#include <cstdio>
#include <cstring>

int main()
{
	int T; scanf ("%d", &T);
	int r1, dump, a[4], b[4];
	for (int cc = 1; cc <= T; cc++) {
		scanf ("%d", &r1);
		for (int r = 1; r <= 4; r++) {
			if (r == r1) {
				for (int c = 0; c < 4; c++) scanf ("%d", a+c);
			} else {
				for (int c = 0; c < 4; c++) scanf ("%d", &dump);
			}
		}
		scanf ("%d", &r1);
		for (int r = 1; r <= 4; r++) {
			if (r == r1) {
				for (int c = 0; c < 4; c++) scanf ("%d", b+c);
			} else {
				for (int c = 0; c < 4; c++) scanf ("%d", &dump);
			}
		}

		int ret = 0, ans = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[i] == b[j]) {
					ret++;
					ans = a[i];
				}
		if (ret == 1) {
			printf ("Case #%d: %d\n", cc, ans);
		} else if (ret > 1) {
			printf ("Case #%d: Bad magician!\n", cc);
		} else if (ret == 0) {
			printf ("Case #%d: Volunteer cheated!\n", cc);
		}
	}
	return 0;
}
