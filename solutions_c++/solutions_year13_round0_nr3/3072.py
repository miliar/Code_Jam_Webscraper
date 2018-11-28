#include <gmpxx.h>
#include <iostream>
#include <string>

using namespace std;

bool ispal(const mpz_class &n) {
	string s = n.get_str(10);
	for (unsigned i = 0; i < s.size() / 2; ++i) {
		if (s[i] != s[s.size() - i -1]) return false;
	}
	return true;
}

void doit(int casenum) {
	cout << "Case #" << casenum << ": ";

	string sa, sb;
	cin >> sa >> sb;
	mpz_class a(sa), b(sb);
	
	mpz_class sqa, sqb;
	sqa = sqrt(a);
	sqb = sqrt(b);
	
	mpz_class n;
	n = sqa;
	if (n*n < a) n++;

	int cnt = 0;
	for (; n <= sqb; ++n) {
		if (ispal(n) && ispal(n*n)) {
			cnt++;
		}
	}

	cout << cnt << endl;
}


int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) doit(i);

	return 0;
}
