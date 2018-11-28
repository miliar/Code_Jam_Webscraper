#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>

using namespace std;

#define mp make_pair
#define pp push_back
#define Sort(x) sort(x.begin(), x.end())
#define rep(i, x, y) for(int i = x; i < y; ++i)
#define Rep(i, x, y) for(int i = x; i <= y; ++i)
#define dRep(i, x, y) for(int i = x;i >= y; --i)
#define vi vector<int>
#define vvi vector<vector<int> >
#define ll long long
#define all(v) v.begin(),v.end()
#define ii pair<int, int>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'
#define MOD 1000000007

int main()
{
	int t, a, b, k;
	ll res;
	freopen("B-small-attempt0 (1).in", "r", stdin);
	freopen("lottery.txt", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		res = 0;
		cin >> a >> b >> k;
		rep(j, 0, a)
		{
			rep(l, 0, b)
			{
				if((j & l) < k)
					res++;
			}
		}

		cout << "Case #" << i << ": " << res << nl;
	}

	return 0;
}