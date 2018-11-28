#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int R, C;
vector <string> B;

bool possible() {
	for (int r=0; r<R; r++) {
		int first = -1;
		int last = -1;
		for (int c=0; c<C; c++)
			if (B[r][c] != '.') {
				if (first == -1) first = c;
				last = c;
		}
		if (first != -1 && first == last) {
			int cnt = 0;
			for (int r1=0; r1<R; r1++)
				if (B[r1][first] != '.')
					cnt++;
			if (cnt == 1)
				return false;
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> R >> C;
		B.resize(R);
		for (int r=0; r<R; r++)
			cin >> B[r];

		cout << "Case #" << t << ": ";
		if (!possible()) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			int ans = 0;
			for (int r=0; r<R; r++) {
				int c = 0;
				while (c < C && B[r][c] == '.') c++;
				if (c < C && B[r][c] == '<') ans++;
				c = C-1;
				while (c > 0 && B[r][c] == '.') c--;
				if (c >= 0 && B[r][c] == '>') ans++;
			}
			for (int c=0; c<C; c++) {
				int r = 0;
				while (r < R && B[r][c] == '.') r++;
				if (r < R && B[r][c] == '^') ans++;
				r = R-1;
				while (r > 0 && B[r][c] == '.') r--;
				if (r >= 0 && B[r][c] == 'v') ans++;
			}
			cout << ans << endl;
		}
	}
}
