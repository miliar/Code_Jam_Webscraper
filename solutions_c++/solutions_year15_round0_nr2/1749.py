#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int lim = 1e3 + 10, inf = 2e9;

int a[lim];

int main() {
	//freopen("b.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (int s = 1; s <= TT; s++) {
		int d;
		scanf("%d", &d);
		int Max = 0;
		for (int i = 0; i < d; i++) {
			scanf("%d", &a[i]);
			Max = max(Max, a[i]);
		}
		int ans = inf;
		for (int i = 1; i <= Max; i++) {
			int now = i;
			for (int j = 0; j < d; j++) {
				now += a[j] / i;
				if (a[j] % i == 0) now--;
			}
			ans = min(ans, now);
		}
		printf("Case #%d: %d\n", s, ans);
	}
	return 0;
}

