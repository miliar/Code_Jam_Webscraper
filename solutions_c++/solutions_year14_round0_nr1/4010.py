#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int t, cases, r, v, mark[20], ans;

void process() {
	scanf("%d", &r);
	for (int i = 1; i <= 4; ++i) {
		for (int j = 1; j <= 4; j++) {
			scanf("%d", &v);
			if (i == r) {
				mark[v]++;
				if (mark[v] == 2) {
					if (ans == 0) {
						ans = v;
					} else {
						ans = -1;
					}
				}
			}
		}
	}
}

int main() {
	scanf("%d", &t);
	cases = 1;
	while(t--) {
		
		memset(mark, 0, sizeof(mark));
		ans = 0;
		process();
		process();
		printf("Case #%d: ", cases++);
		if (ans == 0) {
			printf("Volunteer cheated!\n");
		} else if (ans == -1) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n", ans);
		}
		
	}
	
	return 0;
}
