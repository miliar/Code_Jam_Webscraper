#include <bits/stdc++.h>

#define fi first
#define se second
#define ll long long
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

using namespace std;

int t, n, sz = 1;

string s;

int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	cin >> t;
	
	while (t--)
	{
		cin >> n >> s;
		
		int ans = 0, sm = 0;
		
		for (int i = 0; i <= n; i++)
		{
			if (sm < i)
				ans+=i-sm, sm+=i-sm;
			
			sm += s[i]-48;
		}
		
		printf("Case #%d: %d\n", sz, ans), sz++;
	}
}

