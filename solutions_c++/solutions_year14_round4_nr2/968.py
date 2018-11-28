#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int ts=1; ts<=T; ++ts) {
		int N;
		cin >> N;
		vector<int> A(N);
		for (size_t i=0; i<N; ++i)
			cin >> A[i];
		int l=0;
		int r=N-1;
		int ans=0;
		while (l<r) {
			int midx = l;
			for (int i=l; i<=r; ++i)
				if (A[i] < A[midx])
					midx = i;
			if (midx-l<r-midx) {
				for (int i=midx; i>l; --i) {
					swap(A[i], A[i-1]);
					++ans;
				}
				++l;
			}
			else {
				for (int i=midx; i<r; ++i) {
					swap(A[i], A[i+1]);
					++ans;
				}
				--r;
			}
		}
		cout << "Case #" << ts << ": " << ans << endl;
	}

	return 0;
}
