#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <string>

using namespace std;

// Osmos

int test;
int n, a0;
int a[1000010];

int main() {
	freopen("A-large.inp", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &test);
	for(int ttest = 1; ttest <= test; ttest++) {
		scanf("%d%d", &a0, &n);
		
		for(int i = 1; i <= n; i++) scanf("%d", a+i);
		sort(a+1, a+1+n);
		int ret = 1e9, now = 0;
		for(int i = 1; i <= n; i++) {
			ret = min(ret, now + n-i+1);
			while (a0 <= a[i]) {
                if (a0 == 1) {
                    now = 1e9;
                    break;
                }
				a0 += a0-1;
				now++;
			}
			a0 += a[i];
		}
		ret = min(ret, now);
		printf("Case #%d: %d\n", ttest, ret);
	}
	return 0;
}
