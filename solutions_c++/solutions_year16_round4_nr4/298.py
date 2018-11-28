#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
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

#define maxN 26

int ans, N, cv, arr[maxN];
char mat[maxN][maxN];

bool valid(int p, int mask) {
	if (p == N) return true;
	bool ret = false;
	FOR(i, 0, N) {
		if (mat[arr[p]][i]=='1'&&mask & 1 << i) {
			ret = true;
			if (!valid(p + 1, mask ^ 1 << i)) return false;
		}
	}
	return ret;
}

void solve(int r, int c) {
	if (c == N) {
		solve(r + 1, 0);
		return;
	}
	if (r == N) {
		FOR(i, 0, N) arr[i] = i;
		bool v = true;
		do {
			if (!valid(0, (1 << N) - 1)) v = false;
		} while (next_permutation(arr, arr + N));
		if(v) ans = min(ans, cv);
		return;
	}
	if (mat[r][c]=='0') {
		cv++;
		mat[r][c] = '1';
		solve(r, c + 1);
		mat[r][c] = '0';
		cv--;
	}
	solve(r, c + 1);
}

int main() {
	int T, caso = 1;
	cin >> T;
	while (T--) {
		cin >> N;
		FOR(i, 0, N) cin >> mat[i];
		ans = INF;
		cv = 0;
		solve(0, 0);
		cout << "Case #" << caso++ << ": " << ans << endl;
	}
	return 0;
}
