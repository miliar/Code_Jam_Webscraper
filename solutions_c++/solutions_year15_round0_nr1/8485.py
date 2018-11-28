#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

char s[1001];

int main () {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int test, cnt = 0;
	scanf("%d", &test);

	while (test--) {
		cnt++;
		int n;
		scanf("%d ", &n);
		gets(s);
		int res = 0;

		int stood_up = 1;

		int len = strlen(s);
		if (s[0] == '0') {
			res = 1;
			s[0] = '1';
		} else {
			stood_up = s[0] - '0';
		}
		for (int i = 1; i < len; i++) {
			int cur_num = s[i] - '0';
			if (stood_up >= i)
				stood_up += cur_num;
			else {
				res += (i - stood_up);
				stood_up += (i - stood_up) + cur_num;
			}
		}
		printf("Case #%d: %d", cnt, res);
		if (test > 0)
			puts("");
	}	

	return 0;
}