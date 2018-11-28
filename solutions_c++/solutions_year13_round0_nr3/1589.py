#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

vector<long long> f;
int n, ca;
long long x, y;
long long a[200];

bool pal(long long x)
{
	a[0] = 0;
	while (x != 0) {
		a[++a[0]] = x % 10;
		x /= 10;
	}
	for (int i = 1; i <= a[0]; i++) 
		if (a[i] != a[a[0] + 1 - i]) return false;
	return true;
}

int main()
{
	freopen("c.out", "w", stdout);
	f.clear();
	for (long long i = 0; i <= 10000000; i++) {
		if (!pal(i)) continue;
		if (!pal(i * i)) continue;
		f.push_back(i * i);
	}
	n = f.size();
	scanf("%d", &ca);
	for (int t = 1; t <= ca; t++) {
		cin >> x >> y;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (x > f[i]) continue;
			if (y < f[i]) continue;
			++ans;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

