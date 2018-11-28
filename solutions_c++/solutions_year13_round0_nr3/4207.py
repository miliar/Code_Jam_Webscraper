#include<iostream>
#include<cmath>

using namespace std;

bool isPalindrome(unsigned long long n) {
	char v[100];
	int pos = 0;
	while (n) {
		v[pos] = n%10;
		n /= 10;
		pos++;
	}
	int j = pos - 1;
	for (int i = 0; i < pos; ++i) {
		if (v[i] != v[j]) return false;
		j--;
	}
	return true;
}

int main() {
	int t;
	cin >> t;
	int cas = 1;
	while (t--) {
		unsigned long long a, b;
		cin >> a >> b;
		long n = sqrt(a);
		int count = 0;
		while (true) {
			if (isPalindrome(n)) {
				unsigned long long val = n*n;
				if (val > b) break;
				if (val >= a && isPalindrome(val)) {
					++count;
				}
			}
			n++;
		}
		cout << "Case #" << cas++ << ": " << count << endl;
	}
}
