#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("file.txt", "w", stdout);
	
	int T;

	cin >> T;

	for (int p = 0; p < T; p++) {
		int a[4][4];
		int b[4][4];

		int x;
		int y;

		cin >> x;

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a[i][j];
			}
		}
	
		cin >> y;
	
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> b[i][j];
			}
		}
	
		vector<int> v;
	
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if(a[x - 1][j] == b[y - 1][k]) {
					v.push_back(a[x - 1][j]);
				}
			}
		}
		
		cout << "Case #" << p + 1 << ": ";
		if (v.size() == 1) {
			cout << v[0] << endl;
		} else if (v.size() > 1) {
			cout << "Bad magician!" << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}
	
	return 0;
}


