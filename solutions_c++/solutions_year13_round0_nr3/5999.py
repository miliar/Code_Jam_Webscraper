#include <iostream>
#include <math.h>
using namespace std;

unsigned long long reverse(unsigned long long n);
bool is_palindrome(unsigned long long n);
bool is_f_n_s(unsigned long long n);

int main() {
	int current = 0,cases, st, end, found;
	cin >> cases;
	while (cases) {
		found = 0;
		cin >> st >> end;
		for (int i = st; i <= end; i++) {
			if (is_f_n_s(i))
				found++;
		}
		cout << "Case #" << ++current << ": " << found << endl;
		cases--;
	}
}

bool is_palindrome(unsigned long long n) {
	unsigned long long tmp = n, res = 0;
	while (tmp != 0) {
		res = res*10 + tmp%10;
		tmp = tmp/10;
		//cout << tmp << " " << res << endl;
	}
	
	if (n == res) {
		return true;
	}
	return false;
}

bool is_f_n_s(unsigned long long n) {
	float tmp;
	if (is_palindrome(n)) {
		tmp = sqrt(n);
		if (tmp == (unsigned long long)tmp)
			return is_palindrome((unsigned long long)tmp);
	}
	
	return 0;
}

