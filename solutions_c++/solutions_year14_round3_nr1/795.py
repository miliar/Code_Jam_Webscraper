#include <cstdio>
using namespace std;

typedef long long ll;

int n;
ll a, b;
char c;

ll nwd(ll a, ll b) {
	return (b==0)?a:nwd(b, a%b);
}

int main() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		scanf("%lld%c%lld", &a, &c, &b);
		ll gcd = nwd(a, b);
		a/=gcd;
		b/=gcd;
		if(b&(b-1)) {
			printf("Case #%d: impossible\n", i);
			continue;
		}
		int res=0;
		while(a<b) {
			res++;
			a*=2ll;
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
