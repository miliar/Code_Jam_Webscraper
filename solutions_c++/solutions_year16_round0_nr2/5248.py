//amazing takes time, legendary requires patience
#include "bits/stdc++.h"
#define sd(n) scanf("%d", &(n))
#define rep(i, x, n) for (int i = x, _n = (n); i < _n; ++i)
#define repi(i, a) for(typeof((a).begin()) i = (a).begin(), _##i = (a).end(); i != _##i; ++i)
#define pra(v) repi(it, v) cout << *it << " "; cout << endl;
#define SZ(c) (int)(c).size()
#define lcm(a,b) (a*(b/__gcd(a,b)))
#define VI vector<int>
#define all(c) (c).begin(), (c).end()
#define allr(c) (c).rbegin(), (c).rend()
#define pb push_back
#define mii map<int, int>
#define pii pair<int, int>
#define pip pair<int, pii>
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define llu unsigned long long
#define CLR(p) memset(p, 0, sizeof(p))
#define SET(p) memset(p, -1, sizeof(p))
#define INF 0x3f3f3f3f
#define pi 3.141592653589793
#define debug 0
using namespace std;

const int MOD = 1e9+7;
const int MAX = 100010;
const double eps = 1e-8;

int main()
{
	int n;
	freopen("inp", "r", stdin);
	freopen("op", "w", stdout);
	string s;
	int t;
	cin >> t;
	rep(tc, 1, t+1)
	{
		cin >> s;
		cout << "Case #" << tc << ": ";
		int n = SZ(s);
		
		int cnt = 0;
		while(1)
		{
			bool ok = 1;
			rep(i, 0, n)
				if(s[i] == '-')
				{
					ok = 0;
					break;
				}
			if(ok) break;
			
			int idx = 0;
			if(s[0] == '+')
				while(s[idx] == '+') idx++;
			else
				while(s[idx] == '-') idx++;
			if(idx == 0)
			{
				cnt++;
				rep(i, 0, n) s[i] = '+';
				break;
			}
			
			reverse(s.begin(), s.begin() + idx);
			rep(i, 0, idx)
				if(s[i] == '+') s[i] = '-';
				else s[i] = '+';
			
			cnt++;
		}
		cout << cnt << endl;
	}
    return 0;
}    
