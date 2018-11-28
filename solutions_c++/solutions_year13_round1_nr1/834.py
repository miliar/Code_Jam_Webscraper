#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<cstring>
#include<cmath>

#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		long long r,t;
		scanf("%lld %lld",&r,&t);
		int cnt=0;
		while(1){
			t -= 2LL*r+1LL;
			if(t< 0LL) {
				break;
			}
			cnt++;
			r+=2LL;
		}
		printf("Case #%d: %d\n",caso,cnt);
	}
	return 0;
}
