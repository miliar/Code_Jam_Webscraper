#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int A[5][5], B[5][5];

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		int a, b;
		scanf("%d", &a);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &A[i][j]);
		scanf("%d", &b);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &B[i][j]);
		int cnt = 0, opt = -1;
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				if (A[a][i] == B[b][j]) {
					cnt++; opt = A[a][i];
				}

		printf("Case #%d: ", t);
		if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt > 1) puts("Bad magician!");
		else printf("%d\n", opt);
	}

	return 0;
}
