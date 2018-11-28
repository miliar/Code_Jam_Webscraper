#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Position {
	int x, y;
};

bool empty(char cell) {
	return cell=='.';
}

struct Grid {
	vector<string> cells;
	bool out_of_bounds(Position p) const {
		int h = cells.size();
		if (p.y<0 || p.y>=h)
			return true;
		int w = cells.front().size();
		if (p.x<0 || p.x>=w)
			return true;
		return false;
	}

	bool safe(Position p, char direction) {
		int dx, dy;
		switch (direction) {
			case '<': dx=-1; dy=0; break;
			case '>': dx=1; dy=0; break;
			case 'v': dx=0; dy=1; break;
			case '^': dx=0; dy=-1; break;
			default: cerr << "whoops"; terminate();
		}

		for (;;) {
			p.x += dx;
			p.y += dy;
			if (out_of_bounds(p))
				return  false;
			if (!empty(at(p)))
				return true;
		}
	}

	char at(Position p) const {
		return cells[p.y][p.x];
	}
};

void run_test(istream &fi) {
	string line;
	int R, C;
	fi >> R >> C;
	getline(fi, line);
	Grid g;

	for (int y=0; y<R; ++y) {
		getline(fi, line);
		if (line.size()!=C) {
			cerr << "whoops"; terminate();
		}
		g.cells.push_back(line);
	}

	int ans = 0;
	Position p;
	for (p.y=0; p.y<R; p.y++) {
		for (p.x=0; p.x<C; p.x++) {
			if (!empty(g.at(p))) {
				if (g.safe(p, g.at(p)))
					continue;
				if (
					(g.safe(p, '<' )) ||
					(g.safe(p, '>' )) ||
					(g.safe(p, 'v' )) ||
					(g.safe(p, '^' )) 
				) {
					++ans;
				} else {
					cout << "IMPOSSIBLE";
					return;
				}
			}
		}
	}
	cout << ans;
}

#include <fstream>
int main() {
	int n;
	istream &fi = cin;
	fi >> n;
	for (int i=1; i<=n; i++) {
		cout << "Case #" << i << ": ";
		run_test(fi);
		cout << endl;
	}
}
