#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int D = 0;
		vector<int> P;
		cin >> D;
		for (int j = 0; j < D; j++) {
			int Pi = 0;
			cin >> Pi;
			P.push_back(Pi);
		}
		sort(P.begin(), P.end());
		int min = INT_MAX, minSpecials = 0, minPancakes = 0;
		for (int j = 1; j <= P[D-1]; j++) {
			int numSpecials = 0;
			for (int k = D-1; k >= 0; k--) {
				if (P[k] <= j) break;
				numSpecials += ceil((double)P[k]/j)-1;
			}
			if (numSpecials+j < min) {
				min = numSpecials+j;
				minSpecials = numSpecials;
				minPancakes = j;
			}
		}
		cout << "Case #" << i+1 << ": " << minPancakes+minSpecials << endl;
	}
}