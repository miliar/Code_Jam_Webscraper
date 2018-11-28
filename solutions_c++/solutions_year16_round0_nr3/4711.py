#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>
#include <vector>
#define DN 16
#define LL long long

using namespace std;

bitset<DN> transform(int n, int maxx) {
	bitset<DN> st;
	st[0] = st[maxx - 1] = 1;
	for(int i = 1; i < maxx - 1; ++i) {
		st[i] = n & (1 << (i-1));
	}
	return st;
}

LL is_prime(LL n) {
	LL nn = sqrt(n);
	for(LL d = 2; d <= nn; ++d) {
		if(n % d == 0)
			return d;
	}
	return 1;
}

int main() {
	int n, j, num = 0;
	LL num_candidate, power;
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n >> n >> j;
	cout << "Case #1:\n";
	for(int i = 0; i < (1 << (n-2)) && num < j; ++i) {
		bitset<DN> candidate = transform(i, n);
		vector<LL> divs;
		
		for(LL base = 2; base <= 11; ++base) {
			num_candidate = 0LL;
			if(base == 11) {
				cout << candidate << " ";
				for(int i = 0; i < divs.size(); ++i)
					cout << divs[i] << " ";
				cout << '\n';
				++ num;
				break;
			}
			power = 1;
			for(int index = 0; index < n; ++index) {
				num_candidate += candidate[index] * power;
				power *= base;
			}
			LL d = is_prime(num_candidate);
			if(d == 1)
				break;
			divs.push_back(d);
		}
	}
	return 0;
}