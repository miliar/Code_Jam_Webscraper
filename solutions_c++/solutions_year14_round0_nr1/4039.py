#include <iostream>
#include <cstring>

using namespace std;

void test();

int main() {
	int T;

	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		test();
	}
}

void test() {
	int possible[17];
	memset(possible, 0,sizeof(possible));

	int row, x;
	
	for(int t = 0; t < 2; t++) {
		cin >> row;

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> x;
				if(i + 1 == row) {
					possible[x]++; 
				}
			}
		}
	}

	int ans = -1;
	for(int i = 1; i <= 16; i++) {
		if(possible[i] == 2) {
			if(ans == -1) {
				ans = i;
			} else {
				cout << "Bad magician!\n";
				return;
			}
		}
	}

	if(ans == -1) {
		cout << "Volunteer cheated!\n";
	} else {
		cout << ans << '\n';
	}
}