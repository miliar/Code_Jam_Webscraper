#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)
#ifdef WIN32
	#define I64d "%I64d"
#else
	#define I64d "%lld"
#endif

typedef pair <int, int> pi;
typedef vector <int> vi;

int k, n;
vector <vi> keys;
vi ikeys, c, need, cnt;
int dp[1<<20], gv[1<<20];

int Find(int x) {
	return lower_bound(c.begin(), c.end(), x) - c.begin();
}

bool go(int mask) {
	if (mask == (1 << n) - 1)
		return true;

	int &res = dp[mask];
	if (res != -1) return res;
	res = 0;


	for (int i = 0; i < n; ++i) if (!(mask & (1<<i)) && cnt[need[i]] > 0) {
		--cnt[need[i]];
		forit (it, keys[i])
			++cnt[*it];
		if (go(mask|(1<<i))) {
			if (res == 0) gv[mask] = i;
			res = 1;
		}
		++cnt[need[i]];
		forit (it, keys[i])
			--cnt[*it];
	}
	//printf("mask=%d res=%d\n", mask, res);

	return res;
}

int main() {
	int tests;
	scanf("%d", &tests);	
	for (int casenum = 1; casenum <= tests; ++casenum) {
		scanf("%d%d", &k, &n);			
		c.clear();
		ikeys.resize(k);
		for (int i = 0; i < k; ++i) {
			scanf("%d", &ikeys[i]);
			c.pb(ikeys[i]);
		}
		keys.assign(n, vector <int>());
		need.resize(n);

		for (int i = 0; i < n; ++i) {
			int k;
			scanf("%d%d", &need[i], &k);
			c.pb(need[i]);
			keys[i].resize(k);
			for (int j = 0; j < k; ++j) {
				scanf("%d", &keys[i][j]);
				c.pb(keys[i][j]);
			}
		}

		sort(c.begin(), c.end());
		c.erase(unique(c.begin(), c.end()), c.end());
		/*for (int i = 0; i < c.size(); ++i)
			printf("%d ", c[i]);
		puts("");                   */
		

		//printf("in --> ");
		for (int i = 0; i < ikeys.size(); ++i) {
			ikeys[i] = Find(ikeys[i]);
			//printf("%d ", ikeys[i]);
		}
		//puts("");

		for (int i = 0; i < n; ++i) {
			//printf("%d --> ", i + 1);
			need[i] = Find(need[i]);
			//printf("need=%d , has= ", need[i]);
			for (int j = 0; j < keys[i].size(); ++j) {
				keys[i][j] = Find(keys[i][j]);
				//printf("%d ", keys[i][j]);
			}
			//puts("");
		}

		printf("Case #%d:", casenum);
		memset(dp, -1, sizeof(dp));
		
		cnt.assign(c.size(), 0);
		forit (it, ikeys)
			++cnt[*it];

		if (!go(0))
			puts(" IMPOSSIBLE");
		else {
			for (int mask = 0; mask != (1<<n)-1; ) {
				int v = gv[mask];
				printf(" %d", v + 1);
				mask |= (1 << v);
			}			
			puts("");
		}
	}
	return 0;		
}
