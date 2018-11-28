#include <iostream>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <cassert>
#include <sstream>
#include <bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;

const int inf = 1e9;
const double eps = 1e-7;
const int maxn = 111;
const int mod = 1000000007;

char a[maxn][maxn];
vi gmin, gmax, vmin, vmax;

int get(int n, int m) {
	int res = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			char c = a[i][j];
			if (c == '.') continue;
			if (gmin[i] == gmax[i] && vmin[j] == vmax[j]) {
				return -1;
			}
			int add = 0;
			if (c == '^' && i == vmin[j]) add = 1;
			if (c == 'v' && i == vmax[j]) add = 1;
			if (c == '<' && j == gmin[i]) add = 1;
			if (c == '>' && j == gmax[i]) add = 1;
			res += add;
		}
	}
	
	return res;
}

int main() 
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int T;
	scanf("%d\n", &T);
	for (int t = 0; t < T; ++t) {
		int n, m;
		scanf("%d%d\n", &n, &m);
		gmin.assign(n, inf), gmax.assign(n, -1), vmin.assign(m, inf), vmax.assign(m, -1);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%c", &a[i][j]);
				if (a[i][j] == '.') continue;
				gmin[i] = min(gmin[i], j);
				gmax[i] = max(gmax[i], j);
				vmin[j] = min(vmin[j], i);
				vmax[j] = max(vmax[j], i);
			}
			scanf("\n");
		}
		
		int res = get(n, m);
		if (res == -1) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		} else {
			printf("Case #%d: %d\n", t + 1, res);
		}
	}
	
	return 0;
}
