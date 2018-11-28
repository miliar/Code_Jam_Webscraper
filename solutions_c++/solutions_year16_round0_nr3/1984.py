#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;
int T, n, m;
map<__int64, int> v;
int a[35], b[12], p[10] = { 2,3,5,7,11,13,17,19,23,29 };

bool divide(int base, int mod)
{
	int ans = 0;
	for (int i = n - 1; i >= 0; i--)
	{
		if (!a[i]) continue;
		int res = 1;
		for (int j = 0; j < i; j++) res = res*base%mod;
		ans = (ans + res) % mod;
	}
	return ans == 0;
}

bool check(__int64 num)
{
	v[num] = 1;
	for (int i = 0; i < n; i++) a[i] = num >> i & 1;
	for (int i = 2; i <= 10; i++)
	{
		__int64 now = 0;
		bool flag = 0;
		for (int j = 0; j < 10; j++)
		{
			int mod = p[j];
			if (divide(i, mod))
			{
				flag = 1;
				b[i] = mod;
				break;
			}
		}
		/*for (int j = n - 1; j >= 0; j--) now = now*i + a[j];
		for (int j = 0; j < 10; j++)
		{
			if (now%p[j] == 0)
			{
				flag = 1;
				b[i] = p[j];
				break;
			}
		}*/
		if (!flag) return 0;
	}
	for (int i = n - 1; i >= 0; i--) printf("%d", a[i]);
	for (int i = 2; i <= 10; i++) printf(" %d", b[i]);
	puts("");
	return 1;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> n >> m;
		__int64 l = 1ll << n - 1, r = 1ll << n;
		v.clear();
		printf("Case #%d:\n", t);
		while (m--)
		{
			__int64 now;
			do {
				now = (__int64)rand()*rand()*rand() % (r - l) + l;
				if ((now & 1) == 0) now++;
			} while (v.find(now) != v.end() || !check(now));
		}
	}
}
