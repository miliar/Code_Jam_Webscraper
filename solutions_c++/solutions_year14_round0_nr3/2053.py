#include<iostream>
#include <queue>
#include <string.h>
#include <vector>
using namespace std;
bool check (int a[], int m,int r, int c, int *board, int *start) ;
bool run (int start, int *board, int r, int c);
bool next_comb(int comb[], int k, int n);
int main () {

	int r,c,m;
	r = 2; c = 2;
	m = 1;

	int iter = 1, t;
	cin >> t;
	while (iter <= t) {
		cin >> r >> c >> m;
		int a[r*c];
		int *board = new int[r*c];
		for (int i = 0; i < m; i++) {
			a[i] = i;
		}
		bool done = false;
		bool good = false;
		int start;
		while (!done) {
			memset(board, 0, sizeof(int)*r*c);
			bool result = check(a,m,r,c,board,&start);
			if (result) {
				good = true;
				break;
			}
			done = next_comb(a,m,r*c);
		}
		cout << "Case #" << iter++ <<":"<< endl;
		if (good) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					if (board[i*c+j] == -1)  {
						cout << "*";
					} else if (i*c+j == start) {
						cout << "c";// << " ";
					} else {
						cout << ".";// << " ";
					}
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 1;
}

bool check (int a[], int m,int r, int c, int *board, int *start) {
	for (int j = 0; j < m; j++) {
		board[a[j]] = -1;
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			int pos = i*c + j;
			int count = 0;
			if (board[pos] == -1) continue;
			std::vector<int> neighbors;
			for (int l = -1; l < 2; l++) {
				for (int m = -1; m < 2; m++) {
					if (m == 0 && l == 0) continue;
					if (i+l < r && i+l >= 0 && m+j < c && m+j >= 0) {
						neighbors.push_back(((i+l)*c)+j+m);
					}
				}
			}
			//			cout << "******" <<  neighbors.size() << endl;
			for (int n = 0; n <  neighbors.size(); n++) {
				if (neighbors[n] < 0 || neighbors[n] >= r*c) {
					continue;
				}
				if (board[neighbors[n]] == -1) {
					count++;
				}
			}
			board[pos] = count;
		}
	}
	//cout << board[0] << board[1] << board[2] << board[3]<<endl ;
	for (int i = 0; i < r*c; i++) {
		if (board[i] == -1 ) {
			continue;
		} else if (board[i] != 0 && m == r*c - 1) {
			*start = i;
			return true;
		} else if (board[i] != 0) {
			continue;
		}
		
		if(run(i, board,r,c)) {
			*start = i;
			return true;
		}
	}
	return false;
}

bool run (int start, int *board, int r, int c) {
	bool *visited = new bool[r*c]();
	for (int i = 0; i < r*c; i++) visited[i] = false;
	std::queue<int> q;
	q.push(start);
	visited[start] = true;
	while (!q.empty()) {
		int pos = q.front();
		q.pop();
		int i = pos / c;
		int j = pos % c;
		//cout << i << " " << j;
		std::vector<int> neighbors;
		for (int l = -1; l < 2; l++) {
			for (int m = -1; m < 2; m++) {
				if (m == 0 && l == 0) continue;
				if (i+l < r && i+l >= 0 && m+j < c && m+j >= 0) {
					neighbors.push_back(((i+l)*c)+j+m);
				}
			}
		}
		//int neighbors[8] = {(i-1)*c + j, (i+1)*c + j, (i)*c + j+1, (i)*c + j-1, (i+1)*c + j+1, (i-1)*c + j+1, (i-1)*c + j-1,  (i+1)*c + j-1};
		for (int k = 0; k < neighbors.size(); k++) {
			// std::cout << "{" << neighbors[k]/c << "," << neighbors[k]%c << "}" << " ";
			if (neighbors[k] < 0 || neighbors[k] >= r*c) {
				//				cout << "Came here for " << neighbors[k] <<endl;
				continue;
			}
			
			if (!visited[neighbors[k]]) {
				visited[neighbors[k]] = true;
				if (board[neighbors[k]] == 0) {
					q.push(neighbors[k]);
				}
			}
		}
		// cout << endl;
	}
	for (int i = 0; i < r*c; i++) {
		if (board[i] == -1) {
			continue;
		}
		if (!visited[i]) {
			return false;
		}
	}
	return true;
}

bool next_comb(int comb[], int k, int n) {
	int i = k - 1;
	++comb[i];
	while ((i >= 0) && (comb[i] >= n - k + 1 + i)) {
		--i;
		++comb[i];
	}

	if (comb[0] > n - k) /* Combination (n-k, n-k+1, ..., n) reached */
		return true; /* No more combinations can be generated */

	/* comb now looks like (..., x, n, n, n, ..., n).
	Turn it into (..., x, x + 1, x + 2, ...) */
	for (i = i + 1; i < k; ++i)
		comb[i] = comb[i - 1] + 1;

	return false;
}
