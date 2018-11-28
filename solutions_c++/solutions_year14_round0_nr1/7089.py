#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

int T;
bool hashn[128];
int n;

int main() {
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		printf("Case #%d: ", casen);
		
		memset(hashn, 0, sizeof hashn);
		scanf("%d", &n);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				int tmp;
				scanf("%d", &tmp);
				if (i == n) hashn[tmp] = true;
			}

		int ans = 0, cnt = 0;

		scanf("%d", &n);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				int tmp;
				scanf("%d", &tmp);
				if (i == n && hashn[tmp]) {
					ans = tmp;
					cnt++;
				}
			}
		if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt == 1) printf("%d\n", ans);
		else puts("Bad magician!");
	}

	return 0;
}
