#include<bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

ostream& operator<<(ostream &out, const pii &a) { return out << '(' << a.first << ", " << a.second << ')'; }
istream& operator>>(istream &in, pii &a) { return in >> a.first >> a.second; }

const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

// lambda-expression: [] (args) -> retType { body }

const int MAXBORDER = 400;
const int MAXA = 100;

int R, C, target[2 * MAXBORDER];

bool grid[MAXA][MAXA];

// 0123: NESW
struct pos {
	pii pt;
	int c;

	pos(pii _pt, int _c) : pt(_pt), c(_c) {}

	pos next(bool g) {
		if (g) { // /
			switch(c) {
			case 0: return pos(pt, 3);
			case 1: return pos(pt, 2);
			case 2: return pos(pt, 1);
			case 3: return pos(pt, 0);
			}
		} else { // \

			switch(c) {
			case 0: return pos(pt, 1);
			case 1: return pos(pt, 0);
			case 2: return pos(pt, 3);
			case 3: return pos(pt, 2);
			}
		}
		assert(false);
		return pos(pii(-1,-1),-1);
	}

	bool isSide() {
		return (pt.first == 0 && c == 0) || (pt.second == C - 1 && c == 1)
			|| (pt.first == R - 1 && c == 2) || (pt.second == 0 && c == 3);
	}

	pos swapSide() {
		switch(c) {
		case 0: return pos(pii(pt.first - 1, pt.second), 2);
		case 1: return pos(pii(pt.first, pt.second + 1), 3);
		case 2: return pos(pii(pt.first + 1, pt.second), 0);
		case 3: return pos(pii(pt.first, pt.second - 1), 1);
		}
		assert(false);
		return pos(pii(-1,-1),-1);
	}
};

pos getSide(int i)
{
	if (i < C) {
		return pos(pii(0, i), 0);
	} else if (i < C + R) {
		return pos(pii(i - C, C - 1), 1);
	} else if (i < C + R + C) {
		return pos(pii(R - 1, C - 1 - (i - (C + R))), 2);
	} else {
		return pos(pii(R - 1 - (i - (C + R + C)), 0), 3);
	}
}

bool operator==(const pos &lhs, const pos &rhs)
{
	return lhs.pt == rhs.pt && lhs.c == rhs.c;
}

ostream& operator<<(ostream &out, const pos &po)
{
	return out << po.pt.first << ", " << po.pt.second << ", " << po.c;
}

void run() {
	cin >> R >> C;
	for (int i = 0; i < (R + C); i++) {
		int x, y;
		cin >> x >> y;
		target[x - 1] = y - 1;
		target[y - 1] = x - 1;
	}

	bool poss = false;

	int A = R * C;
	for (int i = 0; i < (1 << A); i++) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				int j = C * r + c;
				grid[r][c] = ((i >> j) & 1);
			}
		}

//		cerr << "Checking board:" << endl;
//		for (int r = 0; r < R; r++) {
//			for (int c = 0; c < C; c++) {
//				cerr << grid[r][c];
//			}
//			cerr << endl;
//		}
//		cerr << endl;

		bool valid = true;
		for (int j = 0; j < 2 * (R + C); j++) {
			int k = target[j];

			pos p = getSide(j);
			while (true) {
				p = p.next(grid[p.pt.first][p.pt.second]);
				if (p.isSide()) {
					break;
				}
				p = p.swapSide();

				assert(0 <= p.pt.first && p.pt.first < R);
				assert(0 <= p.pt.second && p.pt.second < C);
			}

//			 cerr << j << " -> " << k << " ; " << p << " ; " << getSide(k) << endl;

			if (!(getSide(k) == p)) {
				valid = false;
				break;
			}
		}

		if (valid) {
			poss = true;

			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					cout << (grid[r][c] ? '/' : '\\');
				}
				cout << endl;
			}
			break;
		}
	}
	if (!poss) {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main() {
#ifdef LOCAL
    assert(freopen("input.txt", "r", stdin));
//    assert(freopen("debug.txt", "w", stderr));
    assert(freopen("output.txt", "w", stdout));

#endif // LOCAL
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// cerr << boolalpha;
	(cout << fixed).precision(10);

	int ntc;
	cin >> ntc;
	for (int tc = 1; tc <= ntc; tc++) {
		cout << "Case #" << tc << ":" << endl;
		run();
	}

	return 0;
}
