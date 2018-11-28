#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ll;

int main() {
	ll T, r, t, ans;
	scanf("%lld", &T);
	for(int cs = 1; cs <= T; cs++) {
		scanf("%lld%lld", &r, &t);
		ans = 0;
		while(t>0){
			t -= r + r + 1;
			if(t<0){
				break;
			}
			ans ++;
			r+=2;
		}
		printf("Case #%d: %lld\n", cs, ans);
	}
	return 0;
}
