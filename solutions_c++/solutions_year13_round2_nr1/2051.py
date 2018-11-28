#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <cmath>
#include <algorithm>
#include <iterator>
using namespace std;

int func(long long A, long long N, vector<int> &motes) {
	sort(motes.begin(), motes.end());
	long long i = 0, cnt = 0, limit = N;
	if (1 == A) {
		return N;	
	}
	while (i < N) {
		while (i < N && A > motes[i]) {
			A += motes[i];
			i++;	
		}
		if (i < N) {
			long long j = 0, B = A;
			while (j < N-i && B <= motes[i]) {
				B += B-1;
				j++;
			}
			if (j == N-i) {
				cnt += N-i;
				return min(cnt, limit);	
			}
			A = B+motes[i];
			cnt += j;
			if (cnt > limit) {
				return limit;
			}
			i++;	
			limit = min(cnt+N-i, limit);		
		}
	}
	return cnt;
}

void solve() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T = 0;
	in >> T;
	for (int t = 1; t <= T; t++) {
		long long A, N;
		in >> A;
		in >> N;
		vector<int> motes(N, 0);
		for (int i = 0; i < N; i++) {
			in >> motes[i];	
		}
		long long res = func(A, N, motes);
		out << "Case #" << t << ": " << res << endl;
		//cout << "Case #" << t << ": " << res << endl;
	}
	in.close();
	out.close();
}

int main() {
	solve();	
	return 0;	
}
