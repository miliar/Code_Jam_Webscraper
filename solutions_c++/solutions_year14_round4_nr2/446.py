#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int inf = 2147483647;
const int maxn = 1000 + 10;
int n, a[maxn];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int TextN;
	scanf("%d", &TextN);
	for (int TT = 1; TT <= TextN; TT++) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d", a + i);
		}
		int left = 1, right = n, ans = 0;
		for (int i = 1; i <= n-1; i++) {
			int mina = inf, k = 0;
			for (int j = left; j <= right; j++) {
				if (a[j] < mina) {
					mina = a[j];
					k = j; 
				}
			}	
			if (k - left < right - k) {
				for (int i = k; i > left; i--) swap(a[i], a[i-1]);
				ans += k - left;
				left++;
			} else {
				for (int i = k; i < right; i++) swap(a[i], a[i+1]);
				ans += right - k;
				right--;
			}
		}
		printf("Case #%d: %d\n", TT, ans);
	}
	return 0;
}