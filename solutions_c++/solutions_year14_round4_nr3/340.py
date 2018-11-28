#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')

#define X first
#define Y second
typedef pair<int, int> Point;
struct Building {
	Point a, b;
};

int w, h, bn;
vector<Building> builds;
vector<int> ys;
vector<vector<int>> used;

Point operator+(Point a, Point b) {
	return Point(a.X + b.X, a.Y + b.Y);
}
Point operator-(Point a, Point b) {
	return Point(a.X - b.X, a.Y - b.Y);
}
ostream &operator<<(ostream &s, Point p) {
	return s << '(' << p.X << ' ' << p.Y << ')';
}

int shrink(int y) {
	auto it = lower_bound(all(ys), y);
	assert(it != end(ys) && *it == y);
	return it - begin(ys);
}

void setfull(int x, int y) {
	used[x][y] = ys[y + 1] - ys[y];
}

bool full(int x, int y) {
	return used[x][y] == ys[y + 1] - ys[y];
}

bool inbounds(Point p) {
	return 0 <= p.X && p.X < w && 0 <= p.Y && p.Y <= h;
}

const Point dxy[] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

bool flow(int x) {
	if (full(x, 0)) return false;
	vector<Point> pos;
	pos.push_back(Point(x, -1));
	pos.push_back(Point(x, 0));
	while (true) {
		Point p = pos.back();
		//E(p);
		if (p.Y < 0) return false;
		if (p.Y >= h) return true;
		++used[p.X][p.Y];
		assert(pos.size() >= 2);
		Point q = pos[pos.size() - 2];
		int pdir = -1;
		for (int dir = 0; dir < 4; ++dir) if (p - q == dxy[dir]) {
			pdir = dir;
			break;
		}
		assert(pdir != -1);
		bool found = false;
		for (int ndir = pdir + 3; ndir <= pdir + 5; ++ndir) {
			int dir = ndir & 3;
			if (dir == pdir) setfull(p.X, p.Y);
			Point pp = p + dxy[dir];
			if (inbounds(pp) && !full(pp.X, pp.Y)) {
				found = true;
				pos.push_back(pp);
				break;
			}
		}
		if (found) continue;
		//E("pop", p);
		setfull(p.X, p.Y);
		pos.pop_back();
	}
}

void process() {
	scanf("%d%d%d", &w, &h, &bn);
	builds.resize(bn);
	for (auto &b: builds) {
		scanf("%d%d%d%d", &b.a.X, &b.a.Y, &b.b.X, &b.b.Y);
		++b.b.X;
		++b.b.Y;
	}

	ys = {0, h};
	for (auto &b: builds) {
		ys.push_back(b.a.Y);
		ys.push_back(b.b.Y);
	}
	for (int y = 0; y <= h; ++y) ys.push_back(y);
	sort(all(ys));
	ys.erase(unique(all(ys)), end(ys));
	ys.push_back(ys.back() + 1);

	h = shrink(h);
	used.assign(w, vector<int>(h + 1, 0));
	for (auto &b: builds) {
		b.a.Y = shrink(b.a.Y);
		b.b.Y = shrink(b.b.Y);
		for (int x = b.a.X; x < b.b.X; ++x)
			for (int y = b.a.Y; y < b.b.Y; ++y)
				setfull(x, y);
	}

	//for (auto yy: ys) E(yy); E(h);

	int ans = 0;
	for (int i = 0; i < w; ++i) {
		if (flow(i)) ++ans;
	}
	printf("%d\n", ans);
}

int main() {
	ios_base::sync_with_stdio(false);
	int tcases;
	scanf("%d", &tcases);
	for (int tcase = 1; tcase <= tcases; ++tcase) {
		printf("Case #%d: ", tcase);
		process();
	}
	return 0;
}
