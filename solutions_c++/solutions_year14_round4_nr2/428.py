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

int n, a[10100], lt[10100], rt[10100], p[10100];
vector<int> b;

void Solution(int test)
{
	//cerr << test << endl;
	scanf("%d", &n);
	int mi = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] > a[mi]) mi = i;
	}
	b.clear();
	for (int i = 0; i < n; i++)
		b.push_back(a[i]);
	sort(a, a + n);
	int ans = 0;
	for (int i = 0; i < n; i++)
	{
		int v = find(b.begin(), b.end(), a[i]) - b.begin();
		ans += min(v, n - 1 - i - v);
		b.erase(b.begin() + v);
	}
	printf("Case #%d: %d\n", test, ans);
}
