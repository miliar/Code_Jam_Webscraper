#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
int main() {
	//freopen("B-small-attempt0.in","r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++) {
		int A, B, K;
		cin >> A >> B >> K;
		int ans = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				if ((i & j) < K) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", cases, ans);
	}	
}
