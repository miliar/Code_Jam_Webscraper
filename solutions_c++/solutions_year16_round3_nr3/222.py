#include <iostream>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

vector < vector <int> > best;
int maxN;

int J, P, S, K;

int C[4 * 4 * 4];

int sz, M[4 * 4 * 4][3];

void backtrack(int a, int b, int c) {
	if(sz > maxN) {
		best.resize(sz);
		for(int i=0; i<sz; i++) {
			best[i].clear();
			best[i].push_back(M[i][0]);
			best[i].push_back(M[i][1]);
			best[i].push_back(M[i][2]);
		}
		maxN = sz;
	}

	if(c > S) {
		backtrack(a, b + 1, 1);
		return;
	}
	if(b > P) {
		backtrack(a + 1, 1, 1);
		return;
	}
	if(a > J) {
		return;
	}

	backtrack(a, b, c + 1);

	int n12 = a * 4 * 4 + b * 4;
	int n13 = a * 4 * 4 + c;
	int n23 = b * 4 + c;
	if(C[n12] < K && C[n13] < K && C[n23] < K) {
		C[n12]++;
		C[n13]++;
		C[n23]++;
		M[sz][0] = a; M[sz][1] = b; M[sz][2] = c;
		sz++;
		backtrack(a, b, c + 1);
		sz--;
		C[n12]--;
		C[n13]--;
		C[n23]--;
	}
}

int main() {
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		cin >> J >> P >> S >> K;

		maxN = 0;
		best.clear();
		memset(C, 0, sizeof(C));
		sz = 0;
		backtrack(1, 1, 1);

		cout << "Case #" << caso << ": " << best.size() << endl;
		for(int i=0; i<best.size(); i++) {
			cout << best[i][0] << " " << best[i][1] << " " << best[i][2] << endl;
		}
	}
	return 0;
}