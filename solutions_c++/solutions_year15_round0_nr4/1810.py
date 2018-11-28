#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>

using namespace std;

#define INF 1000000007
#define W "RICHARD"
#define L "GABRIEL"

string solve() {
	int X, R, C;
	cin >> X >> R >> C;
	if (R * C % X) return W;
	if (max(R, C) < X) return W;
	if (min(R, C) < (X + 1) / 2) return W;
	if (3 < X && min(R, C) == X - 2 && X % 2 == 0) return W;
	return L;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << solve() << '\n';
	}
	
	return 0;
}

