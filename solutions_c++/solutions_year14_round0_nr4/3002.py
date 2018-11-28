
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		vector<double> A, B;
		for (int i = 0; i < N; i++) {
			double v; cin >> v;
			A.push_back(v);
		}
		for (int i = 0; i < N; i++) {
			double v; cin >> v;
			B.push_back(v);
		}
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		int cntB = 0;
		int j = 0;
		for (int i = 0; i < A.size(); i++) {
			while (j < B.size()) {
				if (A[i] < B[j]) {
					cntB++;
					j++;
					break;
				}
				j++;
			}
		}
		int cntA = 0;
		while (A.size() > 0) {
			double ele = A[0];
			bool smallest = true;
			for (int i = 0; i < B.size(); i++) {
				if (ele > B[i]) {
					smallest = false;
					break;
				}
			}
			if (smallest) {
				A.erase(A.begin());
				B.erase(B.begin()+B.size()-1);
				continue;
			}
			cntA++;
			// say you have highest -> enforce lowest
			A.erase(A.begin());
			B.erase(B.begin());
		}
		cout << "Case #" << t << ": " << cntA << " " << N-cntB << endl;
	}
	return 0;
}
