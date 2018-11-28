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

#define maxN 12

int arr[maxN][1 << maxN];

bool solveBrute(int N, int P, int R, int S) {
	FOR(i, 0, P) arr[0][i] = 0;
	FOR(i, 0, R) arr[0][i + P] = 1;
	FOR(i, 0, S) arr[0][i + P + R] = 2;
	bool valid = false;
	do {
		bool tv = true;
		FOR(i, 0, N) {
			for (int j = 0; j < 1 << N - i; j += 2) {
				if (arr[i][j] == arr[i][j + 1]) {
					tv = false;
					break;
				}
				else if (arr[i][j] == 0 && arr[i][j + 1] == 1) arr[i + 1][j / 2] = 0;
				else if (arr[i][j] == 0 && arr[i][j + 1] == 2) arr[i + 1][j / 2] = 2;
				else if (arr[i][j] == 1 && arr[i][j + 1] == 0) arr[i + 1][j / 2] = 0;
				else if (arr[i][j] == 1 && arr[i][j + 1] == 2) arr[i + 1][j / 2] = 1;
				else if (arr[i][j] == 2 && arr[i][j + 1] == 0) arr[i + 1][j / 2] = 2;
				else if (arr[i][j] == 2 && arr[i][j + 1] == 1) arr[i + 1][j / 2] = 1;
			}
			if (!tv) break;
		}
		if (tv) {
			valid = true;
			break;
		}
	} while (next_permutation(arr[0], arr[0] + (1 << N)));
	return valid;
}

void solve(int st, int N, int P, int R, int S) {
	if (!N) {
		if (P) arr[0][st] = 0;
		else if (R) arr[0][st] = 1;
		else arr[0][st] = 2;
		return;
	}
	int np = P / 2, nr = R / 2, ns = S / 2;
	if (P & 1) np++;
	else if (R & 1) nr++;
	solve(st, N - 1, np, nr, ns);
	if (P & 1) {
		np--;
		if (R & 1) nr++;
		else ns++;
	}
	else {
		nr--;
		ns++;
	}
	solve(st + (1 << N - 1), N - 1, np, nr, ns);
}

int main() {
	int T, N, P, S, R, caso=1;
	cin >> T;
	while (T--) {
		cin >> N >> R >> P >> S;
		cout << "Case #" << caso++ << ": ";
		solveBrute;
		//bool valid = solveBrute(N, P, R, S);
		bool valid = abs(R - P) <= 1 && abs(R - S) <= 1 && abs(P - S) <= 1;
		if (valid) {
			solve(0, N, P, R, S);
			FOR(i, 0, 1 << N) {
				if (!arr[0][i]) cout << 'P';
				else if (arr[0][i] == 1) cout << 'R';
				else cout << 'S';
			}
			cout << endl;
		}
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}