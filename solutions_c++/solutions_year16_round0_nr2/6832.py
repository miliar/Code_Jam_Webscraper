#include <iostream>
#include <string>
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
	string s;
	long res = 0;
	cin >> s;
	long l = s.length();
	long a[111]; 
	for (int i = 0; i < l; i ++) 
		if (s[i] == '+') a[i] = 1;
		else a[i] = 0;
	
	for (long i = l-1; i >= 0; i --) {
		if (a[i] == 0) {
			res	+= 1;
			for (int j = 0; j <i + 1; j ++) a[j] = 1-a[j];
		}
	}
	return res;
}

int main() {
	long t = 0, x = 0;
	cin >> t;
	for (int i = 0; i < t; i ++) {
		long long ans = calc(x);
		printf("Case #%d: %d\n",i+1, ans);
	}
	return 0;
}
