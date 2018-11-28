#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 5e5 + 200;
const int SL = 2500;
#define MP make_pair
#define lli long long int
#define y1 y123123

double p[N];
double d[202][202][202];

int bc(int v) {
	int ans = 0;
	while (v) {
		ans += v & 1;
		v >>= 1;
	}
	return ans;
}

int main() {
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; ++i) cin >> p[i];
		double ans = 0;
		int b = (1 << n);
		for (int mask = 0; mask < b; ++mask) {
			if (bc(mask) != k) continue;
			double f = 0;
			for (int submask = mask; submask > 0; submask = (submask - 1) & mask) {
				if (bc(submask) != k / 2) continue;
				double pr = 1;
				for (int i = 0; i < n; ++i) {
					if ((1 << i) & mask) {
						pr *= ((1 << i) & submask) ? p[i] : (1 - p[i]);
					}
				}
				f += pr;
			}
			ans = max(ans, f);
		}
		printf("%.12lf", ans);

		cout << endl;
	}
}