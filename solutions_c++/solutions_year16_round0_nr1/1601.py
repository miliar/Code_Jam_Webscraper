#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
long long msk(long long x) {
	int ret = 0;
	while (x) {
		ret |= (1 << (x % 10));
		x /= 10;
	}
	return ret;
}
long long ulmsk = (1 << 10) - 1;
int main() {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &t);
	int cas = 1;
	while (t--) {
		printf("Case #%d: ",cas++);
		int x;
		scanf("%d", &x);
		if (x == 0) {
			puts("INSOMNIA");
			continue;
		}
		int ans = 0;
		long long curmsk = 0;
		long long br = x;
		while (curmsk != ulmsk) {
			++ans;
			curmsk |= msk(br);
		
			ans = ans;
			br += x;
		}
		printf("%lld\n", br-x);
	}
}