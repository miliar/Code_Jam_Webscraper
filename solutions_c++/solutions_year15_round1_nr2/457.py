#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>
#define LL long long

using namespace std;

LL n, B, m[100005];

LL cal(LL v){
	LL ret = 0;
	for (LL i = 0; i < B; i++){
		ret += v / m[i] + 1;
	}
	return ret;
}

void solve(){
	scanf("%lld%lld", &B, &n);
	LL maxV = 0;
	for (int i = 0; i < B; i++){
		scanf("%lld", &m[i]);
		maxV = max(maxV, m[i]);
	}
	LL low = 0, high = n * maxV, c1, c, mid;
	while (high >= low){
		mid = (low + high) / 2;
		c = cal(mid), c1 = cal(mid - 1);
		//printf("mid = %lld c = %lld c1 = %lld\n", mid, c, c1);
		if (n <= c && c1 < n) break;
		else if (c < n) low = mid + 1;
		else high = mid - 1;
	}
	LL j = n - c1;
	for (LL i = 0; i < B; i++){
		if (mid % m[i] == 0){
			j--;
			if (j == 0){
				printf("%lld\n", i + 1);
				break;
			}
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
