#include<cassert>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int n;

int a[3];

const char ch[4] = "RPS";

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		scanf("%d", &n);
		for (int i = 0; i < 3; ++i) {
			scanf("%d", a + i);
		}
		bool flag = false;
		for (int i = 0; i < 3; ++i) {
			int b[3] = {0, 0, 0};
			b[i] = 1;
			for (int j = 0; j < n; ++j) {
				int nb[3] = {b[0] + b[1], b[1] + b[2], b[2] + b[0]};
				b[0] = nb[0], b[1] = nb[1], b[2] = nb[2];
			}
			if (a[0] == b[0] && a[1] == b[1] && a[2] == b[2]) {
				string ans = "";
				ans += ch[i];
				for (int j = 0; j < n; ++j) {
					string nans = "";
					for (int k = 0; k < (int)ans.size(); ++k) {
						if (ans[k] == 'R') {
							nans += "RS";
						} else if (ans[k] == 'P') {
							nans += "PR";
						} else {
							nans += "SP";
						}
					}
					ans = nans;
				}
				for (int i = 1; i <= n; ++i) {
					for (int j = 0; j < (int)ans.size(); j += (1 << i)) {
						bool flag = false;
						for (int k = 0; k < (1 << (i - 1)); ++k) {
							if (ans[j + k] != ans[j + (1 << (i - 1)) + k]) {
								if (ans[j + k] > ans[j + (1 << (i - 1)) + k]) {
									flag = true;
								}
								break;
							}
						}
						if (flag) {
							for (int k = 0; k < (1 << (i - 1)); ++k) {
								swap(ans[j + k], ans[j + (1 << (i - 1)) + k]);
							}
						}
					}
				}
				for (int k = 0; k < (int)ans.size(); ++k) {
					if (ans[k] == 'R') {
						--a[0];
					} else if (ans[k] == 'P') {
						--a[1];
					} else {
						--a[2];
					}
				}
				assert(!a[0] && !a[1] && !a[2]);
				printf("%s\n", ans.c_str());
				flag = true;
				break;
			}
		}
		if (!flag) {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
