#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int cf(const pair<int, int>& a, const pair<int, int>& b) {
	return a.first > b.first;
}

void execute(int tc) {
	int n;
	pair<int, int> P[26];
	scanf("%d", &n);
	int sum = 0;
	for (int i=0; i<n; i++) {
		scanf("%d", &P[i].first);
		sum += P[i].first;
		P[i].second = i;
	}
	// for (int i=0; i<n; i++) {
	// 	printf("%d %c\n", P[i].first, P[i].second + 'A');
	// }
	string ans = "";
	int counter = 0;
	while (sum > 0) {
		sort(P, P+n, cf);
		counter ++;
		P[0].first--;
		sum--;
		// printf("%c %d %d\n", (char) (P[0].second + 'A'), sum, n);
		ans += (char) (P[0].second + 'A');
		if (sum != 0 && (counter % 2 == 0 || (sum == 2 && n == 3) )) {
			ans += " ";
			counter = 0;
		}
	}
	printf("Case #%d: %s\n", tc, ans.c_str());
}

int main() {
	int T;
	scanf("%d\n", &T);
	for (int i=1; i<=T; i++) {
		execute(i);
	}
	return 0;
}