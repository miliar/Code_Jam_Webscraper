#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

long long gcd(long long a, long long b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

struct stru {
	long long a;
	long long b;
	void yf() {
		long long c	 = gcd(a, b);
		a /= c;
		b /= c;
	}

	bool operator<(const stru& a) const {
		return this->a * a.b < this->b * a.a;
	}
};

void work() {
	stru a;
	scanf("%I64d/%I64d", &a.a, &a.b);
	a.yf();
	long long tmp = a.b;
	
	while (tmp % 2 == 0) {
		tmp /= 2;
	}
	if (tmp != 1) {
		cout << "impossible" << endl;
		return;
	}

	int ans = 0;
	while (a.a > 1) {
		a.a /= 2;
		ans--;
	}
	while (a.b > 1) {
		a.b /= 2;
		ans++;
	}
	cout << ans << endl;
	/*
	map<stru, int> st;
	stru t;
	t.a = 0;
	t.b = 1;
	st.insert(make_pair(t, 0));
	t.a = 1;
	st.insert(make_pair(t, 0));
	
	do {
		map<stru, int>::iterator it = st.lower_bound(a);
		stru s2 = it->first;
		if (s2.a == a.a && s2.b == a.b) {
			cout << it->second << endl;
			return;
		}

		map<stru, int>::iterator it0 = it;
		it0--;
		stru s1 = it0->first;

		stru nw;
		nw.b = s1.b * s2.b * 2;
		nw.a = s1.b * s2.a + s1.a * s2.b;
		nw.yf();
		st.insert(make_pair(nw, it->second + 1));
	} while (true);
	*/
}

int main() {
	//ios::sync_with_stdio(false);
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}

