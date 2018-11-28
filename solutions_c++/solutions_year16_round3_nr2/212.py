#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		long long B;
		long long M;
		cin >> B >> M;

		long long maxN = (1LL << (B - 2));
		if(M > maxN) {
			cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
		}
		else {
			vector < vector <int> > x(B, vector <int> (B, 0));
			for(int i=1; i<=B-1; i++) {
				for(int j=i+1; j<=B-1; j++) {
					x[i-1][j-1] = 1;
				}
			}
			long long cur = B - 1;
			while(M > 0 && cur >= 1) {
				long long val = (cur == 1 ? 1 : (1LL << (cur - 2)));
				if(M >= val) {
					M -= val;
					x[cur - 1][B - 1] = 1;
				}
				cur--;
			}
			assert(M == 0);
			
			cout << "Case #" << caso << ": POSSIBLE" << endl;
			for(int i=0; i<B; i++) {
				for(int j=0; j<B; j++)
					cout << x[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}