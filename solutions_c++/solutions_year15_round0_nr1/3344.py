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

int main() {
	//freopen("C:\\in.txt", "r", stdin);
	//freopen("C:\\out.txt", "w", stdout);
	//iostream::sync_with_stdio(0);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int smax;
		scanf("%d", &smax);
		int res = 0;
		int sum = 0;
		for (int j = 0; j <= smax; j++) {
			int v;
			scanf("%1d", &v);
			if (j > 0 && sum < j) {
				res += j - sum;
				sum += j - sum;
			}
			sum += v;
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}