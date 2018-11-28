#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<cstring>
#include<numeric>
#include<limits.h>
#include<unordered_map>
#include<unordered_set>
#define long long long
using namespace std;


void solve() {
	int n;
	scanf("%d", &n);
	if (n == 0) {
		printf("INSOMNIA\n");
		return;
	}
	int a = n;
	set<int> was;
	while (was.size() < 10) {
		int cur = n;
		while (cur > 0) {
			was.insert(cur % 10);
			cur /= 10;
		}
		n += a;
	}
	printf("%d\n", n - a);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("codeJamAlarge.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	int id = 1;
	while (t--) {
		printf("Case #%d: ", id);
		solve();
		id++;
	}

	return 0;
}