// In the name of Allah

#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for (int i = (a); i < (b); i ++)
#define rep(i,n) for (int i = 0; i < (n); i ++)
#define repd(i,n) for (int i = (n); i >= 0; i --)
#define PI 3.14159265358979323846
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int max_n = 100+10;
char a [max_n][max_n];
int cnt [max_n][max_n];

int main()
{
	int t;
	cin >> t;
	rep (tt, t)
	{
		int n, m;
		cin >> n >> m;
		rep (i, n)
			rep (j, m)
				cin >> a[i][j];
		memset (cnt, 0, sizeof cnt);
		int ans = 0;
		rep (j, m)
			rep (i, n)
			{
				if ( a[i][j] == '^' )
					ans ++;
				if ( a[i][j] != '.' )
				{
					cnt [i][j] ++;
					break;
				}
			}
				
		rep (j, m)
			repd (i, n-1)
			{
				if ( a[i][j] == 'v' )
					ans ++;
				if ( a[i][j] != '.' )
				{
					cnt [i][j] ++;
					break;
				}
			}
			
		rep (i, n)
			rep (j, m)
			{
				if ( a[i][j] == '<' )
					ans ++;
				if ( a[i][j] != '.' )
				{
					cnt [i][j] ++;
					break;
				}
			}
		
		rep (i, n)
			repd (j, m-1)
			{
				if ( a[i][j] == '>' )
					ans ++;
				if ( a[i][j] != '.' )
				{
					cnt [i][j] ++;
					break;
				}
			}
		bool b = true;			
		rep (i, n)
			rep (j, m)
				if ( cnt[i][j] == 4 )
				{
					b = false;
					break;
				}
		if ( b )
			printf ("Case #%d: %d\n", tt+1, ans);
		else
			printf ("Case #%d: IMPOSSIBLE\n", tt+1);
	}
	
	return 0;
}
