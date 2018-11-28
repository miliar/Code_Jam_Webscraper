#include <fstream>
#include <vector>
using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;
	for (int test = 1; test <= T; test++) {
		int r, c;
		in >> r >> c;
		vector<vector<char>> map(r, vector<char>(c));
		vector<vector<bool>> over(r, vector<bool>(c, false)), below(r, vector<bool>(c, false));
		vector<vector<bool>> left(r, vector<bool>(c, false)), right(r, vector<bool>(c, false));
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				in >> map[i][j];
				over[i][j] = i > 0 && (map[i - 1][j] != '.' || over[i - 1][j]);
				left[i][j] = j > 0 && (map[i][j - 1] != '.' || left[i][j - 1]);
			}
			in.ignore();
		}
		for (int i = r - 1; i >= 0; i--) {
			for (int j = c - 1; j >= 0; j--) {
				below[i][j] = i < r - 1 && (map[i + 1][j] != '.' || below[i + 1][j]);
				right[i][j] = j < c - 1 && (map[i][j + 1] != '.' || right[i][j + 1]);
			}
		}

		int change = 0;
		for (int i = 0; i < r && change >= 0; i++) {
			for (int j = 0; j < c && change >= 0; j++) {
				if (map[i][j]!='.' && !over[i][j] && !below[i][j] && !left[i][j] && !right[i][j]) {
					change = -1;
				}
				else {
					switch (map[i][j]) {
					case '^': change += !over[i][j]; break;
					case '<': change += !left[i][j]; break;
					case 'v': change += !below[i][j]; break;
					case '>': change += !right[i][j]; break;
					}
				}
			}
		}
		out << "Case #" << test << ": ";
		if (change >= 0) {
			out << change <<endl;
		}
		else {
			out << "IMPOSSIBLE" << endl;
		}
	}
	return 0;

}