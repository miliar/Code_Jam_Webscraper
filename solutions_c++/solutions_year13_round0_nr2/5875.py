#include <iostream>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
using namespace std;

void tst()
{
	int N,M;
	cin >> N;
	cin >> M;
	int a[100][100];
	int max_row[100];
	int max_col[100];

	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			cin >> a[i][j];
		}
	}

	for (int i=0; i<N; i++) {
		max_row[i] = 0;
	}

	for (int j=0; j<M; j++) {
		max_col[j] = 0;
	}

	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			if (a[i][j] > max_row[i]) {
				max_row[i] = a[i][j];
			}
			if (a[i][j] > max_col[j]) {
				max_col[j] = a[i][j];
			}
		}
	}

	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			if (a[i][j] < max_row[i] && a[i][j] < max_col[j]) {
				cout << "NO";
				return;
			}
		}
	}

	cout << "YES";

	return;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		tst();
		cout << endl;
	}
}



