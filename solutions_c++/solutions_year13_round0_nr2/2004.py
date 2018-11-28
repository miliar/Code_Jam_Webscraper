#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;

bool isPossible() {
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i<= T; ++i) {
		int N, M;
		cin >> N >> M;
		vector<vector<int> > P(N, vector<int>(M));
		vector<int> row(N,-1), col(M,-1);
		for (int x = 0; x<N;++x) {
			for (int y = 0; y<M; ++y) {
				cin >> P[x][y];
				if (P[x][y]>row[x])
					row[x] = P[x][y];
				if (P[x][y]>col[y])
					col[y] = P[x][y];
			}
		}
		bool flag = true;
		for (int x = 0; x<N;++x) {
			for (int y = 0; y<M; ++y) {
				if (P[x][y] != min(col[y], row[x]))
					flag = false;
			}
		}
		cout << "Case #" << i <<": ";
		if (flag)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}