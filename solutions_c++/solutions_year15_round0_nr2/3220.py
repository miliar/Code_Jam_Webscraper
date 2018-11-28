#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <cctype>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef double dd;

int p[1005];

int main() {
	freopen("C:\\in.txt", "r", stdin);
	freopen("C:\\out.txt", "w", stdout);
	//iostream::sync_with_stdio(0);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int d;
		scanf("%d", &d);
		int ma = 0;
		for (int j = 0; j < d; j++) {
			int v;
			scanf("%d", &v);
			p[j] = v;
			if (p[j] > ma) {
				ma = p[j];
			}
		}
		int res = ma;
		for (int k = 1; k <= ma; k++) {
			int sum = k;
			for (int l = 0; l < d; l++) {
				if (p[l] > k) {
					if (p[l] % k == 0) {
						sum += (p[l] / k - 1);
					} else {
						sum += (p[l] / k);
					}
				}
			}
			res = min(res, sum);
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}