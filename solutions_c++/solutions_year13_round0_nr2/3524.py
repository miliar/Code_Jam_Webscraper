#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;
	int N, M;
	
	for (int t=0; t<T; t++) {
		cin >> N >> M;
		
		int field[128][128];
		bool ff[128][128];
		for (int n = 0; n<N ; n++) {
			for (int m = 0; m<M ; m++) {
				cin >> field[n][m];
				ff[n][m] = false;
			}
		}

		int c = 0;
		for (int n = 0; n<N ; n++) {
			int maxh = 0;
			for (int m = 0; m<M ; m++) {
				if (field[n][m] > maxh ) {
					maxh = field[n][m];
				}
			}
			for (int m = 0; m<M ; m++) {
				if (field[n][m] == maxh && !ff[n][m]) {
					ff[n][m] = true;
					c++;
				}
			}
		}

		for (int m = 0; m<M ; m++) {
			int maxh = 0;
			for (int n = 0; n<N ; n++) {
				if (field[n][m] > maxh ) {
					maxh = field[n][m];
				}
			}
			for (int n = 0; n<N ; n++) {
				if (field[n][m] == maxh && !ff[n][m]) {
					ff[n][m] = true;
					c++;
				}
			}
		}


		bool r = c == N*M;
		cout << "Case #" << (t+1) << ": " << (r?"YES":"NO") << endl;
	
	}

	return 0;
}


