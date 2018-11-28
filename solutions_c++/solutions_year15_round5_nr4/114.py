#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define exit(a) {prt(a);return 0;}
#define PI 3.141592653589
#define int2 pair<int, int>

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n";
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";



int main() {
	int tests = next();
	for (int test = 1; test <= tests; test++) {
		int p = next();
		lint d[p];
		lint c[p];
		for (int i = 0; i < p; i++) d[i] = lnext();
		for (int i = 0; i < p; i++) c[i] = lnext();
		lint sum = 0;
		for (lint cc : c) sum += cc;
		int n = 0;
		lint n2 = 1;
		while(n2 < sum) {
			n2 <<= 1;
			n++;
		}
		int index0 = 0;
		for (int i = 0; i < p; i++) if (d[i] == 0) index0 = i;

		vector<lint> answ(0);
		lint c2[p];
		for (int i = 0; i < n; i++) {
			int imax = 0;
			for (int j = 0; j < p; j++) if (c[j] > 0) imax = j;
			int imax2 = -1;
			for (int j = 0; j < imax; j++) if (c[j] > 0) imax2 = j;
			if (imax2 == -1) {
				answ.pb(0);
				continue;
			}

			lint diff = d[imax] - d[imax2];

			fill(c2, c2 + p, 0);
			int index = p - 1;
			for (int j = p - 1; j > 0; j--) if (c[j] > 0) {
				lint d2 = d[j] - diff;
				while (d[index] > d2) index--;
				c2[index] = c[j];
				c[index] -= c[j];
				c[j] = 0;
			}
			if (c2[index0] > 0) answ.pb(diff);
			else {
				answ.pb(-diff);
				index = p - 1;
				for (int j = p - 1; j >= 0; j--) {
					lint d2 = d[j] - diff;
					while (d[index] > d2) index--;
					c2[j] = c2[index];
					c2[index] = 0;
				}
			}
			for (int j = 0; j < p; j++) c[j] = c2[j];

		}
		sort(answ.begin(), answ.end());


		printf("Case #%d: ", test);
		for (int i = 0; i < n; i++) printf("%d ", answ[i]);
		printf("\n");
	}

}
