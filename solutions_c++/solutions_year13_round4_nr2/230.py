// File Name: B.cpp
// Author: YangYue
// Created Time: Sat Jun  1 23:06:44 2013
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

LL m;
bool checkbad(LL x, LL p) {
	LL t = x;
	LL tmp = m;
	while (t > 0) {
		tmp >>= 1;
		if (p <= tmp) return 0;
		p -= tmp;
		t = (t - 1) >> 1;
	}
	return 1;
}
bool checkgood(LL x, LL p) {
	LL t = m - x - 1;
	LL tmp = m;
	while (t > 0) {
		tmp >>= 1;
		t = (t - 1) >> 1;
	}
	return p >= tmp;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	int cases; cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		printf("Case #%d: ", cas);
		LL p;
		int n; cin >> n >> p;
		m = 1ll << n;
		LL l = 0, r = m;
		while (l + 1 < r) {
			LL mid = (l + r) >> 1;
			if (checkbad(mid, p)) l = mid; else r = mid;
		}
		cout << l << " ";
		l = 0, r = m;
		while (l + 1 < r) {
			LL mid = (l + r) >> 1;
			if (checkgood(mid, p)) l = mid; else r = mid;
		}
		cout << l << endl;
	}
	
	return 0;
}

// hehe ~


