#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

long long a, b, k;

void read() {
    scanf("%lld%lld%lld", &a, &b, &k);
}

void solve() {
	int ans = 0;
	for(int i = 0; i < a; i++){
		for( int j = 0; j < b; j++){
			if((long long)(i&j) < k){
				ans++;
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
