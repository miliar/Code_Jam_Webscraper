#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <stdio.h>

#pragma comment(linker, "/STACK:16777216")

typedef long long lint;
using namespace std;

map<lint, lint> best;
set<lint> not_tryed;
vector<lint> que;
int answ = 1;

#define min(a, b) ((a) < (b) ? (a) : (b))

lint finda(lint a);
void solve()
{
	lint a;
	cin >> a;
	printf("%lld\n", finda(a));
}

lint rever(lint a) {
	lint res = 0;
	while (a > 0) {
		res = res * 10 + a % 10;
		a /= 10;
	}
	return res;
}

bool add(lint b, lint val) {
	if (best.find(b) == best.end()) {
		best[b] = val;
		return true;
	}
	return false;
}

lint finda(lint a) {
	if (best.find(a) != best.end()) {
		return best[a];
	}

	while (true) {
		vector<lint> newq;

		++answ;
		bool found = false;
		for (int i = 0, sz = que.size(); i < sz; ++i) {
			int rev = rever(que[i]);
			int b = que[i];

			if (add(b + 1, answ)) {
				newq.push_back(b + 1);
			}

			if (add(rev, answ)) {
				newq.push_back(rev);
			}

			if (b + 1 == a || rev == a) {
				found = true;
			}
		}

		que.swap(newq);
		if (found) {
			return answ;
		}
	}

}

int main()
{
	best[1] = 1;
	que.push_back(1);

	std::ios_base::sync_with_stdio(0);
#ifdef GRANDVIC_DEBUG
	//freopen("D:/input.txt", "rt", stdin);
#endif
	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		std::cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
