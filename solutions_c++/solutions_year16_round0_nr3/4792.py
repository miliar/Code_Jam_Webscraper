#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <complex>
#include <time.h>

#define M_PI           3.14159265358979323846

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "1"

#pragma comment(linker, "/STACK:56777216")

typedef unsigned long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;


int GetBitIdx(int bitsFromLeft, int bitsInNum) {
	int fromLeft = bitsFromLeft + 1;
	return bitsInNum - fromLeft - 1;
}

ll GetNum(const vi& ans, int div) {
	ll result = 0;

	ll base = 1;
	for (int i = 0; i < ans.size(); ++i) {
		result += ans[ans.size() - 1 - i] * base;
		base *= div;
	}
	return result;
}

vector<char> IsPrime(int n) {
	vector<char> prime(n + 1, true);
	prime[0] = prime[1] = false;
	for (int i = 2; i <= n; ++i)
		if (prime[i])
			if (i * 1ll * i <= n)
				for (int j = i*i; j <= n; j += i)
					prime[j] = false;

	return prime;
}

bool IsPrime(const vi& vec, const vector<ll>& firstPrimes, vector<ll>& divisors) {
	for (int div = 2; div <= 10; ++div) {
		ll num = GetNum(vec, div);
		bool prime = true;
		for (ll p : firstPrimes) {
			if (num % p == 0) {
				divisors.push_back(p);
				prime = false;
				break;
			}
		}
		if (prime) {
			return true;
		}
	}
	return false;
}

vector<vector<int>> GetAnswers(int len, int count, const vector<ll>& firstPrimes, vector<vector<ll>>& divisors) {
	vvi res;
	int i = 0;

	while (res.size() < count) {
		vi fill(len, 0);
		fill[0] = 1;
		fill[fill.size() - 1] = 1;

		int bitIdx = 0;
		int numCopy = i;
		while (numCopy != 0) {
			int bitValue = numCopy % 2;
			numCopy /= 2;
			fill[GetBitIdx(bitIdx, len)] = bitValue;
			bitIdx++;
		}

		vector<ll> div;
		if (!IsPrime(fill, firstPrimes, div)) {
			res.push_back(fill);
			divisors.push_back(div);
		}
		i++;
	}
	return res;
}


int main() {
	freopen(PROBLEM_ID".in", "r", stdin);
	freopen(PROBLEM_ID".out", "w", stdout);
	

	freopen(PROBLEM_ID".in", "r", stdin);
	//freopen(PROBLEM_ID".out", "w", stdout);
	// getline(cin, name)


	const int MaxVal = 1000;
	vector<char> primes = IsPrime(MaxVal);
	vector<ll> firstPrimes;
	for (int i = 2; i < MaxVal; ++i) {
		if (primes[i]) {
			firstPrimes.push_back(i);
		}
	}

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n, j;
		cin >> n >> j;
		
		vector<vector<ll>> div;
		vector<vector<int>> answers = GetAnswers(n, j, firstPrimes, div);

		cout << "Case #" << i + 1 << ":" << endl;

		for (int i = 0; i < answers.size(); ++i) {
			for (int bit : answers[i]) {
				cout << bit;
			}
			cout << " ";
			/*
			cout << endl;
			for (ll divIdx = 0; divIdx < div[i].size(); ++divIdx) {
				ll n = GetNum(answers[i], divIdx + 2);
				assert(div[i].size() == 9);
				ll small = divIdx + 2;
				ll x = div[i][divIdx];
				assert(x >= 2);
				cout << n << " " << small << " " << x << " " << n % x << " " << n / x << endl;
			}
			*/
			
			for (ll divisor : div[i]) {
				cout << " " << divisor;
			}
			
			cout << endl;
		}
	}

	return 0;
}