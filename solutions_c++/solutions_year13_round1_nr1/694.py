#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#define INF 0x7f7f7f7f

using namespace std;

int main(){
	int T;
	long long r,t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		scanf("%lld %lld",&r,&t);
		long long ans = 0;
		long long low,up;
		r = 2 * r + 1;
		low = 0;
		up = t + 1;
		while(low < up - 1){
			ans = (low + up)/2;
			if(r + 2 * ans <= t /(ans + 1)){
				low  = ans;
			}else{
				up = ans;
			}
		}
		ans = low + 1;
		printf("Case #%d: %lld\n",cas,ans);

	}
	return 0;
}