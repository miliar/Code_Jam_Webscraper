#include <iostream>
#include <string>
#include <vector>

using namespace std;
int A[100][100];
int a[100], b[100];

int main()
{
    int T,N,M;
    cin >> T;
    for (int i=1; i<=T; i++) {
	cin >> N >> M;
	for (int j=0; j<N; j++) {
	    a[j] = 0;
	    for (int k=0; k<M; k++) {
		cin >> A[j][k];
		if (A[j][k] > a[j]) a[j] = A[j][k];
	    }
	}
	for (int j=0; j<M; j++) {
	    b[j] = 0;
	    for (int k=0; k<N; k++) {
		if (A[k][j] > b[j]) b[j] = A[k][j];
	    }
	}
	bool possible = true;
	for (int j=0; j<N; j++) {
	    for (int k=0; k<M; k++) {
		if (A[j][k] < a[j] && A[j][k] < b[k]) {
		    possible = false;
		    break;
		}
	    }
	}
	if (possible) cout << "Case #" << i << ": YES" << endl;
	else cout << "Case #" << i << ": NO" << endl;
    }
    return 0;
}
