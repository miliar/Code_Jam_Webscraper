//by allenlyh
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <complex>
#include <assert.h>

using namespace std;

#define sign(x) ((x)<-eps?-1:((x)>eps))
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin();it!=s.end();it++)

typedef long long LL;
typedef pair<int, int> Pii;
typedef pair<LL, LL> PLL;
typedef complex<double> point;

const int maxn = 1000 + 10;
int n;
int p[maxn];

void init() {
	scanf("%d", &n);
	for (int i=0;i<n;i++) scanf("%d", &p[i]);
}

void work() {
	int ans = 0x3f3f3f3f;
	for (int tim=1;tim<=1000;tim++) {
		int cur = 0;
		for (int i=0;i<n;i++) {
			cur += p[i] / tim + (p[i] % tim != 0 ? 1 : 0) - 1;
		}
		ans = min(ans, cur + tim);
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		init();
		printf("Case #%d: ", ++cas);
		work();
	}
	return 0;
}

