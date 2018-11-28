#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const lint inf = ((lint)0x7fffffff) * ((lint)0x7fffffff);
const int Size = 1000 * 1000 + 1;
char buffer[Size];

const int Plus = 0;
const int Minus = 1;

const int size = 1000;
lint dp[size][2];

void init() {
}

void clear(int i) {
	For(i, 0, size) {
		For(j, 0, 2) {
			dp[i][j] = inf;
		}
	}
}

int solution(int nTest) {
	scanf("%s", buffer);
	string s = buffer;
	dp[0][Plus] = (s[0] == '+') ? 0 : 1;
	dp[0][Minus] = 1 - dp[0][Plus];

	For (i, 1, sz(s)) {
		if (s[i] == '+') {
			dp[i][Minus] = min(1 + dp[i-1][Plus], 2 + dp[i-1][Minus]);
			dp[i][Plus] = min(dp[i-1][Plus], 1 + dp[i-1][Minus]);
		} else {
			dp[i][Plus] = min(1 + dp[i-1][Minus], 2 + dp[i-1][Plus]);
			dp[i][Minus] = min(dp[i-1][Minus], 1 + dp[i-1][Plus]);
		}
	}
	printf("%lld\n", dp[sz(s) - 1][Plus]);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
