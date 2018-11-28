#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

long long f(long long k, long long n) {
	long long res = 1;
	for (long long i = 0; i < n; i++)
		res *= k;
	return res;
}

int main(int argc, char const *argv[]) {
	int testcases;
	cin >> testcases;
	for (int i = 1; i <= testcases; i++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i << ": ";
		if (s * c < k) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		long long tmp = 0, m, n;
		for (m = 0, n = c - 1; m < k; m++, n--) {
			tmp += m * f(k, n);
			if (!n) {
				tmp += 1;
				cout << tmp << " ";
				tmp = 0, n = c;
			} 
		} 

		if (n < c - 1) {
			tmp += 1;
			cout << tmp;
		}
		
		cout << endl;
	}
	return 0;
}