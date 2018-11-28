#include <bits/stdc++.h>

#define TASK ""
#define sqr(x) ((x)*(x))
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
using namespace std;
const ll INFLL = numeric_limits<long long>::max();
const ll INFINT = numeric_limits<int>::max();
const ld EPS = 1e-7;
const ll MOD = 1e9 + 7LL;
const ll MAXN = 250000;

int run()
{
	ll n;
	cin >> n;
	string s;
	for(int q=0;q<n;q++)
	{
		cin >> s;
		ll ans=0;
		for(int i=1;i<s.size();i++)
		{
			if(s[i]!=s[i-1])
			{
				ans++;
			}
		}
		if(s[s.size()-1]=='-')ans++;
		cout << "Case #" << q+1 << ": " << ans << endl;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

#ifdef LOCAL
#ifdef STRESS
	freopen("input.txt","w",stdout);



#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if(strcmp(TASK,"")!=0)
	{
		freopen(TASK".in", "r", stdin);
		freopen(TASK".out", "w", stdout);
	}
#endif

	run();

	return 0;
}