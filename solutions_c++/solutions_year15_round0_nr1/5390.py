#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

using namespace std;

#define ll long long
#define vi vector<int>
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define forn(i,n) for (size_t i = 0; i < n; ++i)
#define forb(i,n) for (int i = n - 1; i >= 0; --i)
                              
const double EPS = 1e-9;
const int MAXN = 666666;
const int MOD = 1e9 + 7;
const int MOD1 = 1e9 + 35011;
const int MOD2 = 1e9 + 18169;
const int INF = (1 << 30);
const long long INFl = 1e18;

int T, N, cnt, ans, n;
char s[MAXN];

int main() {
#ifdef F0X
	freopen("input.in", "r", stdin);
	freopen("out.in", "w", stdout);
	double st = clock();
#endif

	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		ans = 0;
		scanf("%d ", &N);
		gets(s);
		n = strlen(s);

		cnt = s[0] - '0';
		for (int i = 1; i < n; ++i) {
			if (cnt < i) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += s[i] - '0';
		}
		printf("Case #%d: %d\n", t, ans);
	}
                                     
#ifdef F0X
	cerr << "Time is " << (clock() - st) / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}