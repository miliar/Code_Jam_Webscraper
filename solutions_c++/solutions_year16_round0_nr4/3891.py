#include<cstdio>
#include<algorithm>

using namespace std;

typedef long long ll;

int main() {
	int TC; scanf("%d", &TC);
	for(int cs=1;cs<=TC;++cs) {
		printf("Case #%d:", cs);
		int K,C,S;
		scanf("%d%d%d",&K,&C,&S);
		if(max(0, K-C)+1 > S) {
			printf(" IMPOSSIBLE\n");
			continue;
		}

		ll s = 0, e = 1;
		int last = -1;
		for(int i=0;i<C;++i) e *= K;
		for(int i=1;i<=K;++i) {
			ll len = (e - s) / K;
			s = (i-1) * len + s;
			e = s + len;

			last = i;

			if(e - s == 1) {
				break;
			}
		}

		for(int i=last;i<=K;++i) {
			printf(" %lld", (s++ +1));
		}

		puts("");
	}
}
