#include <iostream>
#include <set>
#include <complex>
#include <cassert>
#include <vector>

using namespace std;

typedef complex<int> V;
#define row real()
#define col imag()

int rowmin[128];
int rowmax[128];
int colmin[128];
int colmax[128];
int R, C;
vector<pair<V, char>> arrows;

int main() {
	cin.sync_with_stdio(false);
	
	int Te;
	cin >> Te;
	
	for(int T = 0; T < Te; ++T) {
		fill(rowmin, rowmin + 128, 1000);
		fill(rowmax, rowmax + 128, -1);
		fill(colmin, colmin + 128, 1000);
		fill(colmax, colmax + 128, -1);
		arrows.clear();
		
		cin >> R >> C;
		string L;
		for(int i = 0; i < R; ++i) {
			cin >> L;
			for(int j = 0; j < C; ++j) {
				if(L[j] == '.') continue;
				rowmin[i] = min(rowmin[i], j);
				rowmax[i] = max(rowmax[i], j);
				colmin[j] = min(colmin[j], i);
				colmax[j] = max(colmax[j], i);
				arrows.emplace_back(V(i, j), L[j]);
			}
		}
		
		bool impos = false;
		for(auto p : arrows) {
			V pos = p.first;
			int i = pos.row;
			int j = pos.col;
			if(rowmin[i] == j && rowmax[i] == j && colmin[j] == i && colmax[j] == i) {
				impos = true;
				break;
			}
		}
		
		cout << "Case #" << T + 1 << ": ";
		if(impos) {
			cout << "IMPOSSIBLE";
		} else {
			int res = 0;
			for(auto p : arrows) {
				V pos = p.first;
				char dir = p.second;
				int i = pos.row;
				int j = pos.col;
				switch(dir) {
					case '<': {
						if(rowmin[i] == j) ++res;
					} break;
					case '>': {
						if(rowmax[i] == j) ++res;
					} break;
					case '^': {
						if(colmin[j] == i) ++res;
					} break;
					case 'v': {
						if(colmax[j] == i) ++res;
					} break;
					default: assert(false);
				}
			}
			cout << res;
		}
		cout << '\n';
	}
	
	return 0;
}
