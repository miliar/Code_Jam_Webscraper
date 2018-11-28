#include <iostream>
#include <vector>

using namespace std;

typedef vector< vector<int> > Matrix;

Matrix read(int n, int m) {
	Matrix M(n, vector<int>(n));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) cin >> M[i][j];		
	}
	return M;
}

int main() {
	int T;
	cin >> T;
	int n = 4;
	
	Matrix M(n, vector<int>(n));
	
	for (int i = 1; i <= T; ++i) {
		int f; // first
		cin >> f;
		f = f-1;
		M = read(n, n);
		
		vector <int> F(n);
		for (int j = 0; j < n; ++j) {
			F[j] = M[f][j];
		}
		
		int s; // second
		cin >> s;
		s = s-1;
		M = read(n, n);
		
		vector <int> S(n);
				
		for (int j = 0; j < n; ++j) {
			S[j] = M[s][j];
		}
		
		int a = 0;
		int m = 0;
		
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < n; ++k) {
				if (F[j] == S[k]) {
					a = F[j];
					++m;
				}
			}
		}
		
		cout << "Case #" << i << ": ";
		if (m == 0) cout << "Volunteer cheated!";
		if (m == 1) cout << a;
		if (m > 1) cout << "Bad magician!";
		cout << endl;
	}
	
	
	
}
