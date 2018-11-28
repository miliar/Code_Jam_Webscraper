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

int sol()
{
	string s;
	cin >> s;

	int cnt = s[sz(s) - 1] == '-';

	forn(i, sz(s) - 1)
		cnt += s[i] != s[i + 1];

	return cnt;
}


int main()
{
	int t;
	cin >> t;

	forn(i, t)
	{
		cout << "Case #" << i + 1 << ": " << sol() << '\n';
	}
	return 0;
}