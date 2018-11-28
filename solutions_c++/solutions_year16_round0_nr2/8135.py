#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair< int , int >
#define vii vector< int >
#define ff first
#define ss second
#define rep(i,n) for(int i=0;i<n;i++)
#define frep(i , a , b) for(int i = a;i <= b;i++)
#define fast cin.sync_with_stdio(0);cin.tie(0);
#define CASES int t;cin >> t;while(t--)
#define FI freopen ("in.txt", "r", stdin)
#define FO freopen ("out.txt", "w", stdout)

const int MOD = 1e9 + 7;

int main()
{
	FI;
	FO;
	int t;
	cin >> t;
	frep(j, 1, t)
	{
		cout << "Case #" << j << ": ";
		string s;
		cin >> s;
		int ans = 0;
		int i = 1;
		if (s[0] == '-')
		{
			ans++;
			while(i<s.size()&&s[i]!='+')
				i++;
		}
		while (i < s.size())
		{
			int f = 0;
			while (i < s.size() && s[i] == '+')
				i++;
			// cout<<i<<"here\n";
			while (i < s.size() && s[i] == '-') {
				i++; f++;
			}
			if (f)
				ans += 2;
		}
		cout<<ans<<"\n";
	}
	return 0;
}