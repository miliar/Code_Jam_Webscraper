#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define INF 999999999
using namespace std;
string invert(string h, int r)
{
	string s = h;
	for(int i=0;i<=r/2;i++)
	{
		swap(s[i], s[r-i]);
	}
	for(int i=0;i<=r;i++)
	{
		if(s[i] == '+') s[i] = '-';
		else s[i] = '+';
	}
	return s;
}

void solve()
{
	string s;
	cin >> s;
	int ans = 0;
	while(s.size() > 0)
	{
		int it = s.size() - 1;
		while(s[it] == '+') it--;
		if(it == s.size() - 1);
		else s = s.substr(0, it + 1);
		if(s.size() == 0) break;
		if(s[0] == '+')
		{
			int i = 0;
			while(s[i] == '+') s[i] = '-', i++;
			ans++;
		}
		else
		{
			s = invert(s, s.size()-1);
			ans++;
		}
	}
	cout << ans << "\n";
}

int main()
{
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++)
	{
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
