#include <bits/stdc++.h>

#define ft first
#define st second
#define mp make_pair
#define pb push_back
#define sz(n) int(n.size())


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int N = 1e5;
const int inf = 1e9 + 7;
const ll INF = 1e18 + 7;

int t;
string s;

int main ()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for (int q = 1; q <= t; q ++)
	{
		cin >> s;
		int n = sz(s);
		for (int i = sz(s) - 1; i >= 0; i --)
		{
			if (s[i] == '+') n --;
			else break;
		}
		int ans = 1;
		for (int i = 1; i < n; i ++)
		{
			if (s[i] != s[i - 1]) ans ++;
		}
		if (n == 0) ans = 0;
		printf("Case #%d: %d\n", q, ans);
	}
}