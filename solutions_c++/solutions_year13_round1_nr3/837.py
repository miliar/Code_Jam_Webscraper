#include <iostream>
#include <string>

using namespace std;

int ps[12];
int p[12];
int R, M, N, K;

int isSolved() {


	for(int i=0;i<K;i++) {
		int t = ps[i];
		for(int j=0;j<N;j++) {
			if(t % p[j] == 0)
				t /= p[j];
		}
		if(t!=1)
			return 0;
	}

	for(int i=0;i<N;i++)
		cout << p[i];
	cout << endl;
	
	return 1;
}

int sol(int x) {
	if(x == N) 
		return isSolved();

	for(int i=2;i<=M;i++) {
		p[x] = i;
		if(sol(x + 1))
			return 1;
	}

	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int p = 1; p <= T; p++) {
		cin >> R >> N >> M >> K;
		cout << "Case #" << p << ": " << endl;
		for(;R>0;R--) {
			for(int i=0;i<K;i++) {
				cin >> ps[i];
			}
			sol(0);
		}


	}
}