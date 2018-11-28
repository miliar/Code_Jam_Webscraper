#pragma comment(linker, "/STACK:64000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 4<<20;
typedef pair<int, int> pii;

struct Gen {
	int first;
	int mult;
	int add;
	int mod;

	void Read() {
		scanf("%d%d%d%d", &first, &mult, &add, &mod);
	}
	int Do() {
		int res = first;
		first = (int64(first) * mult + add) % mod;
		return res;
	}
};

int n, d;
Gen sal, par;
vector<vector<int>> sons;
int level[SIZE];
pii arr[SIZE];

struct Event {
	int crd;
	int idx;
	bool ends;
	bool operator< (const Event &b) const {
		if (crd != b.crd)
			return crd < b.crd;
		return ends < b.ends;
	}
};
vector<Event> evs;
bool curr[SIZE];
int currCount;


void DFS(int u, pii up) {
	up = pii(min(up.first, level[u]), max(up.second, level[u]));
	arr[u] = up;
	for (int x : sons[u])
		DFS(x, up);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &d);
		sal.Read();
		par.Read();
		sons.clear();
		sons.resize(n);
		for (int i = 0; i < n; i++) {
			level[i] = sal.Do();
			int f = par.Do();
			if (i > 0) {
				f %= i;
				sons[f].push_back(i);
				Ef("%d -> %d\n", i, f);
			}
		}

		DFS(0, pii(level[0], level[0]));
		for (int i = 0; i < n; i++) Ef("%d: [%d %d]\n", i, arr[i].first, arr[i].second);

		evs.clear();
		for (int i = 0; i < n; i++) {
			if (arr[i].second - arr[i].first > d)
				continue;
			Event e;
			e.idx = i;
			e.ends = false;
			e.crd = arr[i].second - d;
			evs.push_back(e);
			e.ends = true;
			e.crd = arr[i].first;
			evs.push_back(e);
		}

		sort(evs.begin(), evs.end());

		int ans = 1;
		memset(curr, 0, sizeof(curr));
		currCount = 0;
		for (auto &e : evs) {
			if (e.ends) {
				curr[e.idx] = false;
				currCount--;
			}
			else {
				curr[e.idx] = true;
				currCount++;
			}
			assert(currCount >= 0);
			ans = max(currCount, ans);
		}
		
		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
