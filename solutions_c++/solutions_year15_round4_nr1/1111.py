#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int main() {
	ifstream fin("E:\\A-large.in");
	// ifstream fin("E:\\temp.txt");
	ofstream fout("E:\\A-large.out");
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++) {
		int R, C;
		fin >> R >> C;
		char grid[100][100];
		set<char> feasible_d[100][100];
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				fin >> grid[j][k];
				if (j == 0 || j == R - 1 || k == 0 || k == C - 1) {
					if (j == 0 && k == 0) {
						feasible_d[j][k].insert('>');
						feasible_d[j][k].insert('v');
					}
					else {
						if (j == 0 && k == C - 1) {
							feasible_d[j][k].insert('<');
							feasible_d[j][k].insert('v');
						}
						else {
							if (j == R - 1 && k == 0) {
								feasible_d[j][k].insert('^');
								feasible_d[j][k].insert('>');
							}
							else {
								if (j == R - 1 && k == C - 1) {
									feasible_d[j][k].insert('^');
									feasible_d[j][k].insert('<');
								}
								else {
									if (j == 0) {
										feasible_d[j][k].insert('>');
										feasible_d[j][k].insert('<');
										feasible_d[j][k].insert('v');
									}
									else {
										if (j == R - 1) {
											feasible_d[j][k].insert('>');
											feasible_d[j][k].insert('<');
											feasible_d[j][k].insert('^');
										}
										else {
											if (k == 0) {
												feasible_d[j][k].insert('>');
												feasible_d[j][k].insert('^');
												feasible_d[j][k].insert('v');
											}
											else {
												if (k == C - 1) {
													feasible_d[j][k].insert('^');
													feasible_d[j][k].insert('<');
													feasible_d[j][k].insert('v');
												}
											}
										}
									}
								}
							}
						}
					}
				}
				else {
					feasible_d[j][k].insert('>');
					feasible_d[j][k].insert('<');
					feasible_d[j][k].insert('v');
					feasible_d[j][k].insert('^');
				}
			}
		}

		bool impossible = false;
		int count = 0;
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (impossible == true) {
					continue;
				}
				if (grid[j][k] == '.') {
					continue;
				}
				bool find = false;
				for (char c : feasible_d[j][k]) {
					if (find == true) {
						continue;
					}
					switch (c) {
					case '^':
						for (int l = j - 1; l >= 0; l--) {
							if (grid[l][k] != '.') {
								find = true;
								break;
							}
						}
						break;
					case 'v':
						for (int l = j + 1; l < R; l++) {
							if (grid[l][k] != '.') {
								find = true;
								break;
							}
						}
						break;
					case '<':
						for (int l = k - 1; l >= 0; l--) {
							if (grid[j][l] != '.') {
								find = true;
								break;
							}
						}
						break;
					case '>':
						for (int l = k + 1; l < C; l++) {
							if (grid[j][l] != '.') {
								find = true;
							}
						}
						break;
					default:
						break;
					}
				}
				if (find == false) {
					impossible = true;
				}
			}
		}
		if (impossible == true) {
			fout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (grid[j][k] == '.') {
					continue;
				}
				if (feasible_d[j][k].find(grid[j][k]) == feasible_d[j][k].end()) {
					count++;
				}
				else {
					bool find = false;
					switch (grid[j][k]) {
					case '^':
						for (int l = j - 1; l >= 0; l--) {
							if (grid[l][k] != '.') {
								find = true;
								break;
							}
						}
						break;
					case 'v':
						for (int l = j + 1; l < R; l++) {
							if (grid[l][k] != '.') {
								find = true;
								break;
							}
						}
						break;
					case '<':
						for (int l = k - 1; l >= 0; l--) {
							if (grid[j][l] != '.') {
								find = true;
								break;
							}
						}
						break;
					case '>':
						for (int l = k + 1; l < C; l++) {
							if (grid[j][l] != '.') {
								find = true;
							}
						}
						break;

					default:
						break;
					}
					if (find == false) {
						count++;
					}
				}
			}
		}
		fout << "Case #" << i << ": " << count << endl;

	}
	return 0;
}
