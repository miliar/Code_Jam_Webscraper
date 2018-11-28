/**
 * Created by zh0ng.
 */
#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int a[11] = {0};
void seta(int x){
	while(x) {
		a[x%10]  =1;
		x/=10;
	}
}

bool check() {
	for(int i=0;i<=9;i++) {
		if(!a[i])
			return false;
	}
	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int cas = 1;cas<=T;cas++){
        int x;
        cin >> x;
        if(x == 0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
        }
        memset(a, 0, sizeof a);
        int cur = x;
        for(;!check();cur +=x){
			seta(cur);
        }
        printf("Case #%d: %d\n", cas, cur - x);
	}

	return 0;
}
