#include <iostream>

using namespace std;

int N,M;
int soll[100][100];
int ist[100][100];

bool try_mow_v(int col, int height) {
	for(int i=0; i<N; ++i) {
		if(soll[i][col] > height)
			return false;
	}
	for(int i=0; i<N; ++i)
		ist[i][col] = height;
	return true;
}

bool try_mow_h(int row, int height) {
	for(int i=0; i<M; ++i) {
		if(soll[row][i] > height)
			return false;
	}
	for(int i=0; i<M; ++i)
		ist[row][i] = height;
	return true;
}

int main() {
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		bool suc = true;
		cin >> N >> M;
		for(int i=0; i<N; ++i) for(int j=0; j<M; ++j) {
			cin >> soll[i][j];
			ist[i][j] = 100;
		}
		for(int i=0; i<N; ++i) for(int j=0; j<M; ++j) {
			if(ist[i][j] == soll[i][j]) continue;
			int sollx = soll[i][j];
			if(!try_mow_h(i,sollx) && !try_mow_v(j,sollx)) {
				suc = false;
				break;
			}
		}
		cout << "Case #" << t << ": " << ((suc)?"YES":"NO") << endl;
	}
}
