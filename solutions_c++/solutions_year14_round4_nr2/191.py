#include <iostream>
#include <vector>
#include <climits>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

int main() {
	int T, te = 1;
	cin >> T;
	while(T--) {
		int N;
		cin >> N;
		vector<int> A(N);
		FOR(i,0,N) cin >> A[i];
		int res = 0;
		int le = -1, ri = N;
		int done = 0;
		while(!done) {
			//cout << le << " " << ri << endl;
			//FOR(i,0,N) cout << A[i] << " ";
			//cout << endl;
			done = 1;
			int sgn = 0;
			FOR(i,1,N) {
				if (sgn == 0) {
					if (A[i] > A[i-1]) sgn = 1;
					if (A[i] < A[i-1]) sgn = -1;
				} else if (sgn == 1 && A[i] < A[i-1]) {
					sgn = -1;
				} else if (sgn == -1 && A[i] > A[i-1]) {
					done = 0;
					break;
				}
			}
			if (done) break;
			int po = le+1;
			FOR(i,le+1,ri) if (A[i] < A[po]) {
				po = i;
			}
			int dl = po-le-1, dr = ri-po-1;
			//cout << ":" << po << endl;
			//cout << ":" << dl << " " << dr << endl;
			if (dl <= dr) {
				while(dl > 0) {
					swap(A[po],A[po-1]);
					po--;
					res++;
					dl--;
				}
				le++;
			} else {
				while(dr > 0) {
					swap(A[po],A[po+1]);
					po++;
					res++;
					dr--;
				}
				ri--;
			}
		}
		cout << "Case #" << te << ": " << res << endl;
		te++;
	}
	return 0;
}