#include<cstdio>
#include<algorithm>

#define N 1005

using namespace std;

int main() {
	int tc, tci;
	scanf("%d", &tc);
	while(tc--){
		tci++;
		int n, ans = 0;
		char str[N];
		scanf("%d %s", &n, str);
		int cnt = 0;
		for (int i = 0; i <= n; i++) {
			if (i > cnt) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += str[i]-'0';
		}
		printf("Case #%d: %d\n", tci, ans);
	}
	return 0;
}
