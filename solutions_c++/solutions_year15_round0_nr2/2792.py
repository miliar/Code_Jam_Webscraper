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

int a[10000];
int main()
{
	int tt, cas = 0, ans, n;
	cin >> tt;
	while (tt --) {
		cin >> n;
		ans = 0;
		for (int i = 0; i < n; i ++) {
			scanf("%d", a + i);
			if (a[i] > ans) ans = a[i];
		}
		for (int i = 2; i < ans; i ++) {
			int tmp = 0;
			for (int j = 0; j < n; j ++)
				tmp += (a[j] - 1) / i;
			if (tmp + i < ans) ans = tmp + i;
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}


