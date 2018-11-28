#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int popcount(int x) {
	int r = 0;
	while(x) {
		x &= x - 1;
		++r;
	}
	return r;
}

bool is_ok(int remain, vector<int>& list, vector<int>& order)
{
	if(remain == 0)
		return true;

	int n = list.size();
	int idx = n - popcount(remain);
	bool ok = false;

	for(int w = 0; w < n; ++w) {

		int p = order[idx];
		if(!(remain & (1 << w)))
			continue;
		if(!((1 << w) & list[p]))
			continue;

		if(!is_ok(remain ^ (1 << w), list, order))
			return false;
		ok = true;
	}

	return ok;
}

int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int casenum = 1; casenum <= testcase; ++casenum) {

		int n;
		vector<int> list;

		scanf("%d", &n);
		list.resize(n);
		for(int i = 0; i < n; ++i) {
			char buffer[512];
			scanf("%s", buffer);
			list[i] = 0;
			for(int j = 0; j < n; ++j) {
				if(buffer[j] == '1')
					list[i] = list[i] | (1 << j);
			}
		}

		int ans = n * n;
		const int mask = (1 << n) - 1;

		for(int bit = 0; bit < (1 << (n * n)); ++bit) {

			int cost = popcount(bit);
			vector<int> a;

			a.resize(n);
			for(int i = 0; i < n; ++i)
				a[i] = list[i] | ((bit >> (i * n)) & mask);

			bool ok = true;

			vector<int> order;

			for(int i = 0; i < n; ++i)
				order.push_back(i);

			while(true) {
				if(!is_ok(mask, a, order)) {
					ok = false;
					break;
				}
				if(!next_permutation(order.begin(), order.end()))
					break;
			}

			if(ok)
				ans = min(ans, cost);
		}

		printf("Case #%d: %d\n", casenum, ans);
	}

	return 0;
}
