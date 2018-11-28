#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <ctime>
#include <stack>
#include <map>
#include <set>
#if __cplusplus > 199711L
#include <unordered_set>
#include <unordered_map>
#include <tuple>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
//	tree<key, mapped = null_type, cmp = less<key>, rb_tree_tag, tree_order_statistics_node_update> name;
//	order_of_key
//	find_by_order
#endif

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define abs(a) ((a) < 0 ? -(a) : (a))
#define sqr(a) ((a) * (a))

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const double eps = 1e-9;
const int mod = (int)1e+9 + 7;
const double pi = acos(-1.);
const int maxn = 100100;

bool pm[2][maxn];
int n, cr, c0, c1;
int mx[5][5], my[5][5];

void dfs(int dl, int u) {
	pm[dl][u] = 1;
	if(dl == 0) {
		c0++;
		for(int i = 0; i < n; i++) {
			if(!my[u][i]) {
				continue;
			}
			cr++;
			if(pm[1][i]) continue;
			dfs(1, i);
		}
	}
	if(dl == 1) {
		c1++;
		for(int i = 0; i < n; i++) {
			if(!my[i][u]) {
				continue;
			}
			cr++;
			if(pm[0][i]) continue;
			dfs(0, i);
		}
	}
}

int main() {

	#ifdef SOL
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	#else
	{
		srand(time(0));
		const string file = "";
		if(!file.empty()) {
			freopen((file + ".in").c_str(), "r", stdin);
			freopen((file + ".out").c_str(), "w", stdout);
		}
	}
	#endif

	int t;
	scanf("%d", &t);
	for(int q = 1; t--; q++) {
		printf("Case #%d: ", q);
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			scanf("\n");
			for(int j = 0; j < n; j++) {
				char c;
				scanf("%c", &c);
				mx[i][j] = c == '1';
			}
		}
		int ans = mod;
		for(int mask = 0; mask < (1 << (n * n)); mask++) {
			int cnt = 0;
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					my[i][j] = 0;
					if(mx[i][j] == 1) my[i][j] = 1; else
					if((mask >> (i * n + j)) & 1) {
						my[i][j] = 1;
						cnt++;
					}
				}
			}
			bool ok = 1;
			for(int i = 0; i < n; i++) {
				if(!pm[0][i]) {
					cr = 0, c0 = 0, c1 = 0;
					dfs(0, i);
//					cout << mask << " " << cnt << " " << c0 << " " << c1 << " " << cr << endl;
					if(c0 != c1 || cr != c0 * c1 * 2) {
						ok = 0;
					}
				}
			}
			for(int i = 0; i < n; i++) {
				pm[0][i] = pm[1][i] = 0;
			}
			if(ok) {
				ans = min(ans, cnt);
			}
		}
		printf("%d\n", ans);
	}

	#ifdef SOL
	{
		fflush(stdout);
		fprintf(stderr, "%.3lf ms\n", 1000. * clock() / CLOCKS_PER_SEC);
		fflush(stderr);
	}
	#endif
	return(0);
}

// by Andrey Kim
