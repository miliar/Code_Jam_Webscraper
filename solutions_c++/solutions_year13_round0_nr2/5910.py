#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN 128

int A[MAXN][MAXN], B[MAXN][MAXN];
int r[MAXN], c[MAXN];

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int N, M;
		bool result = true;
		cin >> N >> M;
		
		for (int i = 0; i < MAXN; i++)
			r[i] = c[i] = 0;
		
		for (int j = 0; j < N; j++)
			for (int i = 0; i < M; i++){
				cin >> A[i][j];
				B[i][j] = 100;
				r[j] = max(r[j], A[i][j]);
				c[i] = max(c[i], A[i][j]);
			}
		
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				B[i][j] = min(B[i][j], c[i]);

		for (int j = 0; j < N; j++)
			for (int i = 0; i < M; i++)
				B[i][j] = min(B[i][j], r[j]);
		
		for (int j = 0; j < N && result == true; j++)
			for (int i = 0; i < M; i++)
				if (A[i][j] != B[i][j]){
					result = false;
					break;
				}
		
		cout << "Case #" << t << ": " << (result == true ? "YES" : "NO") << endl;
	}
}
