#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int maxn = 1000+10;
int n;
int a[maxn];
int mid;
int ans;
int l, r;

void work() {
	scanf("%d", &n);
	for (int i=0;i<n;i++) {
		scanf("%d", &a[i]);
	}
	ans = 0;
	l = 0;
	r = n-1;
	for (int i=0;i<n-1;i++) {
		mid = l;
		for (int j=l;j<=r;j++) {
			if (a[j] < a[mid]) mid = j;
		}
		if (mid - l < r - mid) {
			for (int j=mid;j>l;j--) {
				swap(a[j], a[j-1]);
				ans++;
			}
			l++;
		} else {
			for (int j=mid;j<r;j++) {
				swap(a[j], a[j+1]);
				ans++;
			}
			r--;
		}
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++cas);
		work();
	}
	return 0;
}