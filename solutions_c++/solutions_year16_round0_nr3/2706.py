#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <bitset>
#include <string>
#include <cmath>


using namespace std;

ifstream in ("in.txt");
ofstream out ("out.txt");

typedef long long ll;

ll prime(ll n) {
	ll lim = ceil(sqrt(n));

	if (n % 2 == 0) return 2;

	ll d = 3;
	while (d <= lim) {
		if (n % d == 0) return d;

		d += 2;
	}

	return -1;
}

ll base(ll b, ll num) {
	ll res = 0;
	ll p = 1;

	int mask = 1;

	for (int i = 0; i < 16; i++) {
		ll d = ((1 << i) & num) >> i;
		res += (p * d);

		p *= b;
	}

	return res;
}

void print_two(int num) {
	string s = "";
	for (int i = 0; i < 16; i++) {
		int d = (num & (1 << i)) >> i;
		if (d) s = "1" + s;
		if (!d) s = "0" + s;
	}

	out << s;
}

void solve() {
	int N = 16, J = 50;

	int num = (1 << 15) + 1;
	int c = 0;
	int sum = 2;

	vector<ll> l = vector<ll>();

	while (c < J) {
		l.clear();
		cout << base(10, num) << endl;
		for (int b = 2; b <= 10; b++) {
			ll d = prime(base(b, num));
			if (d > 0) {
				l.push_back(d);
			} else {
				break;
			}
		}

		int s = (int) l.size();
		if (s == 9) {
			c++;
			
			print_two(num);
			out << " ";
			for (int i = 0; i < 8; i++) {
				out << l[i] << " ";
			}
			out << l[8] << endl;
		}

		sum += 2;
		num += 2;
	}


}


int main() {

	int T = 1;

	for (int i = 1; i <= T; i++) {

		int N, J;

		in >> N >> J;
			
		out << "Case #1:\n";
		solve();
	}


	in.close();
	out.close();
	return 0;
}
