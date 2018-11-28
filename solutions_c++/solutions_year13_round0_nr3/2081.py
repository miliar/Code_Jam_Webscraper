#include <iostream>
#include <cstring>
#include <cstdio>
#include <set>
#include <map>
#include <cassert>

using namespace std;

const long long int UPPER = 100000000000001ll;

bool palindrome(long long num) {
	char s[40];
	sprintf(s, "%lld", num);
	unsigned l = strlen(s);
	for (unsigned i = 0; i < l; i++)
		if (s[i] != s[l - 1 - i])
			return false;
	return true;
}

int main() {
	set<long long> tmp;
	map<long long, int> m;
	for (long long i = 1; i <= 1e7; i++) {
		if (palindrome(i) && palindrome(i * i)) {
			//cout << i << " * " << i << " = " << i * i << endl;
			tmp.insert(i * i);
		}
	}
	int cnt = 0;
	for (set<long long>::iterator it = tmp.begin(); it != tmp.end(); it++) {
		m[*it] = cnt++;
	}
	m[UPPER] = cnt++;
	//cout << "Totaal: " << cnt << endl;
	cerr << "m.size() = " << m.size() << endl;
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		long long A, B;
		cin >> A >> B;
		assert(A <= B);
		assert(0 < A && B < UPPER);
		cout << "Case #" << (i + 1) << ": " << (m.upper_bound(B)->second - m.lower_bound(A)->second) << endl;
	}
	return 0;
}
