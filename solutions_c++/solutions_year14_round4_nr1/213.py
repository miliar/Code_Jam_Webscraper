#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("a-large.in", "r", stdin); 
	freopen("a-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		int a[10100], n, sz, ans = 0;
		cin >> n >> sz;
		for (int i = 0; i < n; i++) cin >> a[i];
		
		sort(a, a + n);
		for (int i = 0, j = n - 1; i <= j; i++)
		{
			while (i < j && a[i] + a[j] > sz) ans++, j--;
			ans++;
			if (i >= j) break;
			j--;
		}
		
		printf("Case #%d: %d\n", noTest, ans);
	}
}
