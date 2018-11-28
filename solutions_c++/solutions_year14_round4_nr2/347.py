#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')

void process() {
	int n;
	scanf("%d", &n);
	vector<int> a(n);
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		auto pos = min_element(all(a));
		int dans = min(distance(begin(a), pos), distance(pos + 1, end(a)));
		ans += dans;
		//E(*pos, dans);
		a.erase(pos);
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
