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
#include <cstring>
#include <climits>
#include <cassert>
#include <unordered_map>


using namespace std;
typedef long long ll;
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define EPS 1E-9
#define INF 1E12
#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

typedef pair<int, int> PII;

ll power(ll a, ll b)
{
	ll ans = 1;
	while (b)
	{
		if (b & 1ll) ans *= a;
		a *= a;
		b >>= 1;
	}
	return ans;
}

ll toll(string x)
{
	ll ans = 0;
	for (char v : x)
	{
		ans = ans * 10 + v - '0';
	}
	return ans;
}

ll solve(ll n)
{
	if (n <= 19) return n;
	char N[50];
	ll ans = 1;
	sprintf(N, "%lld", n);
	string s(N), t;
	t = s;
	reverse(t.begin(), t.end());
	ll a, b, c, d;
	int l = s.length();

	for (int i = 1; i < l; i++)
	{
		if (i == 1) ans += 9;
		else ans += power(10, i / 2) + power(10, (i + 1) / 2) - 1;
	}

	if (s[0]>'1')
	{
		a = toll(s.substr(l / 2));
		b = toll(t.substr(l - l / 2));
		//c = toll(s.substr(l / 2 + 1));
		//d = toll(t.substr(l - l / 2 - 1));
		//ans += min(a + b, c + d);
		ans += a + b;
	}
	else
	{
		a = toll(s.substr(l / 2));
		b = toll(t.substr(l - l / 2));
		ll tmp = toll(s.substr(1));
		ans += min(a + b, tmp);
	}

	return ans;
}


int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++)
	{
		printf("Case #%d: ", cs);
		ll n;
		cin >> n;
		ll ans;
		if (n % 10 == 0)
			ans = solve(n - 1) + 1;
		else ans = solve(n);
		cout << ans << endl;
	}


	return 0;
}