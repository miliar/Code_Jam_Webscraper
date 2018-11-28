#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cfloat>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef long long li;
typedef unsigned int uint;
typedef unsigned long long ull;

#define y1 botva
void Solution(int test);

int main()
{
#ifdef DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#else
#endif
	int ts; scanf("%d", &ts);
	for (int i = 1; i <= ts; i++)
		Solution(i);
	return 0;
}

int n, w, a[10200];
multiset<int> all;

void Solution(int test)
{
	scanf("%d%d", &n, &w);
	all.clear();
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]), all.insert(a[i]);
	int ans = 0;
	while (all.size() > 1)
	{
		ans++;
		int v = *(all.rbegin());
		multiset<int>::iterator it = all.end(); --it;
		all.erase(it);
		it = all.upper_bound(w - v);
		if (it == all.begin()) continue;
		--it; all.erase(it);
	}
	ans += all.size();
	printf("Case #%d: %d\n", test, ans);
}
