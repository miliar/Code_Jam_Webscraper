#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const double pi = acos(-1.0);

const int size = 10 * 1000 * 1000;
const int longlen = 100;

bool ispal(long long num) {
	vector <int> h;
	while (num > 0) {
		h.pb(num % 10);
		num /= 10;
	}
	for (int i = 0; i < h.size(); i++)
		if (h[i] != h[h.size() - i - 1])
			return false;
	return true;
}

/*
struct mylong {
	int body[longlen];

	int operator [](int ps) {
		assert(ps >= 0 && ps < longlen);
		return body[ps];
	}


};
*/


int main() {
	freopen("problem_c.in", "r", stdin);
	freopen("problem_c.out", "w", stdout);
	
	vector <long long> amazing;
	for (int i = 1; i <= size; i++)
		if (ispal(i) && ispal(i * 1ll * i))
			amazing.pb(i * 1ll * i);

	sort(amazing.begin(), amazing.end());

	/*
	cout << amazing.size() << endl;
	for (int i = 0; i < amazing.size(); i++)
		cout << long long(sqrt(1.0 * amazing[i])) << ' ' << amazing[i] << endl;
	*/

	long long a, b, tc;
	cin >> tc;
	for (int tnum = 0; tnum < tc; tnum++) {
		cin >> a >> b;
		int cnt = 0;
		for (int i = 0; i < amazing.size(); i++)
			cnt += (amazing[i] >= a && amazing[i] <= b);
		cout << "Case #" << tnum + 1 << ": " << cnt << endl;
	}
	
	return 0;
}