#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
bool visit[10];
void solve(ll x) {
	memset(visit, 0, sizeof(visit));
	int tot = 0;
	for (int i = 1; i <= 20000; ++i) {
		ll s = x * i;
		while (s) {
			int t = s % 10;
			if (!visit[t]) {
				visit[t] = true;
				++tot;
			}
			if (tot == 10) {
				printf("%lld\n", x * i);
				return;
			}
			s /= 10;
		}
	}
	printf("INSOMNIA\n");
}
int main() {
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int T = 0, N;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		scanf("%d", &N);
		solve(N);
	}
}
