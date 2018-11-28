#include <cstdio>
#include <algorithm>
#define MAX 1010
using namespace std;

int maxArr(int v[], int len) {
	int m = -1;
	for(int i = 0; i < len; i++) {
		m = max(m, v[i]);
	}
	return m;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);
		int v[MAX];
		for(int j = 0; j < n; j++) {
			scanf("%d", &v[j]);
		}
		int ans = maxArr(v, n), part = 2;
		while(part < ans) {
			int sum = 0;
			for(int j = 0; j < n; j++) {
				sum += (v[j] - 1) / part;
			}
			ans = min(ans, sum + part);
			part++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}