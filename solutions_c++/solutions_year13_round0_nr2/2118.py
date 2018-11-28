#include <iostream>

using namespace std;

bool check(int a[101][101], int currX, int currY, int N, int M) {
	bool possible = true;
	for (int i = 0; i < N; i++) {
		if (a[i][currY] > a[currX][currY]) {
			possible = false;
		}
	}
	if (!possible) {
		possible = true;
		for (int i = 0; i < M; i++) {
			if (a[currX][i] > a[currX][currY]) {
				possible = false;
			}
		}
	}
	if (possible) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	int T, M, N;
	int a[101][101];
		cin>>T;
	for (int i = 0; i < T; i++) {
		cin>>N>>M;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin>>a[j][k];
			}
		}
		bool done = false;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				if (check(a, j, k, N, M) == false) {
					cout<<"Case #"<<(i + 1)<<": NO"<<endl;
					done = true;
					break;
				}
			}
			if (done) {
				break;
			}
		}
		if (!done)
		cout<<"Case #"<<(i + 1)<<": YES"<<endl;
	}
	return 0;
}
