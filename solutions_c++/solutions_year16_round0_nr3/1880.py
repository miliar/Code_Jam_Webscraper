#include <cstdio> // freopen
#include <iostream>
#include <string> // getline
#include <sstream> // stringstream
#include <vector>
#include <utility> // pair
#include <algorithm> // min
#include <bitset>
using namespace std;

//#define TEST
#define SMALL
//#define LARGE

void coinJam(int N, int J);
void increase(string &s);
void generateBase(vector<vector<long long>> &bases, int rows, int cols);
long long transformDigit(string &s, vector<vector<long long>> &bases, int len, int base);
long long calDivisor(long long num, const vector<long long> &primes);
void generatePrime(vector<long long> &primes, long long N, bool *prime);

int main() {
	string filename = "C";
#ifdef TEST
	string testin = filename + ".txt";
	freopen(testin.c_str(), "rt", stdin);
#endif

#ifdef SMALL
	string smallin = filename + "-small-attempt0.in";
	if (freopen(smallin.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-small.in!" << endl;
		return -1;
	}
	string smallout = filename + "-small.out";
	freopen(smallout.c_str(), "wt", stdout);
#endif
#ifdef LARGE
	string largein = filename + "-large.in";
	if (freopen(largein.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-large.in!" << endl;
		return -1;
	}
	string largeout = filename + "-large.out";
	freopen(largeout.c_str(), "wt", stdout);
#endif

	int T, N, J;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N >> J;
		J = 500;
		cout << "Case #" << i << ":" << endl;
		coinJam(N, J);
		
	}
	return 0;
}

void coinJam(int N, int J) {
	int count = 0;
	int times = pow(2, N - 2);
	string s(N, '0');
	s[0] = '1';
	s[N - 1] = '1';
	string send(N, '1');

	vector<vector<long long>> bases(9, vector<long long>(N, 0));
	generateBase(bases, 9, N);

	// long long primesize = pow(2, 31);
	// long long primesize = 1111111111111111LL;
	long long primesize = 11111111LL;
	// vector<char> temp(primesize, '1');
	bool *prime = new bool[primesize];
	vector<long long> primes;
	generatePrime(primes, primesize, prime);

	vector<long long> res(9, 0);
	// 1010010000000001
	for (int i = 0; i < times; ++i) {
		bool flag = true;
		for (int base = 2; base <= 10; ++base) {
			long long num = transformDigit(s, bases, N, base);
			res[base - 2] = calDivisor(num, primes);
			if (res[base - 2] == 0) {
				flag = false;
				break;
			}
			
		}
		if (flag) {
			cout << s << s;
			for (int i = 0; i < res.size(); ++i) {
				cout << " " << res[i];
			}
			cout << endl;
			++count;
			if (count == J) {
				break;
			}
		}
		/*if (s == send) {
			break;
		}*/
		increase(s);
	}
}
void increase(string &s) {
	int i = 1;
	while (true) {
		if (s[i] == '0') {
			s[i] = '1';
			break;
		}
		else {
			s[i] = '0';
			++i;
		}
	}
}

void generateBase(vector<vector<long long>> &bases, int rows, int cols) {
	long long base = 2;
	for (int i = 0; i < rows; ++i) {
		bases[i][cols - 1] = 1;
		for (int j = cols - 2; j >= 0; --j) {
			bases[i][j] = bases[i][j + 1] * base;
		}

		base += 1;
	}
}

long long transformDigit(string &s, vector<vector<long long>> &bases, int len, int base) {
	long long res = 0;
	for (int i = 0; i < len; ++i) {
		if (s[i] == '1') {
			res += bases[base - 2][i];
		}
	}
	return res;
}

long long calDivisor(long long num, const vector<long long> &primes) {
	long long rootnum = sqrt(num);
	for (int i = 0; i < primes.size() && primes[i] <= rootnum; ++i) {
		if (num % primes[i] == 0) {
			return primes[i];
		}
	}
	return 0;
}

void generatePrime(vector<long long> &primes, long long N, bool *prime) {
	prime[2] = true;
	for (long long i = 3; i < N; ++i) {
		if (i % 2 == 0) {
			prime[i] = false;
		}
		else {
			prime[i] = true;
		}
	}
	long long rootn = sqrt(N);
	for (long long i = 3; i <= rootn; ++i) {
		if (prime[i]) {
			for (long long j = i + i; j < N; j += i) {
				prime[j] = false;
			}
		}
	}
	for (long long i = 2; i < N; ++i) {
		if (prime[i]) {
			// primes.push_back(i);
			primes.insert(primes.end(), i);
		}
	}
}