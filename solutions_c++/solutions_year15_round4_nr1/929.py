#include <iostream>
#include <iomanip>
#include <vector>           
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>
#include <string>
#include <string.h>  // Include for memset!
#include <complex>
#include <random>
#define _USE_MATH_DEFINES
#include <math.h>

#define INF 2000000000              // 9
#define LLINF 9000000000000000000LL // 18
#define LDINF 1e200

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<bool> vb;
typedef long long ll;
typedef long double ld;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int R, C;
		cin >> R >> C;
		vector< vector<char> > board(C, vector<char>(R));
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				cin >> board[c][r];
			}
		}

		vector< vector<int> > status(C, vector<int>(R, 0));
		// =>
		bool item = false;
		for (int r = 0; r < R; ++r) {
			item = false;
			for (int c = 0; c < C; ++c) {
				switch (board[c][r]) {
				case '<':
					if (item)
						status[c][r] = max(status[c][r], 2);
					item = true;
					break;
				case '>':
				case 'v':
				case '^':
					if (item) status[c][r] = max(status[c][r], 1);
					item = true;
					break;
				}
			}
		}

		// <=
		item = false;
		for (int r = 0; r < R; ++r) {
			item = false;
			for (int c = C - 1; c >= 0; --c) {
				switch (board[c][r]) {
				case '>':
					if (item)
						status[c][r] = max(status[c][r], 2);
					item = true;
					break;
				case '<':
				case 'v':
				case '^':
					if (item) status[c][r] = max(status[c][r], 1);
					item = true;
					break;
				}
			}
		}

		// ^
		item = false;
		for (int c = C - 1; c >= 0; --c) {
			item = false;
			for (int r = 0; r < R; ++r) {
				switch (board[c][r]) {
				case '^':
					if (item)
						status[c][r] = max(status[c][r], 2);
					item = true;
					break;
				case '<':
				case 'v':
				case '>':
					if (item) status[c][r] = max(status[c][r], 1);
					item = true;
					break;
				}
			}
		}

		// v
		item = false;
		for (int c = C - 1; c >= 0; --c) {
			item = false;
			for (int r = R - 1; r >= 0; --r) {
				switch (board[c][r]) {
				case 'v':
					if (item)
						status[c][r] = max(status[c][r], 2);
					item = true;
					break;
				case '<':
				case '^':
				case '>':
					if (item) status[c][r] = max(status[c][r], 1);
					item = true;
					break;
				}
			}
		}

		int ans = 0;
		bool pos = true;
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				if (board[c][r] == '.') continue;
				if (status[c][r] == 0) pos = false;
				if (status[c][r] == 1) ans++;
			}
		}

		if (pos)
			cout << "Case #" << t << ": " << ans << endl;
		else cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}
    
    return 0;
}