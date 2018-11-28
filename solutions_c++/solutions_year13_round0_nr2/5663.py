#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

char a[100][100];
int T,M,N;


void OPEN() {
    freopen("thefile.txt","r",stdin);
    freopen("output.txt","w",stdout);
}

bool is_ok(int x, int y) {
	bool canx1 = true, canx2 = true, cany1 = true, cany2 = true;
	for (int i=0; i<x; i++) {
		if (a[x][i] > a[x][y]) {
			canx1 = false;
			break;
		}
	}
	for (int i=x+1; i<N; i++) {
		if (a[x][i] > a[x][y]) {
			canx2 = false;
			break;
		}
	}
	for (int i=0; i<y; i++) {
		if (a[i][y] > a[x][y]) {
			cany1 = false;
			break;
		}
	}
	for (int i=y+1; i<M; i++) {
		if (a[i][y] > a[x][y]) {
			cany2 = false;
			break;
		}
	}
	return (canx1 || canx2 || cany1 || cany2);
}

int max0 = 0;
vector<int> rows, cols;
void solve() {
	max0 = 0;
	rows.clear(); cols.clear();
	for (int i=0; i < N; i++) 
		for (int j=0; j < M; j++) {
			if (a[i][j] > max0) max0 = a[i][j];
		}
	for (int i=0; i< N; i++) {
		int tmp = a[i][0];
		bool go_this_row = true;
		for (int j=1; j< M; j++) {
			if (a[i][j]!=tmp) {
				go_this_row = false;
				break;
			}
		}
		if (go_this_row) rows.push_back(i);
	}
	for (int j=0; j< M; j++) {
		bool go_this_col = true;
		for (int i=1; i < N; i++) {
			if (a[i][j]!= a[0][j]) {
				go_this_col = false;
				break;
			}
		}
		if (go_this_col) cols.push_back(j);
	}
	int b[100][100];
	for (int i=0; i < N; i++)
		for (int j=0; j < M; j++) b[i][j] = max0;
	for (int k=0; k<rows.size(); k++) {
		for (int j=0; j<M; j++) {
			b[rows[k]][j] = a[rows[k]][0];
		}
	}
	for (int k=0; k<cols.size(); k++) {
		for (int i=0; i<N; i++) {
			b[i][cols[k]] = a[0][cols[k]];
		}	
	}
	for (int i=0; i<N; i++) 
		for (int j=0; j<M; j++) {
			if (a[i][j]!=b[i][j]) {
				cout << "NO" << endl;
				return;
			}
		}
	
	cout << "YES" << endl;	
}

int main() {
	OPEN();
  
	
	cin >> T;
	
	for (int i=0; i<T; i++) {
		cin >> N >> M;
		for (int u=0; u < N; u++) {
			for (int v=0; v<M; v++) {
				cin >> a[u][v];
			}
		}
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}