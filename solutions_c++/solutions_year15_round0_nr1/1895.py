#include <cstdio>
#define MAXS 1000
using namespace std;
int main() {
	int T, sum, ans, maxShy, num;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		scanf("%d", &maxShy);
		scanf("%1d", &sum);
		ans = 0;
		for (int nowShy = 1; nowShy <= maxShy; nowShy++) {
			scanf("%1d", &num);
			if (num == 0) {
				continue;
			}
			if (sum < nowShy) {
				ans += nowShy-sum;
				sum = nowShy;
			}
			sum += num;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

