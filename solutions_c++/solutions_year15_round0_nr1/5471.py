#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int T, n;
char s[2000];

int main() {
	scanf("%d", &T);

	for(int t = 1; t <= T; t++) {
		scanf("%d ", &n);
		gets(s);

		int curs = 0, ans = 0;

		for(int i = 0; i <= n; i++) {
			if(curs < i) {
				ans +=  i - curs;
				curs = i;
			}

			curs += s[i] - '0';
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}