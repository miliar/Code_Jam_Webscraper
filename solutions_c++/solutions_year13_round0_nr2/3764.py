#include <iostream>

using namespace std;

int main()
{
	int numCase;
	cin >> numCase;
	int M,N;

	for (int num = 0; num < numCase; num++)
	{

		// Read dimensions
		cin >> M;
		cin >> N;
		
		// Create matrix
		int arr[M][N];
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
		    	cin >> arr[i][j];
			}
		}
		
		bool possible=1;
		for(int i=0;(i<M && possible==1);i++) {
			for(int j=0;(j<N && possible==1);j++) {
				// Find a row or a column containing (i,j) such that arr[i][j]
				// is the largest length, if this is not possible the lawn can't
				// be cut in the proposed way. This is true since we start with the largest
				// length and work our way down and since we must enter on a row or col.
				int cutRow=1,cutCol=1;
				for(int k=0;k<M;k++) { // Row
					if(arr[k][j]>arr[i][j]) {cutRow=0; break;}
				}
				for(int k=0;k<N;k++) { // Col
					if(arr[i][k]>arr[i][j]) {cutCol=0; break;}
				}
				if(cutRow==0 && cutCol==0) { // Not possible so we can jump out of the for-loop
					possible=0;
				}
			}
		}
		
		// Print outcome
		cout << "Case #" << (num+1) << ": ";
		if(possible==1) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}
	return 0;
}