#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

char invert(char c) {
	if (c == '-') return '+';
	return '-';
}

int main() {
	int T, caso=1, K;
	cin >> T;
	string S;
	while (T--) {
		cin >> S >> K;
		int ans = 0;
		FOR(i, 0, S.length()) {
			if (S[i] == '-') {
				if (i + K <= S.length()) {
					FOR(j, i, i + K) {
						S[j] = invert(S[j]);
					}
					ans++;
				}
				else ans = INF;
			}
		}
		cout << "Case #" << caso++ << ": ";
		if (ans >= INF) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
