/*
* @problem: The Last Word
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007LL
#define bitcnt(x) __builtin_popcount(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define ll long long int
#define mp(x, y) make_pair(x, y)
#define pii pair<int, int>
#define pll pair<ll, ll>
#define in(x) scanf("%lld", &x)
#define ind(x) scanf("%d", &x)
#define ins(x) scanf("%s", x)
#define pi acos(-1.0)

using namespace std;
string dp[1010];

int main()
{
	// #ifndef ONLINE_JUDGE
	// 	freopen("../input.txt", "r", stdin);
	// #endif
	// ios_base::sync_with_stdio(0);
    // cin.tie(0);
	int t, l, pos[1010];
	string s;
	string tmp, tmp1;
	cin >> t;
	for(int j = 1; j <= t; j++)
	{
		cin >> s;
		l = s.length();
		dp[0] = s.substr(0, 1);
		for(int i = 1; i < l; i++)
		{
			tmp = s[i] + dp[i - 1];
			tmp1 = dp[i - 1] + s[i];
			if(tmp.compare(tmp1) > 0)
				dp[i] = tmp;
			else
				dp[i] = tmp1;
			//dp[i] = max(tmp, tmp1);
		}
		cout << "Case #" << j << ": " << dp[l - 1] << endl;
	}
	return 0;
}