#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

long long slpTms(int n) {
	if (n == 0) return -1;

	int max_loop = 1000;
	int arr[15] = {};
	int rem = 10;
	for (int i = 1; i <= max_loop; i++) {
		long long x = 1ll * i * n;
		long long ret = x;
		while (x > 0) {
			int v = x % 10;
			x /= 10;
			if (arr[v] == 0) rem--;
			arr[v]++;
		}
		if (rem == 0)
			return ret;
	}
	return -1;
}

int main() {
	int cas, n;
	cin >> cas;
	for (int i = 1; i <= cas; i++) {
		cin >> n;
		long long slp = slpTms(n);
		if (slp != -1)
			cout << "Case #" << i << ": " << slp << endl;
		else
			cout << "Case #" << i << ": INSOMNIA" << endl;
	}
	return 0;
}

