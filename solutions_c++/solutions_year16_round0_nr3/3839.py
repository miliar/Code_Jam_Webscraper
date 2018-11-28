#include <iostream>
#include <bitset>
#include <cmath>
#include <vector>

using namespace std;

long long interpret(string &s, long long base)
{
	long long val = 0;
	for (long long i = s.length() - 1; i >= 0; i--)
		if (s[s.length() - 1 - i] == '1') {
			val += pow((long double) base, i);
		}
	return val;
}

bool isPrime(long long n)
{
	if (n <= 1)
		return false;
	else if (n <= 3)
		return true;
	else if (n % 2 == 0 || n % 3 == 0)
		return false;
	for (long long i = 5; i*i <= n; i += 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;
	return true;
}

bool isValid(string &s, vector<long long> &interps)
{
	for (long long i = 2; i <= 10; i++) {
		long long interp = interpret(s, i);
		if (!isPrime(interp)) {
			interps.push_back(interp);
		} else {
			interps.clear();
			return false;
		}
	}
	return true;
}

long long divisor(long long n)
{
	for (long long i = 2; i < n; i++) {
		if (n % i == 0)
			return i;
	}
}

int main()
{
	long long N, J;
	cin >> N >> N >> J;
	cout << "Case #1:" << endl;
	for (unsigned long long i = 0; (i < 2<<(N-3)) && J; i++) {
		string s = std::bitset<32>(i).to_string();
		s = s.substr(32 - N + 2, 32);
		s = '1' + s + '1';
		vector<long long> interps;
		if (isValid(s, interps)) {
			J--;
			cout << s;
			for (long long interp : interps)
				cout << ' ' << divisor(interp);
			cout << endl;
		}
	}

	return 0;
}