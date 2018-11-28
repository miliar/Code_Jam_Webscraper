#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int mat[100][100];
int ori[100][100];


int main() {
	int t;
	cin >> t;
	for (int kei = 1; kei <= t; kei++) {
		cout << "Case #" << kei << ": ";
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> mat[i][j];
			}
		}
		priority_queue<pair<int,pair<int,int> > > pq;
		// 0,1 = row,col max
		for (int i = 0; i < n; i++) {
			int Max = -1;
			for (int j = 0; j < m; j++) {
				Max = max(Max, mat[i][j]);
			}
			pq.push(make_pair(Max, make_pair(0,i)));
		}
		for (int j = 0; j < m; j++) {
			int Max = -1;
			for (int i = 0; i < n; i++) {
				Max = max(Max, mat[i][j]);
			}
			pq.push(make_pair(Max, make_pair(1,j)));
		}
		while (!pq.empty()) {
			pair<int, pair<int,int> > p = pq.top();
			pq.pop();
			int tofill = p.first;
			if (p.second.first == 0) {
				int x = p.second.second;
				for (int i = 0; i < m; i++) {
					ori[x][i] = tofill;
				}
			}
			else {
				int x = p.second.second;
				for (int i = 0; i < n; i++) {
					ori[i][x] = tofill;
				}
			}
		}
		bool ok = true;
		for (int i = 0; ok && i < n; i++) {
			for (int j = 0; ok && j < m; j++) {
				if (mat[i][j] != ori[i][j]) {
					ok = false;
				}
			}
		}
		cout << (ok ? "YES" : "NO") << endl;
	}
	return 0;
}