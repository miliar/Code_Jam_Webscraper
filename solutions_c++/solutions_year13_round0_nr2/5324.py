#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#define DEB  0
#define EPS  1e-10
#define M_PI 3.14159265358979323846

using namespace std;

typedef complex<double> point;
typedef vector<bool> boolary;
typedef vector<int> intary;
typedef vector<string> strary;
typedef vector<intary> graph;
typedef vector<boolary> bgraph;

string solve() {
	int N, M;
	cin >> N >> M;
	int tbl[N][M];
	bool ok[N][M];
	for (int i = 0 ; i < N; i++) {
		for (int j = 0 ; j< M ; j++) {
			cin >> tbl[i][j];
			ok[i][j] = false;
		}
	}
	if (N == 1 or M == 1) return "YES";

	int num = -1, prenum = -1;
	do {
		prenum = num;
		num = 0;
		//cout << "p1" << endl;
		for (int i = 0 ; i < N; i++) {
			int maxval = -1;
			for (int j = 0 ; j< M ; j++) {
				if (not ok[i][j]) {
					maxval = max(maxval, tbl[i][j]);
				}
			}
			for (int j = 0 ; j< M ; j++) {
				if (ok[i][j]) {
					if (tbl[i][j] > maxval) {
						goto NEXT;
					}
				}
				else if(tbl[i][j] != maxval) {
					goto NEXT;
				}
			}
			//cout << i << endl;
			for (int j = 0 ; j< M ; j++) {
				ok[i][j] = true;
			}
		  NEXT:;
		}

		//cout << "p2" << endl;
		for (int i = 0 ; i < M; i++) {
			int maxval = -1;
			for (int j = 0 ; j< N ; j++) {
				if (not ok[j][i]) {
					maxval = max(maxval, tbl[j][i]);
				}
			}
			for (int j = 0 ; j< N ; j++) {
				if (ok[j][i]) {
					if (tbl[j][i] > maxval) {
						goto NEXT2;
					}
				}
				else if(tbl[j][i] != maxval) {
					goto NEXT2;
				}
			}
			//cout << i << endl;
			for (int j = 0 ; j< N ; j++) {
				ok[j][i] = true;
			}
		  NEXT2:;
		}

		for (int i = 0; i < N ; i++) {
			for (int j = 0; j < M ; j++) {
				if (ok[i][j])num++;
			}
		}
		if (num == N*M) {
			return "YES";
		}
	} while (num > prenum);
	return "NO";
}

int main() {
	int T;
	cin >> T;
	for (int tc=1; tc <= T; tc++) {
		cout << "Case #" << tc << ": " << solve() << endl;
	}
}
