#include <bits/stdc++.h>

using namespace std;

#define fillchar(a, s) memset((a), (s), sizeof(a))
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define all(v) (v).begin(), (v).end()
#define rep(it, v) for (auto it = (v).begin(); it != (v).end(); it++)
#define dbg(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<int, int> pii;
const int MAXN = 110;

pii operator + (const pii &a, const pii &b) {
	return pii(a.first + b.first, a.second + b.second);
}

pii operator += (pii &a, const pii &b) {
	return a = a + b;
}

char dirs[] = "^<>v";

pii get (char c) {
	if (c == '^') {
		return pii(-1, 0);
	} else if (c == '<') {
		return pii(0, -1);
	} else if (c == '>') {
		return pii(0, 1);
	} else if (c == 'v') {
		return pii(1, 0);
	} else {
		return pii(0, 0);
	}
}

int N, M;
char grid[MAXN][MAXN];

bool bounded (pii p) {
	return 1 <= p.first && p.first <= N && 1 <= p.second && p.second <= M;
}

bool out (int i, int j) {
	pii p = get(grid[i][j]);
	if (p == pii(0, 0)) {
		return false;
	}
	//see if it leads directly out
	pii cur(i, j);
	// cerr << "cur " << i << ' ' << j << endl;
	while (true) {
		//uh yea
		cur += p;
		// cerr << cur.first << ' ' << cur.second << endl;
		if (!bounded(cur)) {
			// cerr << "out " << i << ' ' << j << endl;
			return true;
		}
		if (grid[cur.first][cur.second] != '.') {
			return false;
		}
	}
}

void go() {
	cin >> N >> M;
	// cerr << "N = " << N << ", M = " << M << endl;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> grid[i][j];
		}
	}
	//k now let's just think: which lead directly out
	int numout = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			// cerr << "i = " << i << ", j = " << j << endl;
			if (out(i, j)) {
				numout++;
				bool fix = false;	//can you fix it
				//then try to see if it is possible to CHANGE it
				char orig = grid[i][j];
				for (int k = 0; k < 4; k++) {
					grid[i][j] = dirs[k];
					// cerr << "grid[" << i << "][" << j << "] = " << grid[i][j] << endl;
					if (!out(i, j)) {
						fix = true;
						break;
					}
				}
				if (!fix) {
					cout << "IMPOSSIBLE\n";
					return;
				}
				grid[i][j] = orig;
			}
		}
	}
	//determine whether it is possible
	cout << numout << '\n';
}

int main() {
	if (fopen("input.txt", "r")) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	ios::sync_with_stdio(false);
	int tt;
	cin >> tt;
	for (int i = 1; i <= tt; i++) {
		cout << "Case #" << i << ": ";
		go();
	}
}