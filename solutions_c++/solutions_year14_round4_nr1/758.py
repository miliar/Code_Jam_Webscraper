#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <set>
#include <vector>

using namespace std;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Tn;
	scanf("%d", &Tn);
	for (int Tc = 1; Tc <= Tn; ++Tc) {
		int n, m;
		scanf("%d%d", &n, &m);

		multiset<int> val;
		for(int i=0;i<n;++i) {
			int x;
			scanf("%d", &x);
			val.insert(x);
		}


		int ans = 0;
		while(!val.empty()) {
			int x = *val.rbegin();
			auto itr = val.find(x);
			val.erase(itr);

			ans++;


			int rest = m - x;
			auto nxt = val.upper_bound(rest);
			if (nxt == val.begin()) continue;
			nxt--;
			val.erase(nxt);
		}


		printf("Case #%d: ", Tc);
		printf("%d\n", ans);
	}
	return 0;
}
