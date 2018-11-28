#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

using namespace std;

typedef long long ll;

const int maxn = 1e6+1e3;

string toString(int a) {
	stringstream str;
	str << a;
	return str.str();
}

ll findPrime(ll k) {
	if (k%2 == 0) return 2;
	for (ll i = 3; i*i <= k; i += 2) {
		if (k%i == 0) return i;
	}
	return -1;
}

ll to10(ll k, ll base) {
	ll sum = 0, prod = 1;
	while (k > 0) {
		sum += prod*(k%10);
		k /= 10;
		prod *= base;
	}
	return sum;
}

ll to2(ll k) {
	ll sum = 0, prod = 1;
	while(k > 0) {
		sum += prod*(k%2);
		k /= 2;
		prod *= 10;
	}
	return sum;
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("All2.in");
	ofstream cout("All2.out");
	int k;
	cin >> k;
	int n, j, cnt = 0;
	cin >> n >> j;
	cout << "CASE #1:\n";
	for (ll i = (1LL << n-1)+1; cnt < j; i += 2) {
		ll tmp = to2(i);
		ll arr[11];
		bool works = true;
		for (ll base = 2; base <= 10; base++) {
			arr[base] = to10(tmp, base);
			if (findPrime(arr[base]) == -1) {
				works = false;
				break;
			}
		}
		if (works) {
			cnt++;
			cout << tmp;
			for (int base = 2; base <= 10; base++) {
				cout << ' ' << findPrime(arr[base]);
			}
			cout << '\n';
		}
	}
	return 0;
}

