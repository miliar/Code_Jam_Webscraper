#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define XX first
#define YY second

const int MOD = 1e9 + 7;
const int INF = 1e9 + 9;
const int N = 10 + 7;

string p[N][3];
int per[] = {2, 0, 1};
char ch[] = {'R', 'S', 'P'};

void solve(int n, int i)
{
	if (n == 0)
	{
		if (i == 0)
			cout << "R";
		else if (i == 1)
			cout << "S";
		else
			cout << "P";
		return;
	}
	if (i == 2 || i == 0)
	{
		solve(n-1, i);
		solve(n-1, (i+1) % 3);
	}
	else
	{
		solve(n-1, (i+1) % 3);
		solve(n-1, i);
	}
}

int main()
{
	ios::sync_with_stdio(false);

	for (int j=0; j<3; j++)
		p[0][j] += ch[j];
	for (int i=1; i<N; i++)
		for (int j=0; j<3; j++)
			p[i][j] = min(p[i-1][j] + p[i-1][(j+1) % 3], p[i-1][(j+1) % 3] + p[i-1][j]);

	int __;
	cin >> __;
	for (int _=0; _<__; _++)
	{
		cout << "Case #" << _+1 << ": ";
		int n, r, s, t;
		cin >> n >> r >> t >> s;
		string ans;
		ans.clear();
		for (int i=0; i<3; i++)
		{
			int cnt[3] = {0};
			for (int j=0; j<1<<n; j++)
				if (p[n][i][j] == 'R')
					cnt[0] ++;
				else if (p[n][i][j] == 'S')
					cnt[1]++;
				else if (p[n][i][j] == 'P')
					cnt[2]++;
			if (cnt[0] == r && cnt[1] == s && cnt[2] == t && (ans.empty() || ans < p[n][i]))
				ans = p[n][i];
		}
		if (ans.empty())
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << "\n";
	}

	return 0;
}
