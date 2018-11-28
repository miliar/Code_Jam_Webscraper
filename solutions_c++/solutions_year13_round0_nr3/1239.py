// File Name: C.cpp
// Author: YangYue
// Created Time: 六  4/13 19:35:10 2013
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

int m;
LL a[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004 };
int b[MaxN];
bool check(LL x) {
	int len = 0;
	for (LL t = x; t; t /= 10)
		b[len++] = t % 10;
	for (int i = 0; i < len; ++i)
		if (b[i] != b[len - i - 1]) return 0;
	return 1;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	
	/*
	LL MAX = 100000000000000ll;
	for (LL t = 1; t * t <= MAX; ++t) if (check(t)) {
		LL tmp = t * t;
		if (check(tmp)) ++m;
	}
	*/
	m = 39;
	//for (int i = 0; i < m; ++i) printf("%lld, ", a[i]);
	
	int cases; cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		printf("Case #%d: ", cas);
		LL x, y;
		cin >> x >> y;
		int l = lower_bound(a, a + m, x) - a;
		int r = lower_bound(a, a + m, y) - a;
		if (a[r] == y)
		cout << r - l + 1 << endl;
		else cout << r - l << endl;
	}
	
	return 0;
}

// hehe ~


