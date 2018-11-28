#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

#define mem0(x) memset(x, 0, sizeof(x))
#define mem1(x) memset(x, -1, sizeof(x))

ll count(ll num, int x){
	while(num){
		x|=(1<<(num%10));
		num /= 10;
	}
	return x;
};

ll A[1000005];

int main(){
	int t, N, _case = 1;
	int ans = (1<<10)-1;
	for(ll i = 1; i <= 1000005; i++){
		int x = 0;
		ll now = 1;
		while(true){
			x = count(i*now, x);
			if(x==ans) break;
			now++;
		}
		A[i] = now*i;
	}
	scanf("%d", &t);
	while(t--){
		scanf("%d", &N);
		printf("Case #%d: ", _case++);
		if(N==0) puts("INSOMNIA");
		else printf("%lld\n", A[N]);
	}
}
