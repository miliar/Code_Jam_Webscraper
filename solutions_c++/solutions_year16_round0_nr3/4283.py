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



VI vec;

bool check(int base, string s)
{
	long long x = 0;
	int n = SZ(s);
	long long tmp = 1;
	for(int i = n-1; i >= 0; i--)
	{
		int val = (s[i] == '1');
		x = x + tmp *1ll* val;
		tmp = tmp*1ll*base;
	}
	long long w = 2;
	while(w*w <= x)
	{
		if(x%w == 0)
		{
			vec.pb(w);
			return 1;
		}
		w++;
	}
	return 0;
}

string getbinary(int x)
{
	string tmp = "";
	while(x)
	{
		tmp.pb('0' + x%2);
		x /= 2;
	}
	reverse(all(tmp));
	return tmp;
}

vector<string> jamcoin;
vector< VI > ans;

int main()
{
	freopen("inp", "r", stdin);
	freopen("op", "w", stdout);
	int t, n, j;
	cin >> t;
	rep(tc, 1, t+1)
	{
		cin >> n >> j;
		cout << "Case #" << tc << ": " << endl;
		
		rep(mask, 0, 1<<(n-2))
		{
			string tmp = getbinary(mask);
			while(SZ(tmp) != n-2)
				tmp = '0' + tmp;
				//	tmp.push_front('0');
			string s = '1' + tmp + '1';			
			//cout << s << endl;
			
			vec.clear();
			bool ok = 1;
			rep(base, 2, 11)
			{
				if(!check(base, s))
				{
					ok = 0; break;
				}
			}
			if(ok)
			{
				cout << s << " ";
				rep(i, 0, SZ(vec))
					cout << vec[i] << " ";
				cout << endl;
				jamcoin.pb(s);
				ans.pb(vec);
			}
			if(SZ(ans) == j) break;
		}
		
	}
    return 0;
}    

/*
	generate a string of size n both starting and ending at 1 such that
	which when converted in base 2-10, number is composite
	and we need to print that string + non-trivial divisor of number in each base		
*/
