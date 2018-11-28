#include <iostream>
using namespace std;

void solve(int smax, char str[]) {
	int ans = 0, cnt = 0;
	for(int i = 0; i <= smax; ++i) {
		if(str[i] == '0') continue;
		if(i > cnt) {
			ans += (i - cnt);	
			cnt += (i - cnt);
		}
		cnt += (str[i] - '0');
	}
	printf("%d\n", ans);
}

int main() {
	freopen("c:/A-large.in", "r", stdin);
	freopen("c:/A-large.out", "w", stdout);
	int T;
	int smax;
	char str[1010];
	scanf("%d", &T);
	for(int ca = 0; ca < T; ++ca) {
		printf("Case #%d: ", ca + 1);
		scanf("%d %s", &smax, str);
		solve(smax, str);
	}
	return 0;
}