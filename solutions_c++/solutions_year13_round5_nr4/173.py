#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;

double f[1 << 20];
bool done[1 << 20];
int n;

double dp(int mask)
{
	if (!mask) return 0;
	if (done[mask]) return f[mask];
	done[mask] = 1;
	f[mask] = 0;
	int prev;
	
	for (int i = 0; i < n; i++)
		if (mask >> i & 1)
		{
			prev = i; break;
		}
	
	for (int i = n - 1; i >= 0; i--)
	{
		if (mask >> i & 1) prev = i;
		f[mask] += dp(mask ^ 1 << prev) + n - (prev + n - i) % n;
	}
	
	f[mask] /= n;
	return f[mask];
}

int main()
{
	freopen("dsmall.in", "r", stdin); 
	freopen("dsmall.out", "w", stdout);
	int test;
	cin >> test;
	for (int itest = 1; itest <= test; itest++)
	{
		string s;
		cin >> s;
		n = s.size();
		memset(done, 0, sizeof(done));
		int mask = 0;
		for (int i = 0; i < n; i++) mask |= (s[i] == '.') << i;
		printf("Case #%d: %.12lf\n", itest, dp(mask));
	}
}
