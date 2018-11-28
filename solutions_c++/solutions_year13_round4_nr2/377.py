#include<stdio.h>
typedef long long lld;

lld shl(lld n){
	return 1LL << n;
}

bool judge1(lld i, lld p, lld n){
	if (p + 1 == shl(n)) return true;
	if (i == 0) return true;
	if ((p >> (n-1)) == 0) return false;
	return judge1((i-1)/2, p-(shl(n-1)), n-1);
}

/*
lld gao1(lld p, lld n){
	int ans = 0;
	for (lld i=0; i<=p; ++i){
		if (judge1(i, p, n)) ans = i;
		else break;
	}
	return ans;
}
*/

lld gao1(lld p, lld n){
	lld l = 0, r = shl(n) - 1;
	lld ans = 0;
	while (l <= r){
		lld mid = (l + r) / 2;
		if (judge1(mid, p, n)){
			ans = mid;
			l = mid + 1;
		}else{
			r = mid - 1;
		}
	}
	return ans;
}

bool judge2(lld i, lld p, lld n){
	if (p+1 == shl(n)) return true;
	if (i == shl(n) - 1) return false;
	if (p >> (n-1)) return true;
	return judge2((i+1)/2, p, n-1);
}
lld gao2(lld p, lld n){
	lld l = 0, r = shl(n) - 1;
	lld ans = 0;
	while (l <= r){
		lld mid = (l + r) / 2;
		if (judge2(mid, p, n)){
			ans = mid;
			l = mid + 1;
		}else{
			r = mid - 1;
		}
	}
	return ans;
}

int main(){
	lld t, p, n;
	scanf("%lld", &t);
	for (int I=1; I<=t; ++I){
		scanf("%lld %lld", &n, &p);
		p --;
		printf("Case #%d: %lld %lld\n", I, gao1(p, n), gao2(p, n));
	}
	return 0;
}
