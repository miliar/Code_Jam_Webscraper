#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int T, smax, ans, sum;
char s[2000], ch;

int main(int argc, char** argv) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	gets(s);
	
	for (int times = 1; times <= T; times ++) {
		printf("Case #%d: ", times);
		scanf("%d%c", &smax, &ch);
		gets(s);
		ans = 0; sum = 0;
		for (int i = 0; i <= smax; i ++) {
			if (sum < i) {
				ans += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		printf("%d\n", ans);
	}
	return 0;
}

