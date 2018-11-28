// In the name of Allah

#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for ( int i = a; i < b; i ++ )
#define rep(i,n) for ( int i = 0; i < n; i ++ )
#define repd(i,n) for ( int i = n; i >= 0; i -- )
#define PI 3.14159265358979323846
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int max_n = 1000;
int D, p[max_n];

int find (int special)
{
	int lb = 0, ub = 1001;
	while ( ub-lb > 1 )
	{
		int mid = lb+ub >> 1;
		int need = 0;
		rep (i, D)
			need += (p[i]-1)/mid;
		if ( need <= special )
			ub = mid;
		else
			lb = mid;
	}
	return ub+special;
}

int main()
{
	int T;
	cin >> T;
	rep (t, T)
	{
		scanf ("%d", &D);
		rep (i, D)
		scanf ("%d", &p[i]);
		int sq = sqrt(2000);
		int ans = 10000;
		rep (i, sq)
			ans = min (find(i), ans);
		printf ("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
