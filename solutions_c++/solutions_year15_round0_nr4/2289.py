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

int main()
{
	bool a [5][5][5];
	memset (a, false, sizeof a);
	a [1][1][1] = true;
	a [1][2][1] = a [1][2][2] = true;
	a [1][3][1] = true;
	a [1][4][1] = a [1][4][2] = true;
	a [2][2][1] = a [2][2][2] = true;
	a [2][3][1] = a [2][3][2] = a [2][3][3] = true;
	a [2][4][1] = a [2][4][2] = true;
	a [3][3][1] = a [3][3][3] = true;
	a [3][4][1] = a [3][4][2] = a [3][4][3] = a [3][4][4] = true;
	a [4][4][1] = a [4][4][2] = a [4][4][4] = true;
	
	int T;
	cin >> T;
	rep (t, T)
	{
		int X, R, C;
		cin >> X >> R >> C;
		if ( R > C )
			swap (R, C);
		string ans = a[R][C][X] ? "GABRIEL" : "RICHARD";
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	
	return 0;
}
