#include <iostream>
#include <cstdlib>

#define N 4

using namespace std;

int main() {

	int T; cin >> T;
	for(int t=0; t<T; ++t) {
		int i, j;
		int a1[N][N], a2[N][N];
		int nummap[N*N+1];
		for(i=0; i<N*N+1; ++i) nummap[i] = 0;

		int r1, r2;
		int count = 0;
		int num;

		cin >> r1;
		for(i=0; i<N; ++i)
			for(j=0; j<N; ++j) {
				cin >> a1[i][j];
			}

		for(i=0; i<N; ++i) {
			nummap[a1[r1-1][i]] = 1;
		}

		cin >> r2;
		for(i=0; i<N; ++i)
			for(j=0; j<N; ++j) {
				cin >> a2[i][j];
			}

		for(i=0; i<N; ++i) {
			nummap[a2[r2-1][i]]++;
		}

		for(i=0; i<N*N+1; ++i)
			if(nummap[i] == 2) { 
				count++;
				num = i;
			}

		cout << "Case #" << t+1 << ": ";
		if(count == 0) cout << "Volunteer cheated!" << endl;
		else if(count == 1) cout << num << endl;
		else cout << "Bad magician!" << endl;
	}
	
	return 0;
}
