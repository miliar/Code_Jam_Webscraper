#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int a[4], b[4];
int tb[4][4];
int main () {
	int i, j, k, ca, T;

	freopen ("A-small-attempt0.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	scanf ("%d", &T);
	for (ca = 1; ca <= T; ++ca) {
		scanf ("%d", &k);
		for (i = 0; i < 4; ++i)
			for (j = 0; j < 4; ++j)
				scanf ("%d", &tb[i][j]);
		memcpy (a, tb[k-1], 4 * sizeof(int));

		scanf ("%d", &k);
		for (i = 0; i < 4; ++i)
			for (j = 0; j < 4; ++j)
				scanf ("%d", &tb[i][j]);
		memcpy (b, tb[k-1], 4 * sizeof(int));

		int cnt = 0, ans = -1;
		for (i = 0; i < 4; ++i)
			for (j = 0; j < 4; ++j) {
				if (a[i] == b[j]) ans = a[i], cnt ++;
			}

		printf ("Case #%d: ", ca);
		if (cnt == 1) printf ("%d\n", ans);
		else if (cnt > 1) printf ("Bad magician!\n");
		else printf ("Volunteer cheated!\n");
	}
	return 0;
}
