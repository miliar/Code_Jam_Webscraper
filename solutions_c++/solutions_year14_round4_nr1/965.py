#include <cstdio>
#include <algorithm>

using namespace std;

int cases, casei, n, x, ans;
int s[100000];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i) {
			scanf("%d", s + i);
		}
		sort(s, s + n);
		ans = 0;
		for (int i = n - 1; i >= 0; --i) if (s[i] != -1) {
			++ans;
			for (int j = i - 1; j >= 0; --j) 
				if (s[j] != -1 && s[j] + s[i] <= x) {
					s[j] = -1;
					break;
				}
		}
		
		printf("Case #%d: %d\n", casei, ans);
	}
	
	return 0;
}
