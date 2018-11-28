#include <stdio.h>
#include <math.h>

int main() {
	int t;
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for(int k = 1; k <= t; k++) {
		int n, m;
		scanf("%d%d", &n, &m);
		int a[105][105], ans = 0;
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= m; j++) {
		    	scanf("%d", &a[i][j]);
		    }
		}
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= m; j++) {
		    	int flag = 0;
	    		for(int s = 1; s <= n; s++) if(a[s][j] > a[i][j]) flag = 1;
				if(flag == 1) for(int s = 1; s <= m; s++) if(a[i][s] > a[i][j]) flag = 2;
				if(flag == 2) {
					ans = 1;
					break;
				}	    		
		    }
		}
		if(ans == 1) printf("Case #%d: NO\n", k);
		else printf("Case #%d: YES\n", k);		
	}
}