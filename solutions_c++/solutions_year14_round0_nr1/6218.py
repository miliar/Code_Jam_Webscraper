#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int t;
	cin>>t;
	for (int l = 1; l <= t; ++l) {
		int n, f[5][5];
		cin>>n;
		--n;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0 ; j < 4; ++j) {
				cin>>f[i][j];
			}
		}
		int m, g[5][5];
		bool flag_same = true;
		cin>>m;
		--m;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0 ; j < 4; ++j) {
				cin>>g[i][j];
				if (g[i][j] != f[i][j]) {
					flag_same = false;
				}
			}
		}
		if (flag_same) {
			if (m == n) {
				cout<<"Case #"<<l<<": Bad magician!"<<endl;
			}
			else {
				cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
			}
		}
		else {
			bool flag[20], flag_end = false, bad_game = false;
			int ans;
			memset(flag, false, sizeof(flag));
			for (int i = 0; i < 4; ++i) {
				flag[f[n][i]] = true;
			}
			for (int i = 0; i < 4; ++i) {
				if (flag[g[m][i]]) {
					if (!flag_end) {
						flag_end = true;
						ans = g[m][i];
					}
					else {
						bad_game = true;
					}
				}
			}
			if (bad_game) {
				cout<<"Case #"<<l<<": Bad magician!"<<endl;
			}
			else {
				if (flag_end) {
					cout<<"Case #"<<l<<": "<<ans<<endl;
				}
				else {
					cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
				}
			}
		}
	}
}