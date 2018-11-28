#include <iostream>

using namespace std;

int main() {
	int t,T;
	bool possible;

	int a[100][100];
	int n,m;
	const int H = 100;
	int h,i,j;

	bool skipHLines[100];
	bool skipVLines[100];

	cin >> T;
	for (t = 0; t < T; t++) {
		cin >> n >> m;
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				cin >> a[i][j];
			}
		}

		for (i = 0; i < n; i++) {
			skipHLines[i] = false;
		}

		for (j = 0; j < m; j++) {
			skipVLines[j] = false;
		}

		possible = true;

		for (h = 1; h < H; h++) {
			
			bool fullYet;
			bool emptyYet;

			// check for horizontal lines
			for (i = 0; i < n; i++) {
				if (!skipHLines[i]) {
					fullYet = true;
					for (j = 0; j < m; j++) {
						if (!skipVLines[j]) {
							if (a[i][j] > h) {
								fullYet = false;
							}
						}
					}
					if (fullYet) {
						skipHLines[i] = true;
					}
				}
			}

			// check for vertical lines and catch exceptions
			for (j = 0; j < m; j++) {
				if (!skipVLines[j]) {
					fullYet = true;
					emptyYet = true;
					for (i = 0; i < n; i++) {
						if (!skipHLines[i]) {
							if (a[i][j] > h) {
								fullYet = false;
							} else {
								emptyYet = false;
							}
						}
					}
					if (fullYet) {
						skipVLines[i] = true;
					} else if (!emptyYet) {
						possible = false;
					}
				}
			}
		}

		cout << "Case #" << (t+1) << ": " << (possible?"YES":"NO") << "\n";
	}
	
	return 0;
}