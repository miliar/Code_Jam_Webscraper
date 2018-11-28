#include"stdio.h"
#include"stdlib.h"
#include"math.h"
using namespace std;

int T, t, i, j, r, x, count, ans;
bool in[17];
int main() {
	freopen("1.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		count = 0;
		scanf("%d", &r);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d", &x);
				in[x] = (i == r);
			}
		}
		scanf("%d", &r);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d", &x);
				if (i == r && in[x]) {
					count++;
					ans = x;
				}
			}
		}
		printf("Case #%d: ", t);
		if (count == 0) printf("Volunteer cheated!\n");
		else if (count == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}
}
