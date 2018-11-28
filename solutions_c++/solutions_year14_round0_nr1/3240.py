#include <iostream>
#include <cstring>
using namespace std;

bool flag[20], ff;
int T, row1, row2, tmp, ans;

int main() {
	int cas = 0;
	cin >> T;
	while (T --) {
		memset(flag, 0, sizeof(flag));
		ff = 0;
		ans = 0;
		cin >> row1;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++) {
				cin >> tmp;
				if (i == row1 - 1) flag[tmp] = 1;
			}
		cin >> row2;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++) {
				cin >> tmp;
				if (i == row2 - 1 && flag[tmp]) {
					if (ans == 0) ans = tmp;
					else ans = -1;
				}
			}
		cout << "Case #" << ++cas << ": ";
		switch(ans) {
			case -1:
				cout << "Bad magician!";
				break;
			case 0:
				cout << "Volunteer cheated!";
				break;
			default:
				cout << ans;
		}
		cout << endl;
	}
	return 0;
}
