#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 10000 + 10;

int a[N];
int n, cap, ans;
int testCases;

int main()
{
	cin >> testCases;
	for (int t = 1; t <= testCases; ++t) {
		cin >> n >> cap;
		for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
		sort(a, a + n);
		ans = 0;
		int l, r = n - 1;
		for (l = 0; l <= r; ++l) {
			while (r > l && a[l] + a[r] > cap) {
				++ans;
				--r;
			}
			if (l == r) {
				++ans;
				break;
			}
			++ans;
			--r;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
