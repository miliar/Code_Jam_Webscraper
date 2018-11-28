#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <(b); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
typedef long long ll;
ll K,C,S;
int main() {
	int T, e=0;
	scanf("%d",&T);
	while(T--) {
		scanf("%lld%lld%lld",&K,&C,&S);
		printf("Case #%d:", ++e);
		if(K != S) printf(" IMPOSSIBLE\n");
		else {
			ll offset = 1;
			FOR(i,1,C) 
				offset *= K;
			ll x = 1;
			FOR(i,0,S) {
				printf(" %lld", x);
				x += offset;
			}
			printf("\n");
		}
	}
	return 0;
}
