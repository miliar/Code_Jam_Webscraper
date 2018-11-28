#include<cstdio>
#include<string>
#include<set>
using namespace std;
typedef long long ll;
ll pals[16384];
int np = 0;
int ispal(ll x) {
	char buff[32];
	sprintf(buff,"%lld", x);
	int len = strlen(buff);
	for(int i = 0; i < len; ++i) {
		if(buff[i] != buff[len-1-i]) {
			return 0;
		}
	}
	return 1;
}
void pre() {
	for(ll i = 1; i <= 10000000; ++i)
		if(ispal(i) && ispal(i*i)) {
			pals[np++] = i*i;
		}
//	printf("np = %d\n", np);
}
ll doit(ll x) {
	ll cnt = 0;
	for(int i = 0 ; i<np;++i) {
		if(pals[i] <= x) cnt++;
		else break;
	}
	return cnt;
	/*
	int l = 0, r = np-1;
	while(l <= r) {
		int m = (l+r)/2;
		if(pals[m] < x) r = m - 1;
		else l = m + 1; 
	}
	return l;
	*/
}
int main() {
	pre();
	int e = 0, T;
	scanf("%d",&T);
	ll A,B;
	while(T--) {
		scanf("%lld%lld",&A,&B);
		ll ans = 0, v1, v2;
		v1 = doit(B);
		v2 = doit(A-1);
		ans = v1 - v2;
		printf("Case #%d: %lld\n", ++e, ans);
	}
	return 0;
}
