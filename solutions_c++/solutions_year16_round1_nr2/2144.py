#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> GLOBAL_DONE_X,
			 GLOBAL_DONE_Y;

void coutGrid(vector<vector<int> >& grid) {
	cout << endl;
	for (int y = 0; y < grid.size(); ++y) {
		for (int x = 0; x < grid[0].size(); ++x) {
			cout << grid[y][x] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

bool isValid(vector<vector<int> >& grid, vector<vector<int> >& lines, vector<bool>& doneX, vector<bool>& doneY) {
	// All rows are in increasing order
	for (int y = 0; y < grid.size(); ++y) {
		if (grid[y][0] == 0) break;
		for (int x = 1; x < grid[0].size(); ++x) {
			if (grid[y][x] <= grid[y][x-1]) return false;
		}
	}

	// All columns are in increasing order
	for (int x = 0; x < grid[0].size(); ++x) {
		if (grid[0][x] == 0) break;
		for (int y = 1; y < grid.size(); ++y) {
			if (grid[y][x] <= grid[y-1][x]) return false;
		}
	}

	// Check that all columns can go into a line
	int numMisses = 0;
	for (int x = 0; x < grid[0].size(); ++x) {
		if (doneY[x]) continue;
		bool hasMatch = false;
		for (int l = 0; l < lines.size(); ++l) {
			//cout << "testing line: ";
			//for (int i = 0; i < lines[l].size(); ++i)
			//	cout << lines[l][i] << " ";
			//cout << endl;
			bool lineMatches = true;
			for (int y = 0; y < grid.size(); ++y) {
				if (grid[y][x] == 0) continue;
				//cout << "if " << grid[y][x] << " != " << lines[l][y] << endl;
				if (grid[y][x] != lines[l][y]) {
					lineMatches = false;
					break;
				}
			}
			if (lineMatches) {
				hasMatch = true;
				break;
			}
		}
		if (!hasMatch) numMisses++;
	}
	if (numMisses > 1) {
		//cout << "does not have match: " << endl;
		//coutGrid(grid);
		return false;
	}

	return true;
}

vector<vector<int> > solve(vector<vector<int> > grid, vector<vector<int> > lines, vector<bool> doneX, vector<bool> doneY) {
	if (!isValid(grid, lines, doneX, doneY)) {
		return vector<vector<int> >();
	}
	if (lines.empty()) {
		GLOBAL_DONE_X = doneX;
		GLOBAL_DONE_Y = doneY;
		return grid;
	}


	for (int l = 0; l < lines.size(); ++l) {
		// Place in next available row
		vector<vector<int> > copyGrid(grid);
		int nextRow = -1;
		for (int y = 0; y < grid.size(); ++y) {
			if (grid[y][0] == 0) nextRow = y;
		}
		if (nextRow > -1) {
			for (int x = 0; x < grid[0].size(); ++x) {
				copyGrid[nextRow][x] = lines[l][x];
			}
			doneX[nextRow] = true;
			vector<vector<int> > copyLines(lines);
			copyLines.erase(copyLines.begin() + l);
			vector<vector<int> > ret = solve(copyGrid, copyLines, doneX, doneY);
			if (ret.size() > 0) return ret;
		}

		// See if the row can go into an existing one
		if (nextRow == -1) {
			bool matches;
			int matchesCol = -1;
			for (int x = 0; x < grid[0].size(); ++x) {
				matches = true;
				matchesCol = x;
				for (int y = 0; y < grid.size(); ++y) {
					if (grid[y][x] != lines[l][y]) {
						matches = false;
						break;
					}
				}
				if (matches) {
					doneY[matchesCol] = true;
					break;
				}
			}
			if (matches) {
				vector<vector<int> > copyLines2(lines);
				copyLines2.erase(copyLines2.begin() + l);
				vector<vector<int> > ret = solve(grid, copyLines2, doneX, doneY);
				if (ret.size() > 0) return ret;
			}
		}		
	}
	return vector<vector<int> >();
}

int main() {
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; ++caseNum) {
		int n;
		cin >> n;
		vector<vector<int> > grid(n, vector<int>(n));
		vector<vector<int> > lines;
		for (int i = 0; i < 2 * n - 1; ++i) {
			vector<int> line(n);
			for (int j = 0; j < n; ++j) {
				cin >> line[j];
			}
			lines.push_back(line);
		}
		sort(lines.begin(), lines.end());
		reverse(lines.begin(), lines.end());

		vector<bool> doneX(n, false);
		vector<bool> doneY(n, false);
		vector<vector<int> > solvedGrid = solve(grid, lines, doneX, doneY);


		cout << "Case #" << caseNum << ": ";		
		for (int i = 0; i < GLOBAL_DONE_X.size(); ++i) {
			if (GLOBAL_DONE_X[i] == false) {
				for (int x = 0; x < grid[0].size(); ++x) {
					cout << solvedGrid[i][x] << " ";
				}
				cout << endl;
			}
		}

		for (int i = 0; i < GLOBAL_DONE_Y.size(); ++i) {
			if (GLOBAL_DONE_Y[i] == false) {
				for (int y = 0; y < grid.size(); ++y) {
					cout << solvedGrid[y][i] << " ";
				}
				cout << endl;
			}
		}
	}
	return 0;
}
