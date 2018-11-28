#define ll long long
#include <iostream>
#include <math.h>
using namespace std;
ll a, b;

int getrev(int x){
	int res=0, tmp = 1;
	while (x > 0){
		res += tmp * (x % 10);
		x /= 10;
		tmp *= 10;
	}
	return res;
}

int mergerev(int x){
	int res = x * 10;
	if (x > 10) res *= 10;
	if (x > 100) res *= 10;
	res += getrev(x);
	return res;
}

int mergerev(int x, int m){
	int res = x * 10 + m;
	res *= 10;
	if (x > 10) res *= 10;
	if (x > 100) res *= 10;
	res += getrev(x);
	return res;
}

bool isRev(ll x){
	int sx[20], cnt = 0;
	while (x>0){
		sx[cnt++] = x % 10;
		x /= 10ll;
	}
	int l = 0, r = cnt-1;
	while (l < r){
		if (sx[l] != sx[r]) return false;
		l++; r--;
	}
	return true;
}

int find(){
	int res = 0;
	ll sa = sqrt(a), sb = sqrt(b);
	if (sa * sa < a) sa++;
	if (sa <= 1ll && sb >= 1ll) res++;
	if (sa <= 2ll && sb >= 2ll) res++;
	if (sa <= 3ll && sb >= 3ll) res++;
	for (int i=1; i<=999; ++i){
		int x = mergerev(i);
		ll xx = (ll)x * (ll)x;
		if (x >= sa && x <= sb && isRev(xx)) res++;
		for (int j=0; j<10; ++j){
			x = mergerev(i, j);
			ll xx = (ll)x * (ll)x;
			if (x >= sa && x<= sb && isRev(xx)) res++;
		}
	}
	return res;
}

int main(int argc, char const *argv[])
{
	/* code */
	int t; cin >> t;
	for (int cas=1; cas<=t; ++cas){
		cin >> a >> b;
		if (a > b) swap(a, b);
		cout << "Case #" << cas << ": " << find() << endl;
	}
	return 0;
}