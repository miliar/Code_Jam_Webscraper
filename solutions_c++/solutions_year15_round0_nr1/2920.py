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
#include <cstdlib>
#include <ctime>
#include <cstring>
#define ll long long
#define pb push_back 
#define mp make_pair
#define FOR(x, l, r) for(x = (l); x <= (r); x++)
#define FORD(x, r, l) for(x = (r); x >= (l); x --)
using namespace std;
char ch[10000];
int main()
{
	int cas = 0, tt, ans, now, n, j;
	cin >> tt;
	while (tt --) {
		cin >> n; scanf("%s", ch);
		ans = 0; now = 0;
		for (int i = 0; i <= n; i ++) {
			j = ch[i] - '0';
			if (!j) continue;
			if (i - now > ans) ans = i - now;
			now += j;
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}


