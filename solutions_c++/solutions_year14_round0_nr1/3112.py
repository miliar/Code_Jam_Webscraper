#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++ i) {
		cout << endl;
		int ans1, ans2;
		int t1[4][4], t2[4][4];
		cin >> ans1;
		for(int j = 0; j < 16; ++ j)
			cin >> t1[j / 4][j % 4];
		cin >> ans2;
		for(int j = 0; j < 16; ++ j)
			cin >> t2[j / 4][j % 4];
		int sum = 0, ans = -1;
		for(int j = 0; j < 4; ++ j) 
			for(int k = 0; k < 4; ++ k)
				if(t1[ans1 - 1][j] == t2[ans2 - 1][k]) {
					++ sum;
					ans = t1[ans1 - 1][j];
				}
		cout <<	"Case #" << i + 1 << ": ";
		if(sum == 0) {
			cout << "Volunteer cheated!" << endl;
		}
		else if(sum == 1) {
			cout << ans << endl;
		}
		else 
			cout << "Bad magician!" << endl;
	}
}