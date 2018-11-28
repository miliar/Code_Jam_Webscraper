/*
  /\     /\
  | ).|.( |
  |  >-<  |
  =========
It's AdilkhanKo miaaaaaau
*/
#include<bits/stdc++.h>

#define ll long long
#define pb push_back
#define endl "\n"
#define foreach(it, S) for(__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define mp make_pair
#define f first
#define s second
#define name ""
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int MaxN = int (2e6) + 256;
const int INF = int(1e9);
const int mod = (int)(1e9) + 7;
const double pi = 3.1415926535897932384626433832795;
ll n, m, t, ans, a[MaxN];

int main () { _
	#ifdef ONLINE_JUDGE
//		freopen (name".in","r",stdin);
//		freopen (name".out","w",stdout);
	#else
		freopen (".in","r",stdin);
		freopen (".out","w",stdout);
	#endif
	cin >> t;
	for(int T = 1; T <= t; T++){
		cout << "Case #" << T << ": ";
		string s; cin >> s;
		ll ans = 0;
		if(s[s.size() - 1] == '-')ans++;
		for(int i = 1; i < s.size(); i++){
			if(s[i] != s[i - 1])ans++;
		}
		cout << ans << endl;
	}
return 0;
}                                    