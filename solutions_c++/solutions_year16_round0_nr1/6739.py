#include <iostream>
using namespace std;

long count(long long num) {
	long res = 0;
	while (num > 0) {
		res = res | (1 << (num%10));
		num = num / 10;
	}
	return res;
}

long long calc(long x) {
	long long i = 0;
	if (x == 0) return -1;
	long long t = 0;
	long long seen = 0;
	while (1) {
		t = t + x;
		seen = seen | count(t);
		if (seen == ((1 << 10) - 1)) return t;
	}
	return -1;
}

int main() {
	long t = 0, x = 0;
	cin >> t;
	for (int i = 0; i < t; i ++) {
		cin >> x;
		long long ans = calc(x);
		if (ans != -1) 
			printf("Case #%d: %d\n",i+1, ans);
		else printf("Case #%d: INSOMNIA\n",i+1);
	}
	return 0;
}
