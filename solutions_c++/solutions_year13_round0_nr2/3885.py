#include <iostream>
#include <string>
using namespace std;

inline int max(int a, int b) { return a>b?a:b; }

int T, N, M;
int I, R;

int* pattern = nullptr;
const string outcomes[2] = {"NO", "YES"};

inline int max_row(int i0, int j0) {
	int m = 0;
	int j;
	for (j = 0; j<M; j++) {
		if (j==j0) continue;
		m = max(pattern[i0*M+j], m);
	}
	return m;
}

inline int max_col(int i0, int j0) {
	int m = 0;
	int i;
	for (i = 0; i<N; i++) {
		if (i==i0) continue;
		m = max(pattern[i*M+j0], m);
	}
	return m;
}

bool possible() {
	bool res;
	int i, j;
	int v, mr, mc;
	for (i = 0; i<N; i++) {
		for (j = 0; j<M; j++) {
			v = pattern[i*M+j];
			mr = max_row(i, j);
			mc = max_col(i, j);
			res = mr <=v || mc<=v;
			if (!res) return false;
		}
	}
	return true;
}

void print() {
	cout << "Case #" << (I+1) << ": " << outcomes[R] << endl;
}

void read() {
	cin >> N >> M;
	pattern = new int[N * M];
	for (int i = 0; i < N*M; i++) {
		cin >> pattern[i];
	}
}


void solve() {
	R = possible()?1:0;
	delete [] pattern;
}

void main() {
	cin >> T;
	for (I = 0; I < T; I++) {
		read();
		solve();
		print();
	}
}