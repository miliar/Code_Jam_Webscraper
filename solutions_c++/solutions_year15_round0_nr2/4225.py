#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int n, a[1010];
	for (int t = 0; t < T; t++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int tmp;
			scanf("%d", &a[i]);
		}
		int ans = 1000000000;
		for (int i = 1; i <= 1000; i++) {
			int tmp = i;
			for (int j = 0; j < n; j++) {
				tmp += a[j] / i - 1;
				if (a[j] % i != 0) tmp++;
			}
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n", t + 1, ans);

	}
}