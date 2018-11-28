#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t=0; t<T; ++t) {
		__int64 A;
		int N;
		cin >> A >> N;
		vector<__int64> M(N);
		for (int n=0; n<N; ++n) 
			cin >> M[n];
		sort(M.begin(), M.end());
		if ((1==A) &&(M[N-1]>0)){
			cout << "Case #" << t+1 << ": " << N << endl;
			continue;
		}

		__int64 count = 0;
		__int64 maxcount = N;
		bool flag = true;
		for(int n=0; n<N; ++n) {
			if (A > M[n]) {
				A +=M[n];
			} else {
				maxcount = min(N-n + count, maxcount);
				while (A<= M[n]) {
					A = 2*A-1;
					count++;
				}
				A +=M[n];

			}

		}

		cout << "Case #" << t+1 << ": " << min(maxcount,count) << endl;
		cerr << "Case #" << t+1 << ": " << min(maxcount,count) << endl;
	}
	return 0;
}