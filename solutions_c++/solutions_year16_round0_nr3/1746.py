#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using boost::multiprecision::cpp_int;

constexpr long long limit = 10000000;

vector<cpp_int> primes;
vector<bool> isPrime(limit, true);
//vector<vector<cpp_int>> powers(11, vector<cpp_int> (17));

cpp_int getFirstNontrivialFactor(cpp_int n);
void generatePrimes();
bool getPrime(cpp_int n);
cpp_int stoll_base(string s, cpp_int base);
//void genPowers();
string lltos30_bin(cpp_int x);

int main(int argc, char *argv[])
{
	generatePrimes();
	//genPowers();
	printf("Case #1:\n");

	cpp_int x = 0;
	int found = 0;
	while(found < 500) {
		vector<cpp_int> div(11, 0);
		string s = '1' + lltos30_bin(x) + '1';

		bool foundPrime = false;

		for(int base = 2; base <= 10; base++) {
			cpp_int num = stoll_base(s, base);
			div[base] = getFirstNontrivialFactor(num);
			if(div[base] == 1) {
				foundPrime = true;
				break;
			}
		}

		if(!foundPrime) {
			cout << s;
			for(int i = 2; i <= 10; i++) {
				cout << " " << div[i];
			}
			cout << "\n";
			found++;
		}

		x++;
	}
	
	return 0;
}

cpp_int getFirstNontrivialFactor(cpp_int n)
{
	if(n < limit && isPrime[static_cast<long long>(n)]) return 1;

	for(auto p : primes) {
		if(n % p == 0) return p;
		if(p*p > n) return 1;
	}
	/*for(cpp_int p = primes.back(); p*p < n; p+=2) {
		if(n % p == 0) return p;
	}*/

	return 1;
}

void generatePrimes()
{
	isPrime[0] = isPrime[1] = false;

	primes.reserve(300);

	for(long long i = 2; i < limit; i++) {
		if(isPrime[i]) {
			primes.push_back(i);
			for(auto j = i*i; j < limit; j += i) {
				isPrime[j] = false;
			}
		}
	}
}

bool getPrime(cpp_int n)
{
	if(n < limit) return isPrime[static_cast<long long>(n)];

	for(auto p : primes) {
		if(p*p > n) return true;
		if(n % p == 0) return false;
	}

	return true;
}

cpp_int stoll_base(string s, cpp_int base)
{
	cpp_int res = 0;

	for(auto x : s) {
		res *= base;
		res += (x - '0');
	}

	return res;
}

string lltos30_bin(cpp_int x)
{
	string res(30, '0');

	for(int i = 0; i < 30; i++) {
		if(x & (1 << i)) res[30-1-i] = '1';
	}

	return res;
}

/*void genPowers()
{
	for(int i = 0; i < powers.size(); i++) {
		powers[i][0] = 1;
		powers[i][1] = i;

		for(int j = 2; j < powers[i].size(); j++) {
			powers[i][j] = powers[i][1] * powers[i][j-1];
		}
	}
}*/