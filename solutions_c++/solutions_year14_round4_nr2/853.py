#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;


int a[99999], N;


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int testCaseNum;
	scanf("%d", &testCaseNum);
	for (int testCase = 1; testCase <= testCaseNum; ++testCase) {
		scanf("%d", &N);
		for (int i = 1; i <= N; ++i) scanf("%d", &a[i]);
		int ans = 0;
		int l = 1, r = N;
		while (l < r) {
			int p = -1;
			for (int i = l; i <= r; ++i)
				if (p == -1 || a[i] < a[p])
					p = i;
			if (p - l < r - p) {
				int x = a[p];
				for (int i = p; i > l; --i) a[i] = a[i - 1], ++ans;
				a[l] = x;
				l++;
			} else {
				int x = a[p];
				for (int i = p; i < r; ++i) a[i] = a[i + 1], ++ans;
				a[r] = x;
				r--;
			}
		}
		printf("Case #%d: %d\n", testCase, ans);
	}
	
	return 0;
}