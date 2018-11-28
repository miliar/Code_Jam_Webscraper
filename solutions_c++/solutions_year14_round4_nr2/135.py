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

const int N = 1000 + 10;

set<int> vis;
int a[N];
int n, testCases;
int ans;

int main()
{
	cin >> testCases;
	for (int t = 1; t <= testCases; ++t) {
		ans = 0;
		vis.clear();
		
		cin >> n;
		for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
		int l = -1, r = n;
		for (int i = 0; i < n; ++i) {
			int k = -1;
			for (int j = 0; j < n; ++j)
				if (! vis.count(a[j]) && (k == -1 || a[j] < a[k])) k = j;
			vis.insert(a[k]);
			int posL, posR;
			for (posL = k - 1; posL >= 0; --posL)
				if (posL <= l && a[posL] < a[k]) break;
			for (posR = k + 1; posR < n; ++posR)
				if (posR >= r && a[posR] < a[k]) break;
				
//			cerr << posL << ' ' << posR << endl;
				
			if (k - posL - 1 < posR - k - 1) {
				for (int j = k; j > posL + 1; --j) swap(a[j], a[j - 1]);
				ans += k - posL - 1;
				++l;
			}
			else {
				for (int j = k; j < posR - 1; ++j) swap(a[j], a[j + 1]);
				ans += posR - k - 1;
				--r;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
