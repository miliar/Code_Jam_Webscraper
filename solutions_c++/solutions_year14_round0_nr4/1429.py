#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
#define MAX 1005

using namespace std;

double A[MAX], B[MAX];

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int i, j, c, t, n, s, e, p, d;
	scanf("%d", & t);
	for (c = 0; c < t; c++) {
		scanf("%d", & n);
		for (i = 0; i < n; i++)
			scanf("%lf", & A[i]);
		for (i = 0; i < n; i++)
			scanf("%lf", & B[i]);
		sort(A, A + n);
		sort(B, B + n);
		s = 0;
		e = n - 1;
		d = 0;
		for (i = 0; i < n; i++) {
			if (A[i] < B[s])
				e--;
			else {
				d++;
				s++;
			}
		}
		p = 0;
		set<double> S;
		for (i = 0; i < n; i++)
			S.insert(B[i]);
		for (i = 0; i < n; i++) {
			set<double>::iterator it = S.lower_bound(A[i]);
			if (it == S.end()) {
				p++;
				S.erase(S.begin());
			} else S.erase(it);
		}
		printf("Case #%d: %d %d\n", c + 1, d, p);
	}
	return 0;
}

