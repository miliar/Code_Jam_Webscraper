#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
using namespace std;

int a[10004];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		int n;
		scanf("%d", &n);
		int ans = 0, su;
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]), ans = max(ans, a[i]);
		su = ans;

		for (int i = 1; i <= su; i++) {
			int ne = 0;
			for (int j = 0; j < n; j++) {
				int v = a[j] / i - 1;
				if (a[j] % i)
					v++;
				ne += v;
			}
			ans = min(ans, ne + i);
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	
	return 0;
}