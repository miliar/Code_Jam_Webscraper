#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
#define MOD 1000002013

struct line{
	ll o, e, p;
} l[1010];

ll f(ll x, int n) {
	x/=2;
	return x * n - x*(x-1)/2;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; ++kase) {
		ll station[300] = {0};
		ll n, m, ori = 0;
		cin >> n >> m;
		for(int i = 0; i < m; ++i){
			cin >> l[i].o >> l[i].e >> l[i].p;
			l[i].o*=2; l[i].e*=2;
			for(int j = l[i].o; j <= l[i].e; ++j) {
				station[j] += l[i].p;
			}
			ori += f(l[i].e - l[i].o, n)*l[i].p;
		}
		ll ans = 0, tmp;
		while(true) {
			int flag = 0;
			tmp = 0;
			for(int i = 1; i <= 300; ++i) {
				if(station[i]) {
					flag = 1;
					station[i]--;
					tmp++;
				}
				else if(tmp){
					tmp--;
					ans += f(tmp, n);
					tmp = 0;
				}
			}
			if(flag == 0) break;
		}
//		cout << ori << ' ' << ans << endl;
		cout << "Case #" << kase << ": " << (ori - ans)%MOD << endl;
	}
	return 0;
}
