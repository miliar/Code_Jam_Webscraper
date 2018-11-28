#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<int> vi;
typedef vector<vi> vvi;

bool via_libre_izq(const vvc &grid, int y, int x) {
	for (int j = x-1; j >= 0; j--) if (grid[y][j] != '.') return false;
	return true;
}

bool via_libre_der(const vvc &grid, int y, int x) {
	for (int j = x+1; j < (int)grid[y].size(); j++) if (grid[y][j] != '.') return false;
	return true;
}

bool via_libre_up(const vvc &grid, int y, int x) {
	for (int i = y-1; i >= 0; i--) if (grid[i][x] != '.') return false;
	return true;
}

bool via_libre_down(const vvc &grid, int y, int x) {
	for (int i = y+1; i < (int)grid.size(); i++) if (grid[i][x] != '.') return false;
	return true;
}

int main() {
#ifdef TESTING
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
#endif
	int T, R, C, count;
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		cin >> R >> C;
		vvc grid(R, vc(C));
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				cin >> grid[i][j];
		count = 0;
/*
		if (grid[0][0] == '<' || grid[0][0] == '^') count++;
		for (int j = 1; j < C - 1; j++)
			if (grid[0][j] == '^') count++;
		if (grid[0][C-1] == '>' || grid[0][C-1] == '^') count++;
*/
		bool posible = true;
		for (int i = 0; i < R && posible; i++) {
			//if (grid[i][0] == '<') count++;
			for (int j = 0; j < C && posible; j++) {
				if (grid[i][j] == '^' && via_libre_up(grid, i, j)) {
					count++;
					if (via_libre_down(grid, i, j) && via_libre_izq(grid, i, j) && via_libre_der(grid, i, j))
						posible = false;
				} else if (grid[i][j] == '>' && via_libre_der(grid, i, j)) {
					count++;
					if (via_libre_up(grid, i, j) && via_libre_izq(grid, i, j) && via_libre_down(grid, i, j))
						posible = false;
				} else if (grid[i][j] == 'v' && via_libre_down(grid, i, j)) {
					count++;
					if (via_libre_up(grid, i, j) && via_libre_izq(grid, i, j) && via_libre_der(grid, i, j))
						posible = false;
				} else if (grid[i][j] == '<' && via_libre_izq(grid, i, j)) {
					count++;
					if (via_libre_down(grid, i, j) && via_libre_up(grid, i, j) && via_libre_der(grid, i, j))
						posible = false;
				}
			}
			//if (grid[i][C-1] == '>') count++;
		}

		cout << "Case #" << caso << ": ";
		if (posible)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
