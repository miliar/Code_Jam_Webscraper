#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int T, n;
	char ch[1010];
	scanf("%d", &T);
	for (int it = 1;it <= T; ++it) {
		scanf("%d%s", &n, ch);
		int ret = 0, left = 0;
		for (int i = 0;i <= n; ++i) {
			if (ch[i] != '0') left += ch[i] - '1';
			else {
				if (left) left --;
				else ret ++;
			}
		}
		printf("Case #%d: %d\n", it, ret);
	}
}
