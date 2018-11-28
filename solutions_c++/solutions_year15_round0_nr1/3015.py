#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

const int N = 1005;
int a[N];
char s[N];
int n;
bool ok(int mid){
	int now = mid + s[0];
	for (int i = 1; i <= n; i++){
		if (now >= i)
			now += s[i];
		else return false;
	}
	return true;
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T, Cas = 1; scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", Cas++);
		scanf("%d %s", &n, s);
		for (int i = 0; i <= n; i++)s[i] -= '0';
		int l = 0, r = 10000000, ans = r;
		while (l <= r){
			int mid = (l + r) >> 1;
			if (ok(mid)){
				ans = mid;
				r = mid - 1;
			}
			else l = mid + 1;
		}
		printf("%d\n", ans);
	}
	return 0;
}
