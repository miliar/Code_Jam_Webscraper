#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;


int a[99999], v[99999], N, M;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int testCaseNum;
	scanf("%d", &testCaseNum);
	for (int testCase = 1; testCase <= testCaseNum; ++testCase) {
		scanf("%d%d", &N, &M);
		for (int i = 1; i <= N; ++i) scanf("%d", &a[i]);
		sort(a + 1, a + N + 1);
		reverse(a + 1, a + N + 1);
		memset(v, 0, sizeof(v));
		int ans = 0;
		for (int i = 1; i <= N; ++i) {
			if (v[i]) continue;
			int j = i + 1;
			while (j <= N) {
				if (!v[j] && a[i] + a[j] <= M) break;
				++j;
			}
			if (j > N) continue;
			v[i] = v[j] = 1;
			++ans;
		}
		for (int i = 1; i <= N; ++i) ans += (v[i] == 0);
		printf("Case #%d: %d\n", testCase, ans);
	}
	
	return 0;
}