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

int t, r1, r2;
int row[2][20];

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	FOR (tt, 1, t)
	{
		cin >> r1;
		FOR (i, 1, 4)
			FOR (j, 1, 4)
			{
				int a;
				cin >> a;
				row[0][a] = i;
			}
		cin >> r2;
		FOR (i, 1, 4)
			FOR (j, 1, 4)
			{
				int a;
				cin >> a;
				row[1][a] = i;
			}
		int cnt = 0;
		int ans = -1;
		FOR (i, 1, 16)
			if (row[0][i] == r1 && row[1][i] == r2)
			{
				cnt++;
				ans = i;
			}
		cout << "Case #" << tt << ": ";
		if (cnt == 1)
			cout << ans << endl;
		else if (cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}