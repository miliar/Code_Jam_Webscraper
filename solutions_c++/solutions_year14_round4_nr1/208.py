#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int main() {
	int nTest; cin >> nTest;
	for(int test = 0; test < nTest; ++test) {
		int n, cap; cin >> n >> cap;
		multiset<int> a;
		for(int i = 0; i < n; ++i) {
			int x; cin >> x;
			a.insert(x);
		}
		int res = 0;
		while(!a.empty()) {
			++res;
			int first = *a.rbegin();
			a.erase(--a.end());
			if(!a.empty()) {
				multiset<int>::iterator it = a.upper_bound(cap - first);
				if(it != a.begin()) {
					a.erase(--it);
				}
			}
		}
		printf("Case #%d: %d\n", test + 1, res);
	}
	return 0;
}
