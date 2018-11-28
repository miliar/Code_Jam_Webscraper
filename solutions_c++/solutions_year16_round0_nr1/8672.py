#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < n; ++i)
#define sz(a) (int)a.size()
#define mp(a, b) make_pair(a, b)  
#define all(a) a.begin(), a.end()
#define pb(a) push_back(a)

#ifdef LOCAL   
#define pv(a) cout << #a << " = " << a << '\n';
#else
#define pv(a) ;                                 
#endif	
                           
using namespace std;
typedef long long ll;

const int MAXN = 100500;


bool used[MAXN];

bool check()
{
	forn(i, 10)
		if (!used[i])
			return false;
	return true;
}

void upd(ll x)
{
	while (x)
	{
		used[x % 10] = true;
		x /= 10;
	}
}

void solve(int t)
{
	forn(i, 10)
		used[i] = false;

	ll cur = 0;
	ll n;
	cin >> n;

	if (n == 0)
	{
		cout << "Case #" << t + 1 << ": INSOMNIA\n";
		return;
        }

	while (!check())
	{
		cur += n;
		upd(cur);
	}

	cout << "Case #" << t + 1 << ": " << cur << '\n';

}



int main()
{

	int t;
	cin >> t;
	forn(i, t)
		solve(i);
	return 0;
}