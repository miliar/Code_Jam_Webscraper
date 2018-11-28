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

string p[] = {"ZERO", "SIX", "TWO", "EIGHT", "FOUR", "FIVE", "SEVEN", "THREE", "NINE", "ONE"};
int l[] = {0, 6, 2, 8, 4, 5, 7, 3, 9, 1};
string s;
int t, cnt[256];

void solve(int x)
{
	cin >> s;
	for (int i = 0; i < 256; i ++)
	{
	    cnt[i] = 0;
	}
	for (int i = 0; i < sz(s); i ++)
	{
		cnt[s[i]] ++;	
	}

	vector <int> ans;
	for (int i = 0; i < 10; i ++)
	{
		int cur = inf;
		for (int j = 0; j < sz(p[i]); j ++)
		{
			cur = min(cur, cnt[p[i][j]]);	
		}
		for (int j = 0; j < sz(p[i]); j ++)
		{
			cnt[p[i][j]] -= cur;
		}
		while (cur --)
		{
			ans.pb(l[i]);
		}
	}
	sort(ans.begin(), ans.end());

	cout << "Case #" << x << ": ";
	for (int i = 0; i < ans.size(); i ++)
	{
		cout << ans[i];
	}
	cout << endl;
}


int main ()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for (int i = 1; i <= t; i ++)
	{
		solve(i);
	}
}