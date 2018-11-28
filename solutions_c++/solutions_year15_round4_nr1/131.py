#include <bits/stdc++.h>

using namespace std;

char data[128][128];
long n, m;

inline bool OK(const char x) {
	return x == '^' || x == 'v' || x == '<' || x == '>';
}

class e {};

long checkUp(const long i, const long j) {
	for(long x = i - 1; x >= 0; -- x) {
		if (OK(data[x][j])) return 0;
	}
	for(long x = i + 1; x < n; ++ x) {
		if (OK(data[x][j])) return 1;
	}
	for(long x = j - 1; x >= 0; -- x) {
		if (OK(data[i][x])) return 1;
	}
	for(long x = j + 1; x < m; ++ x) {
		if(OK(data[i][x])) return 1;
	}
	throw e();
}

long checkDown(const long i, const long j) {
	for(long x = i + 1; x < n; ++ x) {
		if (OK(data[x][j])) return 0;
	}
	for(long x = i - 1; x >= 0; -- x) {
		if (OK(data[x][j])) return 1;
	}
	for(long x = j - 1; x >= 0; -- x) {
		if (OK(data[i][x])) return 1;
	}
	for(long x = j + 1; x < m; ++ x) {
		if(OK(data[i][x])) return 1;
	}
	throw e();
}

long checkLeft(const long i, const long j) {
	for(long x = j - 1; x >= 0; -- x) {
		if (OK(data[i][x])) return 0;
	}
	for(long x = j + 1; x < m; ++ x) {
		if(OK(data[i][x])) return 1;
	}
	for(long x = i - 1; x >= 0; -- x) {
		if (OK(data[x][j])) return 1;
	}
	for(long x = i + 1; x < n; ++ x) {
		if (OK(data[x][j])) return 1;
	}
	throw e();
}

long checkRight(const long i, const long j) {
	for(long x = j + 1; x < m; ++ x) {
		if (OK(data[i][x])) return 0;
	}
	for(long x = j - 1; x >= 0; -- x) {
		if(OK(data[i][x])) return 1;
	}
	for(long x = i - 1; x >= 0; -- x) {
		if (OK(data[x][j])) return 1;
	}
	for(long x = i + 1; x < n; ++ x) {
		if (OK(data[x][j])) return 1;
	}
	throw e();
}

int main(void) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++ t) {
		cin >> n >> m;
		register long i, j;
		for(i = 0; i < n; ++ i) {
			cin >> data[i];
		}
		cout << "Case #" << t << ": ";
		try {
			long ans = 0;
			for(i = 0; i < n; ++ i) {
				for(j = 0; j < m; ++ j) {
					switch(data[i][j]) {
						case '^':
							ans += checkUp(i, j);
							break;
						case 'v':
							ans += checkDown(i, j);
							break;
						case '<':
							ans += checkLeft(i, j);
							break;
						case '>':
							ans += checkRight(i, j);
					}
				}
			}
			cout << ans << endl;
		} catch(e ex) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
