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
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxSize 101
#define up 0
#define right 1
#define down 2
#define left 3

struct Piece {
	int p, dir;
};

char mat[maxSize][maxSize];
int dirs[4][2] = { {-1,0}, {0,1}, {1,0}, {0,-1}};
Piece pos[4][maxSize];

int getDir(char t) {
	switch (t) {
	case '^':
		return up;
		break;
	case '>':
		return right;
		break;
	case 'v':
		return down;
		break;
	case '<':
		return left;
		break;
	}
	return -1;
}

int main() {
	int T, caso=1, R, C;
	cin >> T;
	while (T--) {
		cin >> R >> C;
		FOR(i, 0, R) {
			cin >> mat[i];
		}
		//top
		FOR(i, 0, C) {
			int r = 0;
			while (r < R&&mat[r][i]=='.') {
				r++;
			}
			pos[up][i].p = r;
			pos[up][i].dir = getDir(mat[r][i]);
			r = R - 1;
			while (r >=0 &&mat[r][i] == '.') {
				r--;
			}
			pos[down][i].p = r;
			pos[down][i].dir = getDir(mat[r][i]);
		}
		FOR(i, 0, R) {
			int c = 0;
			while (c < C&&mat[i][c] == '.') {
				c++;
			}
			pos[left][i].p = c;
			pos[left][i].dir = getDir(mat[i][c]);
			c = C - 1;
			while (c >= 0 && mat[i][c] == '.') {
				c--;
			}
			pos[right][i].p = c;
			pos[right][i].dir = getDir(mat[i][c]);
		}
		int ans = 0;
		bool possible = true;
		FOR(i, 0, R) {
			FOR(j, 0, C) {
				if (mat[i][j] != '.') {
					int d=getDir(mat[i][j]);
					int p1 = (d & 1) ? i : j;
					int p2 = (d & 1) ? j : i;
					if (pos[d][p1].p==p2) {
						bool found = false;
						FOR(k, 0, 4) {
							if (k == d) continue;
							int pp2 = (k & 1) ? p1 : p2;
							int pp1 = (k & 1) ? p2 : p1;
							if (d & 1) swap(pp2, pp1);
							if (pos[k][pp1].p != pp2) found = true;
						}
						if (!found) possible = false;
						ans++;
					}
				}
			}
		}
		cout << "Case #" << caso++ << ": ";

		if (possible) cout << ans;
		else {
			//cout <<R<<" "<<C<< endl;
			FOR(i, 0, R) {
				//cout << mat[i] << endl;
			}
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
