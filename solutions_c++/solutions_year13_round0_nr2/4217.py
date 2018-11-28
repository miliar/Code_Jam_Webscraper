#include <iostream>

using namespace std;

int main()
{
	int m;
	int n;
	int arr[105][105];
	int a[105];
	int b[105];
	int i;
	int j;
	int t;
	int k;

	cin >> t;
	k = 1;

	while (k <= t) {
	cin >> m >> n;

	for (i = 0; i < m; i++) {
		a[i] = 0;
	}

	for (i = 0; i < n; i++) {
               	b[i] = 0;
        }

	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			cin >> arr[i][j];
			if (arr[i][j] > a[i]) {
				a[i] = arr[i][j];

			}
		}
	}

	for (i = 0; i < n; i++) {
                for (j = 0; j < m; j++) {
                        if (arr[j][i] > b[i]) {
                               	b[i] = arr[j][i];
                        }
                }
        }

	for (i = 0; i < m; i++) {
                for (j = 0; j < n; j++) {
			if (arr[i][j] < a[i] && arr[i][j] < b[j]) {
				break;
			}
               	}

		if (j < n) {
			break;
		}
        }

	if (i == m) {
		cout << "Case #" << k << ": YES\n";
	} else {
		cout << "Case #" << k << ": NO\n";
	}

	k++;
	}

	return 0;
}
