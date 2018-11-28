#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
using namespace std;


int a[1000];
int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		printf("Case #%d:", cas);
		int N;
		scanf("%d", &N);
		for (int i = 0;i < N; ++i) {
			scanf("%d", a + i);
		}
		int ans = 0;
		for (int i = 0; i < N; ++i) {
			int left = 0;
			for (int j = 0; j < i; ++j)
				if (a[j] > a[i]) ++left;
			int right = 0;
			for (int j = i + 1; j < N; ++j) 
				if (a[j] > a[i]) ++right;
			ans += min(left, right);
		}
		printf(" %d\n", ans);
	}
	return 0;
}
