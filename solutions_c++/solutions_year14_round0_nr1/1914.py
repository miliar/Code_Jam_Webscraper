#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("1out.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int testc = 1; testc <= tc; testc++) {
		int r1;
		cin >> r1;
		r1--;
		int last[4];
		for (int i =0 ; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int temp;
				if (i != r1) {
					scanf("%d", &temp);
				}
				else {
					scanf("%d", &temp);
					last[j] = temp;
				}
			}
		}
		bool found = false;
		bool duplicate = false;
		int value = 1000000;
		int r2;
		cin >> r2;
		r2--;
		for (int i =0 ; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int temp;
				if (i != r2) {
					scanf("%d", &temp);
				}
				else {
					scanf("%d", &temp);
					for (int k = 0 ; k < 4; k++) {
						if (temp == last[k]) {
							if (found) duplicate = true;
							found = true;
							value = temp;
						}
					}
				}
			}
		}
		if (duplicate) printf("Case #%d: Bad Magician!\n", testc);
		else if (found) printf("Case #%d: %d\n", testc, value);
		else printf("Case #%d: Volunteer Cheated!\n", testc);
	}
}
