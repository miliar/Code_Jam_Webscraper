#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

const long long lim = 10000000000000000;

class bigint
{
public:
	deque<long long> num;
	inline bigint& operator=(const bigint& a) {
		num = a.num;
		return *this;
	}
	inline bigint& operator=(const bigint&& a) {
		this->num = a.num;
		return *this;
	}
	bigint(long long a) {
		do {
			num.push_back(a % lim);
			a /= lim;
		} while (a);
	}
	bigint() {
	}
	bigint(const bigint&& b)
	{
		this->num = b.num;
	}
};

const bigint operator+(const bigint& b, const bigint& a) {
	long long carry = 0;
	int i = 0;
	bigint temp;
	for (; i<b.num.size() && i<a.num.size(); ++i) {
		temp.num.push_back((b.num[i] + a.num[i] + carry) % lim);
		carry = (b.num[i] + a.num[i] + carry) / lim;
	}

	while (i<b.num.size()) {
		temp.num.push_back((b.num[i] + carry) % lim);
		carry = (b.num[i] + carry) / lim;
		++i;
	}
	while (i<a.num.size()) {
		temp.num.push_back((a.num[i] + carry) % lim);
		carry = (a.num[i] + carry) / lim;
		++i;
	}
	if (carry) temp.num.push_back(carry);
	return temp;
}

const bigint operator* (const bigint& b, long long a)
{
	bigint temp;
	long long carry = 0;
	for (deque<long long>::const_iterator itr = b.num.begin(); itr != b.num.end(); ++itr)
	{
		temp.num.push_back((*itr * a + carry) % lim);
		carry = (*itr * a + carry) / lim;
	}
	if (carry)
		temp.num.push_back(carry);
	return temp;
}


vector<long long> convert(long long i, long long j) {
	vector<long long> temp(2);
	bigint a(0);
	bigint b(1);
	while (i > 0) {
		a = a + b * (i & 1);
		b = b * j;
		i >>= 1;
	}
	if (a.num.size() > 2) cout << "error" << endl;
	temp[0] = a.num[0];
	if(a.num.size() > 1)
	temp[1] = a.num[1];
	return temp;
}

bool isnotprime(vector<long long> num, vector<int> prime, int& div) {
	bool check = false;
	for (int p : prime) {
		if (num[0] == p) break;
		long long mod;
		mod = (num[0] % p) + ((num[1] % p) * (lim % p)) % p;
		mod = mod % p;
		if (mod == 0) {
			//cout << p << endl;
			check = true;
			div = p;
			break;
		}
	}
	return check;
}

void print(long long num, vector<int> divs) {
	vector<int> n;
	while (num) {
		n.push_back(num & 1);
		num >>= 1;
	}
	for (vector<int>::reverse_iterator ritr = n.rbegin(); ritr != n.rend(); ++ritr) cout << *ritr;
	cout << ' ';
	for (vector<int>::iterator itr = divs.begin() + 2; itr != divs.end(); itr++) cout << *itr << ' ';
	cout << endl;
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	vector<int> primes;
	primes.reserve(1000000);
	primes.push_back(2);
	for (int i = 3; i < 1000000; i += 2)
	{
		bool isprime = true;
		for (int j : primes)
		{
			if (j > sqrt(i) + 1) break;
			if (i%j == 0)
			{
				isprime = false;
				break;
			}
		}
		if (isprime) primes.push_back(i);
	}
	int t;
	cin >> t;
	int done = 0;
	while (done < t) {
		int n;
		cin >> n;
		int z;
		cin >> z;
		cout << "Case #" << done + 1 << ":" << endl;
		for (long long i = (1LL << (n - 1)) + 1; (i <= (1LL << n) - 1) && z > 0; i = i + 2) {
			vector<int> divs(11);
			bool possible = true;
			for (long long j = 2; j <= 10; j++) {
				vector<long long> num(2);
				num = convert(i, j);
				//cout << ((num[1] != 0) ? num[1]:0) << num[0]<< endl;
				if (!isnotprime(num, primes, divs[j])) {
					possible = false;
					break;
				}
			}
			if (possible) {
				print(i, divs);
				z--;
			}
		}
		done++;
	}
	return 0;
}