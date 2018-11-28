#include <iostream>
#include <math.h>
using namespace std;

long long my_pow(int a, int b) {
	long long ret = 1;
	for(int i = 0; i < b; ++i) {
		ret *= a;
	}
	return ret;
}


int main() {
	int t; cin >> t;
	for(int tloop = 1; tloop <= t; ++tloop) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << tloop << ": ";
		for(int i = 0; i < k; ++i) {
			cout << i * my_pow(k,c-1)  + 1 << ' ';
		}
		cout << endl;
	}
}
