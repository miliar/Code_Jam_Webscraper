#include <bits/stdc++.h>

#define fi first
#define se second
#define ll long long
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

using namespace std;

int t, r, c, n, ans;

bool f[20], v[20][20];

void tap(int x, int san)
{
	if (x == r*c)
	{
		if (san == n)
		{
			fill(v[0], v[20], 0);
			
			int a = 0, b = 0;
			for (int i = 0; i < r*c; i++)
			{
				v[a][b++] = f[i];
				
				if (b == c)
					b = 0, a++;
			}
			
			int j = 0;
			for (int i = 0; i < r; i++)
			{
				for (int h = 0; h < c; h++)
				{
					if (v[i][h] == 1)
					{
						if (i+1 < r && v[i+1][h] == 1)
							j++;
						
						if (h+1 < c && v[i][h+1] == 1)
							j++;
					}
				}
			}
			ans = min(ans, j);
		}
		return;
	}
	
	for (int i = 0; i < 2; i++)
	{
		if (i == 1)
		f[x] = i, tap(x+1, san+1);
		else
		f[x] = i, tap(x+1, san);
	}
}

int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d%d", &r, &c, &n);
		ans = 100000;
		tap(0, 0);
		printf("Case #%d: %d\n", i, ans);
	}
}

