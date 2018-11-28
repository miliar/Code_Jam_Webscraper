#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

long long n, m;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; ++t) {
        cin >> n >> m;
        long long l = 1, r = (1 << n), mid;
    	while (l < r) {
   	    	mid = (l + r + 1) / 2;
        	long long ans = 0;
        	long long u = (1 << n) - mid;
        	for (long long j = 1; j <= n; ++j) {
            	if (u == 0) ans = ans * 2 + 1;
            	else {
                	ans = ans * 2;
                	u = (u - 1) / 2;
            	}
        	}
        	if (ans + 1 <= m) l = mid;
        	else r = mid - 1;
    	}
    	long long ans2 = l - 1;
    	l = 1 ,r = (1 << n);
    	while (l < r) {
        	mid = (l + r + 1) / 2;
        	long long ans = 0;
        	long long u = mid - 1;
        	for (long long j = 1; j <= n; ++j) {
            	if (u == 0) ans = ans * 2;
            	else {
                	ans = ans * 2 + 1;
                	u = (u - 1) / 2;
            	}
        	}
        	if (ans + 1 <= m) l = mid;
        	else r = mid - 1;
    	}
    	long long ans1 = l - 1;
        cout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}
