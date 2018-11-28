#include <bits/stdc++.h>
using namespace std;
const int oo = int(1e9) + 1;

int n, a[1010];

int main()
{
	freopen("b-large.in", "r", stdin); 
	freopen("b-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		cin >> n;
		int ans = 0;
		
		for (int i = 1; i <= n; i++) cin >> a[i];
		
		for (int i = 1, l = 0, r = n + 1; i <= n; i++)
		{
			int id, minA = oo;
			for (int j = l + 1; j < r; j++)
				if (a[j] < minA)
				{
					minA = a[j];
					id = j;
				}
				
			if (r - id < id - l)
			{
				for (int j = id + 1; j < r; j++) 
				{
					swap(a[j - 1], a[j]);
					ans++;
				}
				r--;
			}
			else
			{
				for (int j = id - 1; j > l; j--)
				{
					swap(a[j + 1], a[j]);
					ans++;
				}
				l++;
			}
		}
		
		printf("Case #%d: %d\n", noTest, ans);
	}
}
