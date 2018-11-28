#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

typedef long long ll;

int t, n;

ll f(int k) {
	if(k == 0) return -1;
	bool b = 0, c[10];
	memset(c,0,sizeof(c));
	ll init = k;
	while(!b) {
		ll tmp = init;
		while(tmp != 0) {
			c[tmp%10] = 1;
			tmp/=10;
		}
		bool b2 = 1;
		for(int i = 0; i < 10; i++) {
			b2 &= c[i];
		}
		b = b2;
		init += k;
	}
	return init  - k;

}
int main() {
	if(fopen("A.in","r")) freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> n;
		ll val = f(n);
		printf("Case #%d: ", i);
		if(val != -1) {
			cout << val << endl;
		} else {
			printf("INSOMNIA\n");
		}
	}
	return 0;
}