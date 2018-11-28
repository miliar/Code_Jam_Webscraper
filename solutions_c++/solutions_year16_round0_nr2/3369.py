#include <bits/stdc++.h>
#define INF 99999999

using namespace std;

int n;
string str;
int memo[105][105];

int rec(int pos, int numFace) {
	if (memo[pos][numFace] != -1) return memo[pos][numFace];
	if (pos == str.size()) {
		if (numFace == pos) {
			return 0;
		} else {
			return INF;
		}
	}
	return memo[pos][numFace] = min(rec(pos + 1, numFace + ((str[pos] == '+') ? 1 : 0)), rec(pos + 1, (pos - numFace) + ((str[pos] == '+') ? 0 : 1)) + 1);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		memset(memo, -1, sizeof(memo));
		cin >> str;
		printf("Case #%d: %d\n", i + 1, rec(0, 0));
	}
}
