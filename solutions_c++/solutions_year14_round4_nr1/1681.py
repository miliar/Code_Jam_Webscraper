#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <ctime>
#include <iterator>
#include <cstdlib>

using namespace std;

#define pb push_back
#define rs resize
#define mp make_pair
#define ass assign
#define sort(a) sort((a).begin(), (a).end())
#define reverse(a) reverse((a).begin(), (a).end())
#define sz(a) (a).size()
#define ms(a, x) memset(a, x, sizeof(a))
#define sf scanf
#define pf printf

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <vvi> vvvi;
typedef vector <ll> vl;
typedef vector <vl> vvl;
typedef vector <vvl> vvvl;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <vvb> vvvb;
typedef vector <string> vs;
typedef vector <vs> vvs;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <vii> vvii;
typedef pair <ll, ll> pll;
typedef vector <pll> vll;
typedef vector <vll> vvll;

void solve()
{
	int n, x;
	cin >> n >> x;
	multiset <int> a;
	for (int i = 0; i < n; ++i)
	{
		int y;
		cin >> y;
		a.insert(y);
	}
	int ans = 0;
	while (!a.empty())
	{
		int u = *a.rbegin();
		a.erase(a.find(u));
		ans++;
		multiset <int> ::iterator i = a.upper_bound(x - u);
		if (i == a.begin())
		{
			continue;
		}
		i--;
		a.erase(a.find(*i));
		continue;
	}
	cout << ans << endl;
	return;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		pf("Case #%d: ", i);
		solve();
	}
}