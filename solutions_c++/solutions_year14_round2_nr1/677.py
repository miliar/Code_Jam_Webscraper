#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

int main() {
	char st[101][101];
	char ee[101][101];
	int l[101], num[101][101];
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t) {
		int n;
		cin>>n;
		memset(ee, '.', sizeof(ee));
		for (int i = 0; i < n; ++i) {
			cin>>st[i];
			l[i] = 0;
			int len = strlen(st[i]);
			for (int j = 0; j < len; ++j) {
				if (l[i]) {
					if (st[i][j-1] == st[i][j]) {
						++num[i][l[i]-1];
						continue;
					}
					else {
						ee[i][l[i]] = st[i][j];
						num[i][l[i]] = 1;
						++l[i];
					}
				}
				else {
					++l[i];
					ee[i][0] = st[i][j];
					num[i][0] = 1;
				}
			}
		}
		bool flag = true;
		for (int i = 1; i < n; ++i) {
			for (int j = max(l[i], l[i-1]); j >= 0; j--) {
				if (ee[i][j] != ee[i-1][j]) {
					flag = false;
					break;
				}
			}
		}
		if (!flag) {
			cout<<"Case #"<<t<<": Fegla Won"<<endl;
		}
		else {
			int answ = 0;
			for (int i = 0; i < l[0]; ++i) {
				int ans = 199999999;
				for (int k = 0; k <= num[0][i]; ++k) {
					int sum = 0;
					for (int j = 0; j < n; ++j) {
						sum += abs(k-num[j][i]);
					}
					if (sum < ans) {
						ans = sum;
					}
				}
				answ += ans;
			}
			cout<<"Case #"<<t<<": "<<answ<<endl;
		}
	}
}