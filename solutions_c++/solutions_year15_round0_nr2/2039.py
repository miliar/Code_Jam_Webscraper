#include <iostream>
#include <cstdio>
using namespace std;

int p[1024];
int main () {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t, d, aux, specials, ret;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> d;
		for (int i = 0; i < d; i++) {
			cin >> aux;
			p[i] = aux;
		}
		ret = 1000000000;
		for (int k = 1; k < 1020; k++) {
			specials = 0;
			for (int i = 0; i < d; i++) {
				specials += (p[i] + k - 1)/k - 1;
			}
			if (ret > specials + k)
				ret = specials + k;
		}
		cout << "Case #" << tc << ": " << ret << endl;
	}
	return 0;
}
