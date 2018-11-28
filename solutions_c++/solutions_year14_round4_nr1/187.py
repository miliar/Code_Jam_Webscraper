#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define ALL(A) A.begin(), A.end()

int main() {
	int T, te = 1;
	cin >> T;
	while(T--) {
		int N, X;
		cin >> N >> X;
		vector<int> A(N);
		FOR(i,0,N) cin >> A[i];
		sort(ALL(A));
		vector<int> v(N,0);
		int res = N;
		for(int i=N-1;i>=0;i--) if (!v[i]) {
			for(int j=i-1;j>=0;j--) if (!v[j] && A[i]+A[j] <= X) {
				v[j] = 1;
				res--;
				break;
			}
			v[i] = 1;
		}
		cout << "Case #" << te << ": " << res << endl;
		te++;
	}
}