#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

struct Point {
	int r;
	int c;
	int h;
};

Point points[10100];
int Board[110][110];

bool cmp(const Point& lhs, const Point& rhs) {
	return lhs.h < rhs.h;
}

ifstream fin("B.in");
ofstream fout("B.out");

int main() {
	int testcase, N, M;
	//cin >> testcase;
	fin >> testcase;
	int board[4][4];
	for (int tc=1; tc<=testcase; ++tc) {
		memset(points, 0, sizeof points);
		memset(Board, 0, sizeof Board);
		//cin >> N >> M;
		fin >> N >> M;
		int index = 0;
		for (int r=0; r<N; ++r) for (int c=0; c<M; ++c) {
			//cin >> Board[r][c];
			fin >> Board[r][c];
			points[index].r = r;
			points[index].c = c;
			points[index].h = Board[r][c];
			++index;
		}

		sort(points, points + index, cmp);

		bool found = false;
		for (int i=0; i<index && !found; ++i) {
			int r = points[i].r;
			int c = points[i].c;
			int h = points[i].h;
			bool OK = true;
			for (int hor=0; hor<M; ++hor) {
				if (Board[r][hor] > h) {
					//cout << "1r " << r << " c " << hor << " h " << Board[r][hor] << " " << h << endl;
					OK = false;
					break;
				}
			}
			if (OK) continue;
			OK = true;
			for (int ver=0; ver<N; ++ver) {
				if (Board[ver][c] > h) {
					//cout << "2r " << ver << " c " << c << " h " << Board[ver][c] << " " << h << endl;
					OK = false;
					break;
				}
			}
			if (!OK) found = true;
		}
		//cout << "Case #" << tc << ": " << (found ? "NO" : "YES") << endl;
		fout << "Case #" << tc << ": " << (found ? "NO" : "YES") << endl;
	}

	return 0;
}