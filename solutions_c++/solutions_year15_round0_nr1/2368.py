#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int T, S;
char str[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d%s", &S, str);

		int cnt = 0, tot = 0;
		for (int i = 0; i <= S; i++) {
			cnt = max(cnt, i) + str[i] - '0';
			tot += str[i] - '0';
		}

		printf("Case #%d: %d\n", test, cnt - tot);
	}
	return 0;
}
