#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n, d[1010];
int gao(int m){
	for (int i = 1; i <= m; ++i){
		int cnt = 0;
		for (int j = n - 1; j >= 0; --j){
			cnt += (d[j] - 1) / i;
			if (cnt + i > m) break;
		}
		if (cnt + i <= m) return true;
	}
	return false;
}
int gao(){
	int ans = 1000;
	int s = 1, t = 1000;
	while (s <= t){
		int m = (s + t) / 2;
		if (gao(m)){
			ans = m;
			t = m - 1;
		}else{
	 		s = m + 1;
		}
	}
	return ans;
}
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = 0, tt;
	for (scanf("%d ", &tt); t < tt; ++t){
		scanf("%d ", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d ", &d[i]);
		sort(d, d + n);
		int ans = gao();
		//for (int i = 0; i < n; ++i)
		//	printf("%d ", d[i]);
		printf("Case #%d: %d\n", t + 1, ans);
	}
} 
