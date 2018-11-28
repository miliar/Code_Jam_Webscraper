#include <iostream>
using namespace std;

int main() {
	int T;
	int a[5][5], b[5][5];
	int p[17];
	cin >> T;
	for (int times = 1; times <= T; times++) {
		int M, N;
		cin >> M;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> a[i][j];
		cin >> N;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> b[i][j];
		for (int i = 1; i <= 16; i++)
			p[i] = false;
		for (int i = 1; i <= 4; i++)
			p[a[M][i]] = true;
		int count = 0;
		int ans = 0;
		cout << "Case #" << times << ": ";
		for (int i = 1; i <= 4; i++) {
			if (p[b[N][i]]) {
				count++;
				ans = b[N][i];
			}
		}
		switch (count) {
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << ans << endl;
				break;
			default:
				cout << "Bad magician!" << endl;
				break;
		}
	}
	return 0;
}