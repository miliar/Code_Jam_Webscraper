#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char* argv[]){
	ifstream infile(argv[1]);

	int numTrials;
	infile >> numTrials;

	for (int trial = 1; trial <= numTrials; trial++){
		cout << "Case #" << trial << ": ";
		int R,C;
		infile >> R >> C;
		vector< string > grid;
		for (int r = 0; r < R; r++) {
			string line;
			infile >> line;
			grid.push_back(line);
		}

		vector <vector <int> > counts(R);
		for (int r = 0; r < R; r++){
			counts[r] = vector<int> (C);
			for (int c = 0; c < C; c++)
				counts[r][c]=0;
		}


		for (int r=0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] != '.') {
					counts[r][c]++;
					break;
				}
			}
			for (int c = C-1; c >= 0; c--) {
				if (grid[r][c] != '.') {
					counts[r][c]++;
					break;
				}
			}
		}

		for (int c=0; c < C; c++) {
			for (int r = 0; r < R; r++) {
				if (grid[r][c] != '.') {
					counts[r][c]++;
					break;
				}
			}
			for (int r = R-1; r >= 0; r--) {
				if (grid[r][c] != '.') {
					counts[r][c]++;
					break;
				}
			}
		}

		bool possible = true;

		for (int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				if (counts[r][c] == 4)
					possible = false;
			}
		}
		if (!possible) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		for (int r = 0; r<R; r++)
			for (int c=0; c< C; c++)
				counts[r][c] = 0;

		for (int r=0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] != '.'){
				if (grid[r][c] == '<') {
					counts[r][c] = 1;
					break;
				}
				break;
				}
			}
			for (int c = C-1; c >= 0; c--) {
				if (grid[r][c] != '.'){
				if (grid[r][c] =='>') {
					counts[r][c] = 1;
					break;
				}
				break;
				}
			}
		}

		for (int c=0; c < C; c++) {
			for (int r = 0; r < R; r++) {
			  if (grid[r][c] != '.'){
				if (grid[r][c] == '^') {
					counts[r][c] = 1;
					break;
				}
				break;
				}
			}
			for (int r = R-1; r >= 0; r--) {
				if (grid[r][c] != '.'){
				if (grid[r][c] == 'v') {
					counts[r][c] = 1;
					break;
				}
				break;
				}
			}
		}

		int total = 0;
		for (int r = 0; r< R; r++)
			for (int c = 0; c < C; c++)
				total += counts[r][c];
		cout << total << endl;



	}
}
