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

int f[10];

void process(int x)
{
	while(x > 0)
	{
		f[x%10] = 1;
		x /= 10;
	}
}


int main()
{
	int n;
	freopen("inp", "r", stdin);
	freopen("op", "w", stdout);
	
	int t;
	cin >> t;
	rep(tc, 1, t+1)
	{
		cin >> n;
		cout << "Case #" << tc << ": ";
		if(n == 0)
		{
				cout << "INSOMNIA\n";
				continue;
		}
		rep(i, 0, 10) f[i] = 0;
		int x;
		for(x = n; x <= (1<<25); x += n)
		{
			process(x);
			bool ok = 1;
			rep(j, 0, 10)
			{
				if(!f[j]) ok = 0;
			}
			if(ok) break;
		}
		assert(x <= (1<<25));
		cout << x << endl;
	}
    return 0;
}    

