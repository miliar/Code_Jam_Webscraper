#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
int a[10000];
int b[10000];
int n;
int main(){
    int tc;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    //freopen("B.in", "r", stdin);
    //freopen("B.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        printf("Case #%i: ", tt);        
		scanf("%i", &n);
		for(int i=0; i<n; ++i) {
			scanf("%i", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);

		int k = n;
		int ans = 0;
		for(int i=1; i<n; ++i) {
			for(int j=0; j<k; ++j) if (a[j] == b[i-1]) {
				ans += min(j, k - j - 1);
				for(int z=j; z<k; ++z) a[z] = a[z+1];
				k--;
				break;
			}
		}
		printf("%i\n", ans);
    }

    return 0;
}

