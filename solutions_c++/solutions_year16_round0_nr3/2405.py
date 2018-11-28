#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)

typedef long long int tint;
struct binary { tint n; };

tint readInBase(int revnum, int base) {
	tint res = 0;
	while (revnum) {
		res *= base;
		res += (revnum % 2);
		revnum /= 2;
	}
	return res;
}

tint p_rev(tint tr) {
	return readInBase(tr, 2);
}

int minPrime(tint n) {
	for (tint i = 3;(i * i) <= n;i += 2) {
		if (!(n % i)) return i;
	}
	return -1;
}

vector<int> jam(int n) {
	vector<int> res;
	for (int base = 2;base < 11;base++) {
		int minp = minPrime(readInBase(n, base));
		if (minp == -1) {
			return {};
		}
		res.push_back(minp);
	}
	return res;
} 

ostream& operator<<(ostream& os, vector<int> vi) {
	forn(i, vi.size()) {
		if (i) os << " ";
		os << vi[i];
	}
	return os;
}

ostream& operator<<(ostream& os, binary b) {
	vector<int> res;
	tint n = b.n;
	while (n) {
		res.push_back(n % 2);
		n /= 2;
	}
	reverse(res.begin(), res.end());
	for (int i : res) os << i;
	return os;
}


int main() {
	int t, n, j; cin >> t >> n >> j;
	cout << "Case #1:\n";
	for (tint tr = ((1 << 15) + 1), found = 0;tr < (1 << 16) && found < 50;tr += 2) {
		tint revtr = p_rev(tr);
		vector<int> v = jam(revtr);
		if (!v.empty()) {
			binary b = {tr};
			cout << b << ' ' << v << endl;;
			
			found++;
		}
	}
}
