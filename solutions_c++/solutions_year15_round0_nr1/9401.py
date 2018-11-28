#include <stdio.h>
#include <iostream>
#include <string>
#define problem "test"
#define sort stable_sort
const int z = 1111;

using namespace std;
int n, t, ans, cnt, a[z];
string s;

int main()
{
    ios::sync_with_stdio(0);
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	freopen(problem".in", "r", stdin);
	freopen(problem".out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n >> s;
		for (int j = 0; j <= n; j++)
			a[j] = s[j] - '0';
		cnt = a[0];
		ans = 0;
		for (int j = 1; j <= n; j++)
		{
			ans += max(j - cnt, 0);
			cnt += max(j - cnt, 0) + a[j];
		}
		cout << "Case #" << i + 1 << ": " << ans << "\n"; 	
	}

	return 0;
}