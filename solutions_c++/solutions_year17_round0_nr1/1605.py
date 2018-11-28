#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 1005;

char s[N];

int k;

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		scanf("%s%d", s, &k);
		int n = strlen(s);
		bool valid = true;
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (s[i] == '-') {
				if (i + k > n) {
					valid = false;
					break;
				} else {
					++ans;
					for (int j = 0; j < k; ++j) {
						s[i + j] = '+' + '-' - s[i + j];
					}
				}
			}
		}
		printf("Case #%d: ", ++id);	
		if (valid) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
