#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	int t;
	
	cin >> t;
	for (int s = 1; s <= t; s++) {
		int a1, a2, n = 0, res = 0;
		int m1[4], m2[4];
		
		cin >> a1;
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == a1 - 1) {
					cin >> m1[j];
				} else {
					int tmp;
					cin >> tmp;
				}
			}
		}
		
		cin >> a2;
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == a2 - 1) {
					cin >> m2[j];
				} else {
					int tmp;
					cin >> tmp;
				}
			}
		}
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (m1[i] == m2[j]) {
					n++;
					if (n == 1) {
						res = m1[i];
					}
				}
			}
		}
		
		if (n == 1) {
			cout << "Case #" << s << ": " << res << endl;
		} else if (n > 1) {
			cout << "Case #" << s << ": " << "Bad magician!" << endl;
		} else if (n == 0) {
			cout << "Case #" << s << ": " << "Volunteer cheated!" << endl;
		}
	}
	
	return 0;
}
