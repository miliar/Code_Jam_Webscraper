#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
void PR(vi &v) { trav(x, v) cout << x << ' '; cout << endl; }

int R, C;
char at(int bits, int i, int j) {
	int row = (bits >> (i*C)) & ((1 << C) - 1);
	return row & (1 << j) ? '/' : '\\';
}

struct Pos {
	int x, y;
};
bool operator!=(Pos a, Pos b) { return a.x != b.x || a.y != b.y; }

enum { UP, DOWN, LEFT, RIGHT};
pair<Pos, int> step1(Pos pos, int dir) {
	if (dir == LEFT) pos.x--;
	if (dir == RIGHT) pos.x++;
	if (dir == UP) pos.y--;
	if (dir == DOWN) pos.y++;
	return {pos, dir};
}

pair<Pos, int> step(int bits, Pos pos, int dir) {
	char c = at(bits, pos.y, pos.x);
	if (c == '/') {
		if (dir == DOWN) return step1(pos, LEFT);
		if (dir == RIGHT) return step1(pos, UP);
		if (dir == UP) return step1(pos, RIGHT);
		if (dir == LEFT) return step1(pos, DOWN);
	}
	else if (c == '\\') {
		if (dir == DOWN) return step1(pos, RIGHT);
		if (dir == RIGHT) return step1(pos, DOWN);
		if (dir == UP) return step1(pos, LEFT);
		if (dir == LEFT) return step1(pos, UP);
	}
	assert(0);
}

Pos outpos(int bits, Pos pos, int dir) {
	while (pos.x >= 0 && pos.y >= 0 && pos.x < C && pos.y < R)
		tie(pos, dir) = step(bits, pos, dir);
	return pos;
}

Pos topos(int p) {
	p--;
	if (p < C) return Pos{p, -1};
	p -= C;
	if (p < R) return Pos{C, p};
	p -= R;
	if (p < C) return Pos{C-1-p, R};
	p -= C;
	if (p < R) return Pos{-1, R-1-p};
	assert(0);
}

bool works(vi& perm, int bits) {
	rep(i,0,R+C) {
		Pos pos1 = topos(perm[2*i]);
		Pos pos2 = topos(perm[2*i+1]);
		int dir;
		if (pos1.x < 0) dir = RIGHT, pos1.x++;
		else if (pos1.y < 0) dir = DOWN, pos1.y++;
		else if (pos1.x >= C) dir = LEFT, pos1.x--;
		else if (pos1.y >= R) dir = UP, pos1.y--;
		else assert(0);
		if (outpos(bits, pos1, dir) != pos2) return false;
	}
	return true;
}

void solve() {
	cin >> R >> C;
	vi perm(2*R + 2*C);
	rep(i,0,2*R + 2*C) {
		cin >> perm[i];
	}

	cout << endl;
	rep(b,0,(1 << (R*C)))
		if (works(perm, b)) {
			rep(i,0,R) {
				rep(j,0,C) cout << at(b,i,j);
				cout << endl;
			}
			return;
		}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	rep(i,0,N) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
