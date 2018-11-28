#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')

void process() {
	int n, x;
	scanf("%d%d", &n, &x);
	int d;
	multiset<int> disks;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &d);
		disks.insert(d);
	}
	int ans = 0;
	for (auto it = begin(disks); it != end(disks); ) {
		++ans;
		int v = *it;
		it = disks.erase(it);
		auto jt = disks.upper_bound(x - v);
		if (jt != begin(disks)) {
			--jt;
			if (it == jt) ++it;
			disks.erase(jt);
		}
	}
	printf("%d\n", ans);
}

int main() {
	ios_base::sync_with_stdio(false);
	int tcases;
	scanf("%d", &tcases);
	for (int tcase = 1; tcase <= tcases; ++tcase) {
		printf("Case #%d: ", tcase);
		process();
	}
	return 0;
}
