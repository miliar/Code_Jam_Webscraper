#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

char s[1010];
char head[1010], fin[1010];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;

		scanf("%s", s);
		int n = strlen(s);
		head[0] = s[0];
		for (int i = 1; i < n; ++i) {
			if (s[i] > head[i - 1]) {
				head[i] = s[i];
			} else {
				head[i] = head[i - 1];
			}
		}
		int L = 0, R = n - 1;
		for (int i = n - 1; i >= 0; --i) {
			if (s[i] == head[i]) {
				fin[L] = s[i];
				++L;
			} else {
				fin[R] = s[i];
				--R;
			}
		}
		fin[n] = 0;
		puts(fin);
	}
	return 0;
}