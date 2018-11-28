#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
#include <set>
using namespace std;
typedef long long ll;

set<int> s;
void f(ll n) {
	while(n) {
		int a = n % 10;
		if(s.count(a) == 0) s.insert(a);
		n /= 10;
	}
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int loop = 1; loop <= T; loop++) {
		cout << "Case #" << loop << ": ";

		ll N, n;
		cin >> N;
		if(N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}

		s.clear();
		n = N;
		while(true) {
			f(n);
			if(s.size() == 10) break;
			n += N;
		}
		cout << n << endl;
	}
}