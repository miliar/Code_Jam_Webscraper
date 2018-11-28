#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>

#define INF 2e9
#define mp make_pair
#define pb push_back

using namespace std;

int a, b, k;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tt;
	cin >> tt;
	for (int tc = 0; tc < tt; tc++)
	{
		cout << "Case #" << tc + 1 << ": ";
		cin >> a >> b >> k;
		int ans = 0;
		for (int i = 0; i < a; i++)
		for (int j = 0; j < b; j++)
		{
			if ((i & j) < k) 
				ans++;
		}
		cout << ans;
		cout << endl;
	}
	return 0;
}