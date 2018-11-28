#include <set>
#include <iostream>
#include <vector>

using namespace std;

double A[1024], B[1024], N;

int solve(double *A, double *B) {
	set<double> a;
	set<double>::iterator it;
	register int ret = 0, i;
	for(i = 0; i < N; ++ i) a.insert(A[i]);
	for(i = 0; i < N; ++ i) {
		it = a.lower_bound(B[i]);
		if(it != a.end()) {
			a.erase(it);
			++ ret;
		}
	}
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	register int i;
	for(int t = 1; t <= T; ++ t) {
		cin >> N;
		for(i = 0; i < N; ++ i) cin >> A[i];
		for(i = 0; i < N; ++ i) cin >> B[i];
		cout << "Case #" << t << ": " << solve(A, B) << " " << N - solve(B, A) << endl;
	}
}
