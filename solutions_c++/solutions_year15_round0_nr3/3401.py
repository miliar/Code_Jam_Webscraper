#include <fstream>

#include <cstdio>
using namespace std;

#define I 2
#define J 3
#define K 4

const int MAX_LEN = 100022;

int M[7][7];
int L[MAX_LEN], R[MAX_LEN];
char s[MAX_LEN];

void initialize() {
	s[0] = ' ';
	
	M[1][1] = 1; M[1][2] = I; M[1][3] = J; M[1][4] = K;
	M[2][1] = I; M[2][2] = -1; M[2][3] = K; M[2][4] = -J;
	M[3][1] = J; M[3][2] = -K; M[3][3] = -1; M[3][4] = I;
	M[4][1] = K; M[4][2] = J; M[4][3] = -I; M[4][4] = -1;
}

inline int getVal(char c) {
	if(c == 'i') {
		return I;
	}
	else if(c == 'j') {
		return J;
	}
	else {
		return K;
	}
}

inline int mult(int x, int y) {
	int s = 0;
	
	if(x < 0) {
		x = -x;
		++s;
	}
	if(y < 0) {
		y = -y;
		++s;
	}

	if(s % 2) {
		s = -1;
	}
	else {
		s = 1;
	}
	
	return s * M[x][y];
}

int main() {
	ifstream f("data.in");
	freopen("data.out", "w", stdout);

	initialize();
	
	int T;
	
	f >> T;
	for(int test = 1; test <= T; ++test) {
		int N, X;

		f >> N >> X;
		f >> (s + 1);
		
		for(int i = 1; i <= X; ++i) {
			for(int j = 1; j <= N; ++j) {
				s[j + i * N] = s[j];
			}
		}

		N *= X;

		L[1] = getVal(s[1]);
		for(int i = 2; i <= N; ++i) {
			L[i] = mult(L[i - 1], getVal(s[i]));			
		}
		
		R[N] = getVal(s[N]);
		for(int i = N - 1; i >= 1; --i) {
			R[i] = mult(getVal(s[i]), R[i + 1]);
		}

		bool haveSol = 0, ok = 0;
		for(int i = 1; i < N; ++i) {
			if(ok && L[i] == K && R[i + 1] == K) {
				haveSol = 1;
			}
			if(L[i] == I) {
				ok = 1;
			}
		}

		if(haveSol) {
			printf("Case #%d: YES\n", test);
		}
		else {
			printf("Case #%d: NO\n", test);
		}
	}

	f.close();
	fclose(stdout);
	
	return 0;
}
