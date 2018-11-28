#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t;
string a, ans;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("al.out", "w",stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		cin >> a;
		ans = a[0];
		for (int i = 1; i < a.length(); i++)
		{
			if (a[i] >=ans[0])
				ans = a[i] + ans;
			else ans += a[i];
		}
		cout << ans << endl;
	}
	return 0;
}