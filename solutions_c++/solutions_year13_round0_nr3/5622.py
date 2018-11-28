#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int a, b;

int isPalin (int n) {
	vector<int> a;
	while (n) {
		a.push_back(n % 10);
		n /= 10;
	}
	int sz = a.size();
	for (int i = 0; i < sz; i++) {
		if (a[i] != a[sz - i - 1])
			return false;
	}
	return true;
}

int fair (int n) {
	int sq = sqrt(n);
	if (sq * sq != n) return false;
	if (isPalin (sq) && isPalin(n))
		return true;
	return false;
}

int solve(int a, int b) {
	int ans = 0;
	for (int i = a; i <= b; i++) {
		if (fair(i))
			ans ++;
	}
	return ans;
}

int main() {
	int T , caseNo = 1;
	scanf("%d",&T);
	while (T--) {
		scanf ("%d%d" , &a , &b);
		int ans = solve(a , b);
		printf("Case #%d: %d\n" , caseNo ++ , ans);
	}
	return 0;
}
