// File Name: C.cpp
// Author: YangYue
// Created Time: 六  4/27 10:10:57 2013
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

const int MaxN = 200005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const LL LINF = 1000000000000000005ll;

int n, m, K, R;
int b[MaxN], c[MaxN];
void solve() {
	int a[3];
	int tot = 0;
	for (a[0] = 2; a[0] <= m; ++a[0])
	for (a[1] = 2; a[1] <= m; ++a[1])
	for (a[2] = 2; a[2] <= m; ++a[2]) {
		set<int> SET;
		for (int t = 0; t < 1 << 3; ++t) {
			int produ = 1;
			for (int i = 0; i < 3; ++i) if ((t >> i) & 1) produ *= a[i];
			SET.insert(produ);
		}
		bool find = 1;
		for (int i = 0; i < K; ++i) if (!SET.count(c[i])) find = 0;
		if (find) {
			b[tot++] = a[0] * 100 + a[1] * 10 + a[2];
		}
	}
	int t = rand() % tot;
	printf("%d\n", b[t]);
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	printf("Case #1:\n");

	int cases; cin >> cases;

	cin >> R >> n >> m >> K;
	while (R--) {
		for (int i = 0; i < K; ++i) scanf("%d",c+i);
		if (c[0] == 1 && c[1] == 1 && c[2] == 1) printf("222\n");
		else solve();
	}
	return 0;
}

// hehe ~


