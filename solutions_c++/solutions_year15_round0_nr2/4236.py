#include <iostream>
#include <cstdio>

using namespace std;

int num[1111];

int main() {
	int nc;
	cin >> nc;
	for(int cid=1; cid<=nc; ++cid) {
		int n, maxnum = 0;
		cin >> n;
		for(int i=0; i<n; ++i) {
			cin >> num[i];
			maxnum = max(maxnum, num[i]);
		}
		int ans = maxnum;
		for(int limit=1; limit<=maxnum; ++limit) {
			int total = 0;
			for(int i=0; i<n; ++i)
				if(num[i] > limit)
					total += (num[i]-1)/limit;
			ans = min(ans, total+limit);
		}
		printf("Case #%d: %d\n", cid, ans);
	}
	return 0;
}
