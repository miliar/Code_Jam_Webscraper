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

int n, m, p[10];
vector<string> s, all;
bool was[10];
int go[100][26], sz, ans, cnt;

void push(const string &s)
{
	int cur = 0;
	for (int i = 0; i < s.length(); i++)
	{
		int v = (int)(s[i] - 'A');
		if (go[cur][v] == -1)
		{
			fill(go[sz], go[sz] + 26, -1);
			go[cur][v] = sz++;
		}
		cur = go[cur][v];
	}
}

int gettrie()
{
	sz = 1; fill(go[0], go[0] + 26, -1);
	for (int i = 0; i < all.size(); i++)
		push(all[i]);
	return sz;
}

void check()
{
	for (int i = 0; i < m; i++)
		was[i] = false;
	for (int i = 0; i < n; i++)
		was[p[i]] = true;
	for (int i = 0; i < m; i++)
		if (!was[i]) return;
	int cur = 0;
	for (int i = 0; i < m; i++)
	{
		all.clear();
		for (int j = 0; j < n; j++)
			if (p[j] == i)
				all.push_back(s[j]);
		cur += gettrie();
	}
	if (cur > ans)
	{
		ans = cur, cnt = 1;
	}
	else if (cur == ans) cnt++;
}

void solve(int x)
{
	if (x == n) {
		check(); return;
	}
	for (int i = 0; i < m; i++)
		p[x] = i, solve(x + 1);
}

void Solution(int test)
{
	cin >> n >> m;
	s.resize(n);
	for (int i = 0; i < n; i++)
		cin >> s[i];
	ans = -1; cnt = 0;
	solve(0);
	cout << "Case #" << test << ": " << ans << " " << cnt << endl;
}
