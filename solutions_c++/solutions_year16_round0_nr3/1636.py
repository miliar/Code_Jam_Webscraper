#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef set<ll> sll;

bool isPrime(int p) {
	if(p <= 1) return false;
	for(int i = 2;i*i <= p; ++i) {
		if(p%i == 0) return false;
	}
	return true;
}

vi getDivList(ll mask, int n) {
	int MAX_P = 1000; //must be smaller than 2^15+1 (approx 30.000).
	vi divList(11,-1);
	for(int b = 2;b <= 10; ++b) {
		for(int p = 2;p <= MAX_P && divList[b] == -1; ++p) {
			if(isPrime(p)) {
				int r = 0;
				for(int i = n-1;i >= 0;--i) {
					r = r*b + ((mask & (((ll)1) << i)) >> i);
					r = r%p;
				}
				if(r == 0) {
					divList[b] = p;
				}
			}
		}
		if(divList[b] == -1) return divList;
	}
	return divList;
}

bool check(const vi& divList) {
	for(int b = 2;b <= 10; ++b) {
		if(divList[b] == -1) return false;
	}
	return true;
}

ll genRandMask(int n) {
	ll mask(0);
	mask |= ((ll)1) << 0;
	mask |= ((ll)1) << (n-1);
	for(int i = 1;i < n-1; ++i) {
		if(rand()%2 == 0) {
			mask |= ((ll)1) << i;
		}
	}
	return mask;
}

string toStr(ll mask, int n) {
	stringstream ss;
	for(int i = n-1; i >= 0; --i) {
		ss << ((mask & (((ll)1) << i)) >> i);
	}
	return ss.str();
}

void solve(int n, int m) {
	sll masks;
	while((int) masks.size() < m) {
		ll mask(genRandMask(n));
		vi divList(getDivList(mask,n));
		bool good(check(divList));
		if(good) masks.insert(mask);
	}
	for(sll::iterator it = masks.begin(); it != masks.end(); ++it) {
		ll mask = *it;
		cout << toStr(mask,n);
		vi divList(getDivList(mask,n));
		for(int b = 2;b <= 10; ++b) {
			cout << " " << divList[b];
		}
		cout << endl;
	}
}

int main() {
	srand(12851231);
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		cout << "Case #" << t << ":" << endl;
		int N, J;
		cin >> N >> J;
		solve(N,J);
	}
	return 0;
}