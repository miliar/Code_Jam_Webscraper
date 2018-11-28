#include <iostream>
using namespace std;

int main(){

	int T;

	int N;
	int M[10000];
	int r1, r2;
	int max;

	cin >> T;

	for (int i = 1; i <= T; i++){
		r1 = 0; r2 = 0;
		max = 0;
		cin >> N;

		cin >> M[0];
		for (int j = 1; j < N; j++){
			cin >> M[j];
			if (M[j] < M[j - 1]) r1 += M[j - 1] - M[j];
		}

		for (int j = 1; j < N; j++){
			if (M[j] < M[j - 1]){
				if (max < M[j - 1] - M[j]) max = M[j - 1] - M[j];
			}
		}
		for (int j = 0; j < N-1; j++){
			if (M[j] > max) r2 += max;
			else r2 += M[j];
		}
		
		
		cout << "Case #" << i << ": " << r1 << " " << r2 << endl;
		
	}
	


	return 0;
}