#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <functional>
#include <map>

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))

using namespace std;

typedef long long LL;
typedef pair <int,int> PI;
typedef pair <LL, LL> PLL;

int Read()
 {
	char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
	bool neg = (c == '-'); int ret = neg ? 0 : c - 48;
	while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
	return neg ? -ret : ret;
 }
 
LL ans1, ans2;
LL N, P;

bool check1(LL x)
 {
	LL bigcnt = x, sum = 0;
	fd (i, N - 1, 0)
		if (bigcnt) sum += (1LL << (LL) i), bigcnt --, bigcnt /= 2;
	return sum < P;
 }
 
bool check2(LL x)
 {
	LL smallcnt = (1LL << N) - x - 1, sum = 0;
	fd (i, N - 1, 0)
		if (smallcnt) smallcnt --, smallcnt /= 2; else sum += (1LL << (LL) i);
	return sum < P;
 }
 
int main()
 {
	freopen("B.in", "r", stdin), freopen("B.out", "w", stdout);
	int cases = Read(); fo (cas, 1, cases)
	 {
		cin >> N >> P;
		printf("Case #%d: ", cas);
		
		LL l = 0, r = (1LL << N) - 1, ret = 0;
		while (l <= r)
		 {
			LL mid = (l + r) / 2;
			// check
			if (check1(mid)) ret = mid, l = mid + 1; else r = mid - 1;
		 }
		cout << ret << " ";
		
		l = 0, r = (1LL << N) - 1, ret = 0;
		while (l <= r)
		 {
			LL mid = (l + r) / 2;
			if (check2(mid)) ret = mid, l = mid + 1; else r = mid - 1;
		 }
		cout << ret << endl;
	 }
	return 0;
 }
