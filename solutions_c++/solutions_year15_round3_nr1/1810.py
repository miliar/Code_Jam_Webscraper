#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
#pragma warning (disable : 4996)
typedef long long ll;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, bk;
	cin >> t;
	for (bk = 1; bk <= t; bk++)
	{
		cout << "Case #" << bk << ": ";
		int r, c, w, ans, k;
		cin >> r >> c >> w;
		if (c%w == 0)
			k = 0;
		else
			k = 1;
		ans = r*c;
		ans = ans / w;
		ans = ans + w - 1 + k;
		cout << ans;
		cout << endl;
	}
	return 0;
}