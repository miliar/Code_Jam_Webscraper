#include <cstdio>
using namespace std;

int main() {
	int tc, cn = 0;
	int n, A[4][4];
	for (scanf("%d", &tc); tc--; ) {
		int cnt[20] = {0};
		for (int k=0; k<2; ++k) {
			scanf("%d", &n);
			for (int i=0; i<4; ++i) for (int j=0; j<4; ++j) scanf("%d", A[i]+j);
			for (int i=0; i<4; ++i) ++cnt[A[n-1][i]];
		}
		int cc = 0, res = -1;
		for (int i=1; i<=16; ++i) if (cnt[i] == 2) ++cc, res = i;
		printf("Case #%d: ", ++cn);
		if (cc > 1) puts("Bad magician!");
		else if (cc == 0) puts("Volunteer cheated!");
		else printf("%d\n", res);
	}
	return 0;
}
