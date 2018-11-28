#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, ans;
	string s;
	cin >> t;
	for(int g=0;g<t;g++)
	{
		cin >> s;
		n=s.length();
		ans=0;
		for(int i=0;i<n-1;i++)
		{
			if(s[i]!=s[i+1])
				ans++;
		}
		if(s[n-1]=='-')
			ans++;
		cout << "Case #" << g+1 << ": " << ans << "\n";
	}
}
