#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

#define X first
#define Y second

typedef long long ll;
typedef vector <int> vi;

bool check(int *a, int *b, int *c, int n) {
	for (int i = 0; i < n; ++i) {
		int llx = 0;
		for (int j = 0; j < i; ++j)
			if (c[j] < c[i] && a[j] > llx)
				llx = a[j];
		if (a[i] != llx + 1) {
			//cerr << "At " << i << ", expected inc " << a[i] << ", have " << llx + 1 << endl;
			return false;
		}
	}
	for (int i = n - 1; i >= 0; --i) {
		int llx = 0;
		for (int j = n - 1; j > i; --j)
			if (c[j] < c[i] && b[j] > llx)
				llx = b[j];
		if (b[i] != llx + 1) {
			//cerr << "At " << i << ", expected dec " << b[i] << ", have " << llx + 1 << endl;
			return false;
		}
	}
	return true;
}

bool solve(int *f, int *b, int *a, int n, int cnum) {
	if (cnum == 0)
		return check(f, b, a, n);

	set <int> p;
	int mx = 0;
	for (int i = 0; i < n; ++i)
		if (!a[i] && f[i] > mx) {
			mx = f[i];
			p.insert(i);
		}
	mx = 0;
	int uu = 0;
	for (int i = n - 1; i >= 0; --i)
		if (!a[i] && b[i] > mx) {
			mx = b[i];
			if (p.find(i) != p.end() && uu >= b[i] - 1) {
				a[i] = cnum;
				if (solve(f, b, a, n, cnum - 1))
					return true;
				a[i] = 0;
			}
			++uu;
		} else if (!a[i])
			++uu;
	return false;
}

int main() {
	int TT;
	scanf("%d", &TT);
	for (int T = 1; T <= TT; ++T) {
		int n;
		scanf("%d", &n);
		int f[n];
		int b[n];
		int a[n];
		memset(a, 0, n * sizeof(int));

		for (int i = 0; i < n; ++i)
			scanf("%d", &f[i]);
		for (int i = 0; i < n; ++i)
			scanf("%d", &b[i]);

		if (!solve(f, b, a, n, n))
			cerr << "Alert!Alert!" << endl;

		printf("Case #%d:", T);
		for (int i = 0; i < n; ++i)
			printf(" %d", a[i]);
		printf("\n");
	}
}