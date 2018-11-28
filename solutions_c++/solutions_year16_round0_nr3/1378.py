#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<bitset>
#include <cstdio>
using namespace std;
int primes[7] = {2,3,5,7,11,13,17};
int primefound=7;
int mul = 510510;
int digits, lines, testing;
bool prime(int n) {
	for (int i = 1; i < primefound; i++) {
		if (n%primes[i] == 0)return false;
	}
	return true;
}
void generateprimes(void) {
	primes[0] = 2;
	primefound = 1;
	for (int i = 3; i < 100000; i = i + 2) {
		if (prime(i))primes[primefound++] = i;
	}
}
unsigned long long powof(int base, int p) {
	if (p == 0)return 1;
	if (p % 2)return ((powof(base, p - 1) % mul)*base) % mul;
	unsigned long long tem = (powof(base, p / 2) % mul);
	return (tem*tem) % mul;
}
unsigned long long tobase(int base, string num) {
	unsigned long long res=0;
	int len = num.length();
	len--;
	for (int i = 0; i <= len; i++) {
		if (num[i] == '1') {
			res += powof(base, (len - i));
		}
	}
	return res;
}
int main(void) {
	int totalCase, cases;
	int i, j, k;
	int lim;
	bool ok;
	int divisors[11];
	string s;
	unsigned long long n;
	ifstream cin("l.in");
	ofstream cout("l.out");
	cin >> totalCase;
	//generateprimes();
	for (cases = 1; cases <= totalCase; cases++) {
		testing =0;
		cin >> digits >> lines;
		digits -= 2;
		cout << "Case #" << cases << ":" << endl;
		for (i = 0; i < lines; testing++) {
			s = bitset<32>(testing).to_string();
			s = "1" + s.substr(32-digits,32) + "1";
			for (j = 2; j <= 10; j++) {
				n = tobase(j, s);
				lim = ceil(sqrt(n));
				ok = false;
				for (k = 0; k < primefound && primes[k] <= lim; k++) {
					if (n%primes[k] == 0) {
						divisors[j] = primes[k];
						ok = true;
						break;
					}
				}
				if (!ok)break;
			}/////////divisor
			if (j > 10) {/////////////print
				i++;
				cout << s;
				for (k = 2; k <= 10; k++)cout << " " << divisors[k];
				cout << endl;
			}
		}/////////////////line
	}////////////////////case
	system("pause");
	return 0;
}
