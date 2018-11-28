#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <time.h>
using namespace std;

int n, a[30], b[30];
int arr[30];

int cones (int x) {
	int ret = 0;
	while (x) {
		ret += x&1;
		x >>= 1;
	}
	return ret;
}

bool sol (int ind, int st) {
	if (ind == n) {
		return 1;
	}

	bool ret = 0;
	for (int i=0;i<n;i++) {
		if (b[arr[ind]] & (1<<i)) {
			if (st & (1<<i)) {
				continue;
			}
			ret = 1;
			break;
		}
	}

	if (ret) {
		for (int i=0;ret && i<n;i++) {
			if (b[arr[ind]] & (1<<i)) {
				if (st & (1<<i)) {
					continue;
				}
				ret = sol(ind+1, st|(1<<i)) && ret;
			}
		}
	}

	return ret;
}

bool can() {
	for (int i=0;i<n;i++) {
		arr[i] = i;
	}

	bool ret = 1;
	do {
		ret = sol(0, 0) && ret;
	} while (ret && next_permutation (arr, arr+n));
	return ret;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);


	for (int it=1;it<=t;it++) {
		printf ("Case #%d: ", it);

		scanf ("%d", &n);
		char x[30];

		for (int i=0;i<n;i++) {
			scanf ("%s", x);
			a[i] = 0;
			for (int j=0;j<n;j++) {
				a[i] += (x[j] == '1')?(1<<j):0;
			}
		}

		int ret = n*n;

		for (int i=0;i<(1<<(n*n));i++) {
			int cbit = i;
			int ones = (1<<n) - 1;
			bool ok = true;
			for (int j=0;j<n;j++) {
				int tbit = cbit & ones;
				if (tbit & a[j]) {
					ok = false;
					break;
				}
				cbit >>= n;
			}
			if (ok) {
				int res = 0;
				cbit = i;
				for (int j=0;j<n;j++) {
					int tbit = cbit & ones;
					b[j] = a[j] | tbit;
					res += cones (tbit);
					cbit >>= n;
				}
				if (can()) {
					//cout << i << endl;
					ret = min (ret, res);
				}
			}
		}

		printf ("%d\n", ret);
	}

	return 0;
}