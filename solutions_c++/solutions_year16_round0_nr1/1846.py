#include <bits/stdc++.h>
using namespace std;
#define N 1000010
typedef long long int LL;
bool flag[20];
LL ans[N];
LL preprocess(LL n) {
	int cnt = 0;
	memset(flag, false, sizeof(flag));
	for(LL i=1LL ; ; i++) {
		LL tmp = n * i;
		while( tmp > 0LL ) {
			LL digit = tmp % 10LL;
			if( flag[digit] == false ) {
				flag[digit] = true;
				cnt++;
			}
			tmp /= 10LL;
		}
		if( cnt >= 10 ) return n * i;
	}
}
int main() {
	int T, data;
	for(int i=1 ; i<=1000000 ; i++) ans[i] = preprocess((LL)(i));
	scanf("%d", &T);
	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%d", &data);
		if( data == 0 ) printf("Case #%d: INSOMNIA\n", caso);
		else printf("Case #%d: %d\n", caso, ans[data]);
	}
	return 0;
}