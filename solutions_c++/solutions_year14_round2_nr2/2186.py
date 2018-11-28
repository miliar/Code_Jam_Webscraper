#include<cstdio>
using namespace std;

int t, cn;

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &t);
	for (cn=1; cn<=t; cn++) {
		int a, b, k;
		scanf("%d%d%d", &a, &b, &k);
		printf("Case #%d: ", cn);
		long long ans = 0;
		for (int i=0; i<a; ++i)
			for (int j=0; j<b; ++j)
				if ((i&j) < k)
					++ans;
		printf("%lld\n", ans);
	}
	return 0;
}