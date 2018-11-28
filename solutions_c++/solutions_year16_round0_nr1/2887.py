#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
#define mem(x) memset(x,0,sizeof x)
#define LL long long
int n;
set<int> s;
inline void sift(int x)
{
	while (x)
	{
		int k = x % 10;
		x /= 10;
		s.insert(k);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		cin >> n;
		s.clear();
		if (n == 0){ printf("Case #%d: INSOMNIA\n", kcase); continue; }
		else
		{
			int ans = 0;
			for (int i = 1; i <= 1000000; i++)
			{
				int u = i*n;
				if (s.size() == 10){ ans = (i-1)*n; break; }
				else
				{
					sift(u);
				}
			}
			printf("Case #%d: %d\n", kcase, ans);
		}
	}
	return 0;
}