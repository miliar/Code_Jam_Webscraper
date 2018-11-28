#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i,a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)

const int maxn = 10000;

int a[maxn];

int solve()
{
	int X, n;
	scanf("%d%d", &n, &X);
	for (int i = 0; i < n; ++ i) {
		scanf("%d", &a[i]);
	}
	sort(a, a + n);
	
	int left = 0, right = n / 2 + 1;
	while (left + 1 < right) {
		int middle = (left + right) / 2;
		
		bool valid = true;
		for (int i = 0; i < middle; ++ i) {
			if (a[i] + a[middle * 2 - 1 - i] > X) {
				valid = false;
				break;
			}
		}
		
		if (valid) {
			left = middle;
		} else {
			right = middle;
		}
	}
	return n - left;
}

int main()
{
	int tests, test = 1;
	for (scanf("%d", &tests); test <= tests; ++ test) {
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
