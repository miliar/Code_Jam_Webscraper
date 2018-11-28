#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX_N = 1007;

int n;
char str[MAX_N];

int main() {
	int T;
	scanf("%d", &T);
	//freopen("b.out", "w", stdout);
	int cas = 0;
	while (T-- > 0) {
		scanf("%d%s", &n, str);
		int peo = 0, ans = 0;
		for (int i = 0; i <= n; ++i) {
            if (peo < i && str[i] != '0') {
                ans += i - peo;
                peo += i - peo;
            }
            peo += str[i] - '0';
		}
		printf("Case #%d: %d\n", ++cas, ans);

	}
	return 0;
}
