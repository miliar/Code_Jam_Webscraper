#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int a, b;

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
