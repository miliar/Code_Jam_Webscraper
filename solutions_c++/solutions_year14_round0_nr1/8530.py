#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin>>T;
	for (int t=1;t<=T;++t) {
		int a, b;
		int v;
		cin>>a;
		bool possible[16];
		memset(possible, -1, sizeof(possible));


		for (int r=0;r<4;r++) {
			for (int c=0;c<4;++c) {
				cin>>v;
				if (r != a - 1) {
					possible[v - 1] = false;
				}
			}
		}
		cin>>b;
		for (int r=0;r<4;r++) {
			for (int c=0;c<4;++c) {
				cin>>v;
				if (r != b - 1) {
					possible[v - 1] = false;
				}
			}
		}

		vector<int> ans;
		for (int i=0;i<16;++i) {
			if (possible[i]) {
				ans.push_back(i + 1);
			}
		}

		cout << "Case #" << t << ": ";
		if (ans.size() == 0) {
			cout << "Volunteer cheated!";
		} else if (ans.size() == 1) {
			cout << ans[0];
		} else {
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}
