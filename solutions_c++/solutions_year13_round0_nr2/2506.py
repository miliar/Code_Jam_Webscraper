#include <iostream>
#include <string>
using namespace std;


int garden[128][128];

bool validate(int i, int j, int N, int M) {
	int k;
	for(k=0; k<N; k++) {
		if(garden[k][j] > garden[i][j]) break;
	}

	if(k == N) return true;

	for(k=0; k<M; k++) {
		if(garden[i][k] > garden[i][j]) break;
	}

	if(k == M) return true;

	return false;
}

void solve_case() {
	int M, N;
	cin >> N >> M;
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			cin >> garden[i][j];
		}
	}

	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			if(!validate(i,j,N,M)) {
				cout << "NO";
				return;
			}
		}
	}

	cout << "YES";
}


int main() {
	int T;
	cin >> T;

	for(int i=1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		solve_case();
		cout << endl;
	}
}