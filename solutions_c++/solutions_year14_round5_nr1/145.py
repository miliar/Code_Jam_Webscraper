#include <iostream>
#include <iomanip>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

long long A[1<<20], S[1<<20];

void do_case(int case_no) {
	int N;
	int p, q, r, s;
	cin >> N >> p >> q >> r >> s;
	FOR(i,0,N) {
		long long ii = i;
		A[i] = (ii * p + q)%r + s;
		S[i] = A[i];
		if (i) S[i] += S[i-1];
	}
	long long be = 0;
	FOR(i,0,N) {
		long long s1 = S[i], s2 = S[N-1]-S[i];
		long long my = min(s1,s2);
		be = max(be,my);
	}
	if (N <= 2) {
		cout << "Case #" << case_no << ": " << fixed << setprecision(12) << (double)be/S[N-1] << endl;
		return;
	}
	long long lo = 0, hi = 1000000000000000ll;
	while(lo < hi) {
		long long mid = (lo + hi) / 2;
		int le = -1, ri = N;
		FOR(i,0,N-1) if (S[i] <= mid) le = i;
		for(int i=N-1;i>=1;i--) if (S[N-1]-S[i-1] <= mid) ri = i;
		bool f = false;
		if (le == -1 || ri == N) {
			lo = mid+1;
			continue;
		}
		if (le >= ri-1) {
			hi = mid;
			continue;
		}
		if (S[ri-1] - S[le] <= mid) {
			hi = mid;
		} else {
			lo = mid + 1;
		}
	}
	cout << "Case #" << case_no << ": " << fixed << setprecision(12) << 1.0 - (double)lo/S[N-1] << endl;
}

int main() {
	int T, te = 1;
	cin >> T;
	while(T) {
		do_case(te);
		T--;
		te++;
	}
	return 0;
}