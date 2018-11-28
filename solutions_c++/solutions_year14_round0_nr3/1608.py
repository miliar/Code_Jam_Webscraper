#include <iostream>
#include <vector>
#include <cstdlib>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <map>
#include <sstream>
#include <list>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <set>
#include <utility>


using namespace std;

void print(int nrow, int ncol, vector<vector<int>> &matrix, int pr, int pc) {
	for (int i = 0; i < nrow; i++) {
		for (int j = 0; j < ncol; j++) {
			if (matrix[i][j] == 2) {
				cout << "*";
				continue;
			}
			if (i == pr && j == pc) {
				cout << "c";
			} else {
				cout << ".";
			}
		}
		cout << endl;
	}
}

/*
void solve(int nrow, int ncol, vector<vector<int>> &matrix) {
	static int dr[] = {0, 1, 1};
	static int dc[] = {1, 0, 1};
	for (int i = 0; i < nrow; i++) {
		for (int j = 0; j < ncol; j++) {
			if (matrix[i][j] == -1) {
				for (int dir = 0; dir < 3; dir++) {
					int pr = i+dr[dir], pc = j+dc[dir];
					if (pr < nrow && pc < ncol && matrix[pr][pc] == 0) { 
						matrix[pr][pc] = 1;
					}
				}
			} else {
		    if (matrix[i][j] == 0){
				print(nrow, ncol, matrix, i, j);
				return;
			}
			}
		}
	}
	cout << "Impossible" << endl;
}


bool hasNeighbor(int pr, int pc, int nrow, int ncol, vector<vector<int>> &matrix, int num) {
	static int dr[] = {-1, -1, -1, 0};
	static int dc[] = {-1, 0, 1, -1};
	for (int dir = 0; dir < 4; dir++) {
		int nr = pr+dr[dir], nc = pc+dc[dir];
		if (nr < 0 || nr >= nrow || nc < 0 || nc >= ncol || matrix[nr][nc] == num) {
			return true;
		}
	}
	return false;
}

*/


/*
static vector<int> tmp(5, 0);
static vector<vector<int>> matrix(5, tmp);

static bool A[] = {true, false, true};
static vector<vector<bool>> tf2(5, vector<bool>(A, A+3));
static vector<vector<vector<bool>>> f(5, tf2);
*/

bool A[] = {true, false, true};
vector<vector<int>> matrix;
vector<vector<vector<bool>>> f;

bool found = false;


void solve(int pr, int pc, int nrow, int ncol, vector<vector<int>> &matrix) {
	if (pr < 0 || pr >= nrow || pc < 0 || pc >= ncol){// || matrix[pr][pc] >= 2) {
		return;
	}
	if (matrix[pr][pc] == 0) {
		matrix[pr][pc] = 3;
		for (int i = -1; i <= 1; i++) {
			for (int j = -1; j <=1; j++) {
				solve(pr+i, pc+j, nrow, ncol, matrix);
			}
		}
	} else {
		if (matrix[pr][pc] == 1) 
			matrix[pr][pc] = 3;
	}
}

bool check(int nrow, int ncol, vector<vector<int>> &matrix) {
	for (int i = 0; i < nrow; i++) {
		for (int j = 0; j  < ncol; j++) {
			if (matrix[i][j] < 2) {
				return false;
			}
		}
	}
	return true;
}


bool legal(int nrow, int ncol, int nmines, vector<vector<int>> &matrix) {
	vector<vector<int>> testmatrix = matrix;
	int ones = 0, rone = 0, cone = 0;
	for (int i = 0; i < nrow; i++) {
		for (int j = 0; j < ncol; j++) {
			if (matrix[i][j] == 0) {
				solve(i, j, nrow, ncol, testmatrix);
				if (check(nrow, ncol, testmatrix)) {
					print(nrow, ncol, matrix, i, j);
					return true;
				}
				return false;
			} else {
				if (matrix[i][j] == 1) {
					ones++;
					rone = i;
					cone = j;
				}
			}
		}
	}
	if (ones == 1) {
		print(nrow, ncol, matrix, rone, cone);
		return true;
	}
	return false;
}

void search(int pr, int pc, int nrow, int ncol, int nmines) {
	//-1	- mine
	//0 - doesn't have mine in neighbors
	//1 - has mine in neighbors
	static int curmines = 0;
	static int dr[] = {0, 1, 1, 1};
	static int dc[] = {1, -1, 0, 1};
	static vector<int> cnt(3, 0);

	if (found == true) {
		return;
	}

	if (pr == nrow) {
		if (curmines == nmines) {
			if (legal(nrow, ncol, nmines, matrix)) {
				found = true;
			}
			
			/*
			cout << "found!!" << endl;
			for (int i = 0; i < nrow; i++) {
				for (int j = 0; j < ncol; j++) {
					cout << matrix[i][j] << " ";
				}
				cout << endl;
			}
			cout << endl;
			*/
		}
		return;
	}
	if (pc == ncol) {
		search(pr+1, 0, nrow, ncol, nmines);
		return;
	}

	vector<vector<vector<bool>>> cur = f;

	if (f[pr][pc][2] && curmines < nmines) {
		matrix[pr][pc] = 2;
		curmines++;
		for (int dir = 0; dir < 4; dir++) {
			int nr = pr+dr[dir], nc = pc + dc[dir];
			if (nr >= 0 && nr < nrow && nc >= 0 && nc < ncol) {
				f[nr][nc][0] = false;
				f[nr][nc][1] = true;
			}
		}
		search(pr, pc+1, nrow, ncol, nmines);
		f = cur;
		curmines--;
	}
//	if (canPlaceOne(pr, pc, nrow, ncol, matrix){

	if (cnt[0]+cnt[1]+nmines >= nrow*ncol) {
		return;
	}
	if (f[pr][pc][1]){// && !(pr > 0 && pc > 0 && matrix[pr-1][pc] == 1 && matrix[pr][pc-1]==1)) {
		cnt[1]++;
		matrix[pr][pc] = 1;
		search(pr, pc+1, nrow, ncol, nmines);
		cnt[1]--;
	}
	if (f[pr][pc][0]) {
		matrix[pr][pc] = 0;
		cnt[0]++;
		for (int dir = 0; dir < 4; dir++) {
			int nr = pr+dr[dir], nc = pc + dc[dir];
			if (nr >= 0 && nr < nrow && nc >= 0 && nc < ncol) {
				f[nr][nc][2] = false;
			}
		}
		cnt[0]--;
		search(pr, pc+1, nrow, ncol, nmines);
		f = cur;
	}
}


int main() {
	int ncases;
	cin >> ncases;
	for (int caseid = 1; caseid <= ncases; caseid++) {
		int nrow, ncol, nmines;
		cin >> nrow >> ncol >> nmines;
/*
	}	

	for (int nrow = 1; nrow <= 5; nrow++) 
		for (int ncol = 1; ncol <= 5; ncol++)
			for (int nmines = 0; nmines <= nrow*ncol; nmines++)
			{
				cout << nrow << " " << ncol << "  " << nmines << endl;
				*/

				cout << "Case #" << caseid << ":" << endl;
				matrix.clear();
				matrix.resize(nrow);
				for (int i = 0; i < nrow; i++) {
					matrix[i].resize(ncol, 0);
				}

				f.clear();
				f.resize(nrow);
				for (int i = 0; i < nrow; i++) {
					f[i].resize(ncol, vector<bool>(A, A+3));
				}

				found = false;

				search(0, 0, nrow, ncol, nmines);
				if (!found) {
					cout << "Impossible\n";
				}
			}
	return 0;
}
