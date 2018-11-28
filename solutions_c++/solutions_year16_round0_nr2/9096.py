/* [theMighty] Deathsurgeon (Rupesh Maity)
* 3rd year, B.Tech in IT
* IIIT Allahabad
*/

#define _CRT_SECURE_NO_WARNINGS

#include <bits/stdc++.h>

#define ll long long
#define pii pair<int, int>

#define MOD 1000000007
#define MAX 100001
#define sd(x) scanf("%d", &x)

using namespace std;

int main()
{
#ifdef _MSC_VER
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		string str;

		cin >> str;

		char c = '+';
		int ans = 0;

		for (int i = str.size() - 1; i >= 0; i--) {
			if (str[i] != c) {
				++ans;
				c = str[i];
			}
		}

		cout << ans << endl;
	}

	return 0;
}