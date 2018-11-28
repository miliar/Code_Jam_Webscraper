#include <fstream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

int v[30];
char a[10][10];
char mat[10][10];
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int main() {
	ifstream f("input.txt");
	FILE* g = fopen("output.txt", "wt");
	int t;
	int R, C, M;
	f >> t;
	for(int testCase = 1; testCase <= t; testCase++) {
		f >> R >> C >> M;
		for(int i = 0; i < R * C; i++) {
			if(i < R * C - M)	v[i] = 0;
			else				v[i] = 1;
		}
		bool isImpossible = true;
		do {
			int vCont = 0;
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					a[i][j] = (v[vCont] == 0 ? '.' : '*');
					vCont++;
				}
			}
			memcpy(mat, a, sizeof(mat)); //save a in mat
			//search for a click position that uncovers all cells
			for(int i = 0; i < R && isImpossible; i++) {
				for(int j = 0; j < C && isImpossible; j++) {
					if(a[i][j] == '.') {
						//click, uncover and fill
						queue<pair<int, int> > q;
						q.push(pair<int, int> (i, j));
						while(!q.empty()) {
							pair<int, int> p = q.front();
							q.pop();
							int sCnt = 0;
							for(int k = 0; k < 8; k++) {
								int ii = p.first + dx[k];
								int jj = p.second + dy[k];
								if(ii >= 0 && ii < R && jj >= 0 && jj < C && a[ii][jj] == '*')	sCnt++;
							}
							a[p.first][p.second] = sCnt + '0';
							if(sCnt == 0) {
								for(int k = 0; k < 8; k++) {
									int ii = p.first + dx[k];
									int jj = p.second + dy[k];
									if(ii >= 0 && ii < R && jj >= 0 && jj < C && a[ii][jj] == '.')	q.push(pair<int, int> (ii, jj));
								}
							}
						}
						//check if there are any non mined uncovered cells
						bool won = true;
						for(int i1 = 0; i1 < R && won; i1++) {
							for(int j1 = 0; j1 < C && won; j1++) {
								if(a[i1][j1] == '.') {
									won = false;
								}
							}
						}
						if(!won) {//repair a
							memcpy(a, mat, sizeof(mat));
						}
						else {//won, print result, stop searching
							fprintf(g, "Case #%d:\n", testCase);
							mat[i][j] = 'c';
							for(int i1 = 0; i1 < R; i1++) {
								for(int j1 = 0; j1 < C; j1++) {
									fprintf(g, "%c", mat[i1][j1]);
								}
								fprintf(g, "\n");
							}
							isImpossible = false;
						}
					}
				}
			}

		} while(next_permutation(v, v + R * C) && isImpossible);
		if(isImpossible) fprintf(g, "Case #%d:\nImpossible\n", testCase);
	}
	f.close();
	fclose(g);
	return 0;
}
