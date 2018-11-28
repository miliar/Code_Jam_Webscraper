#include <iostream> 
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm> 
#include <cmath> 

#include <vector> 
#include <set>
#include <map>
#include <string>
#include <bitset>
#include <queue>
#include <unordered_map>
#include <sstream>


using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;
ll gcd(ll a, ll b)
{
	return b ? gcd(b, a%b) : a;
}

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		ll c, k, s;
		cin >> k >> c >> s;
		vector <ll> res;
		vector <ll> cc;
		cc.push_back(1LL);
		for (int i = 1; i < c; ++i)
		{
			cc.push_back(cc.back() * k);
		}
		ll cur = c - 1;
		ll pos = 0;
		for (ll i = 0; i < k; ++i)
		{
			if (cur < 0)
			{
				cur = c - 1;
				res.push_back(pos);
				pos = 0;
			}
			pos += i * cc[cur];
			cur--;
		}
		res.push_back(pos);
		printf("Case #%d: ",t + 1);
		if (res.size() > s)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			for (ll i = 0; i < res.size(); ++i)
			{
				cout << res[i] + 1 << ' ';
			}
			printf("\n");
		}
	}
	return 0;
}