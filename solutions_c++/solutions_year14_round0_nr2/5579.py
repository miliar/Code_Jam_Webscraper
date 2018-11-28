//Besmellah
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define pb push_back
#define SQR(x) ((x) * (x))
#define SZ(x) ((int)((x).size()))
#define ALL(x) (x).begin(), (x).end()
#define debug(x) cerr << #x << " = " << x << endl
#define FOR(i, a, n) for(__typeof(n) i = (a); i <= (n); i++)
#define FORD(i, n, a) for(__typeof(n) i = (n); i >= (a); i--)
#define INF (1000 * 1000 * 1000)
#define MAXN 100010

int t;
long double c, f, x;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	cout.precision(7);
	FOR (tt, 1, t)
	{
		cin >> c >> f >> x;
		long double s = 2, p = 0, tm = 0, ans = INF;
		FOR (j, 1, 1000010)
		{
			ans = min(ans, tm + (x - p) / s);
			tm += (c - p) / s;
			p = 0;
			s += f;
		}
		cout << "Case #" << tt << ": " << fixed << ans << endl;
	}
	return 0;
}