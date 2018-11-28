#include <bits/stdc++.h>

using namespace std;

int arr[10005];

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
    int t, cases = 1;
    
    scanf("%d", &t);
    while (t--) {
		int ans, mx = 0, n, i, j;
		
		scanf("%d",&n);
		for (i = 1; i <= n; i++) {
			scanf("%d", &arr[i]);
			mx = max(mx, arr[i]);
		}
		ans = mx;
		for (i = 1; i <= mx; i++) {
			int now = 0, maxx = 0;
			for (j = 1; j <= n; j++) {
				if (arr[j] > i) {
					now += (arr[j]/i)+((arr[j]%i == 0)?0:1)-1;
					maxx = max(maxx, i);
				} else maxx = max(maxx, arr[j]);
			}
			now += maxx;
			if (now < ans) ans = now;
		}
		printf("Case #%d: %d\n", cases++, ans);
    }
    return 0;
}
