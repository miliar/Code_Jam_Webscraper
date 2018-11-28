#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#define mp(x, y) make_pair(x, y)

using namespace std;

typedef long long ll;

const int INF = int(1e9) + 7;

int t, a[2000], cnt[2000], n, d[2000][2000];
string s;



int main()
{
	freopen("/Users/user/Downloads/B-large.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> t;
	int maxn = 1005;
	for(int j = 1; j <= maxn; j++)
		for(int i = 2; i <= maxn; i++)
			d[i][j] = INF;
	
	for(int j = 1; j <= maxn; j++)
		for(int i = 1; i <= j; i++)
			d[i][j] = 0;
	
	for(int j = 1; j <= maxn; j++)
		for(int i = j; i <= maxn; i++)
			for(int k = 1; k < i; k++)
				d[i][j] = min(d[i][j], d[k][j] + d[i - k][j] + 1);
	
	for(int q = 0; q < t; q++)
	{
		cin >> n;
		int maxn = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> a[i];
			maxn = max(maxn, a[i]);
		}
		
		int res = INF;
		for(int i = 1; i <= maxn; i++)
		{
			int sum = i;
			for(int j = 0; j < n; j++)
				sum += d[a[j]][i];
			res = min(res, sum);
		}
		printf("Case #%d: %d\n", q + 1, res);
		for(int i = 0; i <= 1010; i++)
			a[i] = 0;
	}
	
	return 0;
}
