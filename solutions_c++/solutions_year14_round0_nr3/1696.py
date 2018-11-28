#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

ifstream fin("c.in");
ofstream fout("c.out");

void showBoard(vector<vector<int> > &m, int x, int y) {
	m[y][x] = 2;
	forn(i,m.size()) {
		forn(j, m[0].size()) {
			cout << (m[i][j] == 2 ? "c" : (m[i][j] ? "*" : "."));
			fout << (m[i][j] == 2 ? "c" : (m[i][j] ? "*" : "."));
		}
		cout << endl;
		fout << endl;
	}
}

void showNums(vector<vector<int> > &m, vector<vector<int> > &p) {
	forn(i,m.size()) {
		forn(j, m[0].size()) {
			if (m[i][j] == 1) cout << "*";
			else cout << p[i][j];
		}
		cout << endl;
	}
}

void showDiscovery(vector<vector<int> > &m, vector<vector<int> > &p, vector<vector<int> > &used) {
	forn(i,m.size()) {
		forn(j, m[0].size()) {
			if (!used[i][j]) cout << "?";
			else if (m[i][j] == 1) cout << "*";
			else cout << p[i][j];
		}
		cout << endl;
	}
}

void toBoard(vector<int> &v, int r, int c, vector<vector<int> > &m) {
	forn(i,r) forn(j,c) m[i][j] = v[i*c+j];
}

int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

bool valid(int r, int c, int x, int y) {
	return x >= 0 && y >= 0 && x < c && y < r;
}

void paintNums(vector<vector<int> > &m, vector<vector<int> > &p) {
	forn(y,m.size()) forn(x,m[0].size()) {
		if (m[y][x] == 1) continue;
		int c = 0;
		forn(k,8) {
			int cx = x + dx[k], cy = y + dy[k];
			if (!valid(m.size(), m[0].size(), cx, cy)) continue;
			if (m[cy][cx] == 1) c++;
		}
		p[y][x] = c;
	}
}

void discover(vector<vector<int> > &m, vector<vector<int> > &p, vector<vector<int> > &used, int x, int y) {
	// This is not a mine
	if (used[y][x] == 1) return;
	used[y][x] = 1;
	if (p[y][x] > 0) return;
	// This is a '0' with no mine around
	forn(k,8) {
		int cx = x + dx[k], cy = y + dy[k];
		if (!valid(m.size(), m[0].size(), cx, cy)) continue;
		discover(m, p, used, cx, cy);
	}
}

bool solved(vector<vector<int> > &m, int x, int y) {
	if (m[y][x] == 1) return false;
	vector<vector<int> > p(m.size(), vector<int>(m[0].size(), 0));
	vector<vector<int> > d(m.size(), vector<int>(m[0].size(), 0));
	paintNums(m, p);
	//showNums(m, p); cout << "--" << endl;
	discover(m, p, d, x, y);
	//showDiscovery(m, p, d); cout << "--" << endl;
	forn(i,m.size()) forn(j,m[0].size()) if (m[i][j] == 0 && d[i][j] == 0) return false;
	return true;
}

int main() {
	int T, r, c, m;
	fin >> T;
	cout << T << endl;
	forn(icase,T) {
		fin >> r >> c >> m;
		
		cout << "Case #" << (icase+1) << ":" << endl;
		fout << "Case #" << (icase+1) << ":" << endl;
		cout << r << " " << c << " " << m << endl;
		
		vector<int> v(r*c, 0);
		forn(i,m) v[v.size()-i-1] = 1;
		
		bool valid = false;
		int posx = 0, posy = 0;
		vector<vector<int> > b(r, vector<int>(c));
		do {
			toBoard(v, r, c, b);
			
			forn(y,r) {
				forn(x,c) if (solved(b, x, y)) {
					posx = x;
					posy = y;
					valid = true;
					break;
				}
				if (valid) break;
			}
		} while(!valid && next_permutation(v.begin(), v.end()));
		if (!valid) {
			cout << "Impossible" << endl;
			fout << "Impossible" << endl;
		} else {
			showBoard(b, posx, posy);
		}
	}
	cout << "Done" << endl;
	
	return 0;
}
