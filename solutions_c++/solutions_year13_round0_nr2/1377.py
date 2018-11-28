// File Name: B.cpp
// Author: YangYue
// Created Time: 六  4/13 19:17:27 2013
//headers 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<LL, LL>PLL;
typedef pair<LL,int>PLI;

#define lch(n) ((n<<1))
#define rch(n) ((n<<1)+1)
#define lowbit(i) (i&-i)
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define MP make_pair
#define PB push_back

const int MaxN = 105;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const LL LINF = 1000000000000000005ll;

int n, m;
int a[MaxN][MaxN], b[MaxN][MaxN];
int f[MaxN], g[MaxN];

int main()
{
	//freopen("in","r",stdin);
	//freopen("out","w",stdout);

	int cases; cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		printf("Case #%d: ", cas);
		
		memset(f, 0, sizeof f);
		memset(g, 0, sizeof g);
		cin >> n >> m;

		for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf("%d",&a[i][j]);
			g[i] = max(g[i], a[i][j]);
			f[j] = max(f[j], a[i][j]);
		}
		for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) b[i][j] = INF;

		for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			b[i][j] = min(b[i][j], f[j]);
			b[i][j] = min(b[i][j], g[i]);
		}

		bool yes = 1;
		for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) if (b[i][j] != a[i][j]) {
			yes = 0;
			break;
		}
		if (!yes) puts("NO");
		else puts("YES");
	}
	
	return 0;
}

// hehe ~


