#include <bits/stdc++.h>
using namespace std;
using uint = unsigned int;
using ll = long long;
using pii = pair<int, int>;
#define dbg(x) cerr<<#x": "<<(x)<<'\n'
#define dbg_v(x, n) cerr<<#x"[]: ";for(long long _=0;_<n;++_)cerr<<(x)[_]<<' ';cerr<<'\n'
#define all(v) v.begin(), v.end()
#define NMAX 

void flip(char *s, int l, int r)
{
	while(l <= r) s[l] = (s[l] == '-' ? '+' : '-'), ++l;
}

bool ok(char *s)
{
	for(int i = 0; s[i]; ++i)
		if(s[i] == '-')
			return false;
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int t, tt, i, k, nr;
	char s[1010];

	cin >> t;
	for(tt = 1; tt <= t; ++tt)
	{
		cin >> s >> k;
		for(nr = 0, i = 0; s[i + k - 1]; ++i)
		{
			if(s[i] == '-') flip(s, i, i + k - 1), ++nr;
		}

		cout << "Case #" << tt << ": ";
		if(ok(s)) cout << nr << '\n';
		else cout << "IMPOSSIBLE\n";
	}

	return 0;
}