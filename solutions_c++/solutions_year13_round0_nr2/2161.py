#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int t, n, m, i, j, u = 1;
	int maxr[1000];
	int maxc[1000];

	int grass[200][200];
	int a[200][200];


	cin >> t;
	while (t--) {
		cin >> n >> m;
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				cin >> a[i][j];
				grass[i][j] = 100;
			}
		}
		for (i = 0; i < n; i++) {
			maxr[i] = a[i][0];
			for (j = 1; j < m; j++) {
				maxr[i] = max(a[i][j], maxr[i]);
			}
			for (j = 0; j < m; j++) {
				grass[i][j] = min(maxr[i], grass[i][j]);
			}
		}
		for (i = 0; i < m; i++) {
			maxc[i] = a[0][i];
			for (j = 0; j < n; j++) {
				maxc[i] = max(a[j][i], maxc[i]);
			}
			for (j = 0; j < n; j++) {
				grass[j][i] = min(grass[j][i], maxc[i]);
			}
		}
		/*
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				//if (grass[i][j] != a[i][j]) {
				//	break;
				//}
				cout << grass[i][j] << " ";
			}
			cout << endl;
		}*/
		int flag = 0;
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				if (grass[i][j] != a[i][j]) {
				      flag = 1;
				}
		//		cout << a[i][j] << " ";
			}
		//	cout << endl;
		}
		if (flag == 0) {
			cout << "Case #" << u++ << ": YES" << endl;
		} else {
			cout << "Case #" << u++ << ": NO" << endl;
		}
	}
	return 0;
}
