#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int ts=1; ts<=T; ++ts) {
		int N, X;
		cin >> N >> X;
		multiset<int> sizes;
		typedef multiset<int>::iterator setit;
		for (size_t i=0; i<N; ++i) {
			int sz;
			cin >> sz;
			sizes.insert(sz);
		}
		int cd_cnt = 0;
		while (!sizes.empty()) {
			++cd_cnt;
			setit bit = sizes.end();
			setit begit = sizes.begin();
			--bit;
			int bsize = *bit;

			setit kit = sizes.lower_bound(X-bsize);
			while (kit==sizes.end() || (*kit + bsize > X && kit!=begit)) {
				--kit;
			}
			if (kit==bit&&kit!=begit)
				--kit;

			if (kit==bit) {
				sizes.erase(bit);
				continue;
			}
			sizes.erase(bit);
			if (*kit + bsize <= X) {
				sizes.erase(kit);
			}
		}
		cout << "Case #" << ts << ": " << cd_cnt << endl;
	}
	return 0;
}
