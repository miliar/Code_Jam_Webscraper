#include <bits/stdc++.h>
using namespace std;
long long tcs, d, p[1050], ans, ct, mh;
int main(){
	scanf("%lld", &tcs);
	for(long long tc=1;tc<=tcs;tc++){
		scanf("%lld", &d);
		mh = 0;
		ans = 1LL<<60;
		for(long long i=0;i<d;i++){
			scanf("%lld", &p[i]);
			mh = max(mh, p[i]);
		}
		for(long long i=1;i<=mh;i++){
			ct = i;
			for(long long k=0;k<d;k++){
				ct += ceil(p[k] / (double)i) - 1;
			}
			ans = min(ans, ct);
		}
		printf("Case #%lld: %lld\n", tc, ans);
	}
}