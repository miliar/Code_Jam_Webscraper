#include <stdio.h>
#include <string.h>
#define ull unsigned long long
#define loop(i, j, n)  for(int (i) = (j); i < n; i++)
#define sd(x) scanf("%d", &x)
#define slld(x) scanf("%lld", &x)

using namespace std;

int main() {
	int t;
	sd(t);
	for(int k=1; k<=t; k++) {
		int m, n, a[4][4], b[4][4];
		sd(m);
		loop(i, 0, 4) {
			loop(j, 0, 4) sd(a[i][j]);
		}
		sd(n);
		loop(i, 0, 4) {
			loop(j, 0, 4) sd(b[i][j]);
		}
		int res, cnt = 0;
		loop(i, 0, 4) {
			loop(j, 0, 4) {
				if(a[m-1][i] == b[n-1][j]) {
				cnt++;
				res = a[m-1][i];
			}
			}
		}
		printf("Case #%d: ", k);
		if(cnt == 1) printf("%d\n", res);
		else printf("%s\n", cnt == 0 ? "Volunteer cheated!" : "Bad magician!");
	}
	return 0;
}
