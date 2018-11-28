#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define er erase
#define bg begin()
#define ed end()
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
#define files(name) fin(name".in"); fout(name".out")
#define enter cout << "\n"
#define space cout << " "
#define endl "\n"
#define fi(st,n) for (int i = (st); i <= (n); i++)
#define fj(st,n) for (int j = (st); j <= (n); j++)
#define fk(st,n) for (int k = (st); k <= (n); k++)
#define fq(st,n) for (int q = (st); q <= (n); q++)
#define fw(st,n) for (int w = (st); w <= (n); w++)
#define ff(i, st, n) for (int (i) = (st); (i) <= (n); (i)++)
#define ei(st,n) for (int i = (st); i >= (n); i--)
#define ej(st,n) for (int j = (st); j >= (n); j--)
#define ek(st,n) for (int k = (st); k >= (n); k--)
#define ri(st,n) for (int i = (st); i < (n); i++)
#define rj(st,n) for (int j = (st); j < (n); j++)
#define rk(st,n) for (int k = (st); k < (n); k++)
#define rq(st,n) for (int q = (st); q < (n); q++)
#define rf(i, st, n) for (int (i) = (st); (i) < (n); (i)++)
#define clean(a) memset((a),0,sizeof (a))
#define sync ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define y1 dsklmlvmd

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ll inf = (ll) 1000000000000;
const dbl eps = (dbl) 1e-8;
const int mod = (int) 1000000007;
const int maxn = (int) 1e5 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0))

char c[11];
int a[11], a0[11], fl;
string ans[11], u[111][2];
int T, n;

string dzen(int x, int z)
{
	if (z == n)
	{
		a[x]--;
		u[z][0] = "";
		u[z][0] += c[x];
		return u[z][0];
	}
	u[z][0] = dzen(x, z + 1);
	if (x == 0)
		u[z][1] = dzen(2, z + 1);
	if (x == 1)
		u[z][1] = dzen(0, z + 1);
	if (x == 2)
		u[z][1] = dzen(1, z + 1);
//	cout << x << " " << z << " " << u[z][0] << " " << u[z][1] << " " << a[0] << " " << a[1] << " " << a[2] << endl;
	if (a[0] < 0 || a[1] < 0 || a[2] < 0)
		return "IMPOSSIBLE";
	if (u[z][0] < u[z][1])
		return u[z][0] + u[z][1];
	else
		return u[z][1] + u[z][0];
}

int main()
{
	fin("t.in");
	fout("t.out");
	sync;
	cin >> T;
	ff(numT, 1, T)
	{
		cin >> n;
		fi(0, 2)
		{
			cin >> a[i];
			a0[i] = a[i];
		}
		c[0] = 'R';
		c[1] = 'P';
		c[2] = 'S';
		fl = 0;
		fi(0, 2)
		{
			ans[i] = dzen(i, 0);
			if (ans[i] != "IMPOSSIBLE")
			{
				fl = 1;
			}
			fj(0, 2)
			{
				a[j] = a0[j];
			}
		}
		if (!fl)
		{
			cout << "Case #" << numT << ": IMPOSSIBLE" << endl;
			continue;
		}
		sort(ans + 1, ans + 3);
		fi(0, 2)
		{
			if (ans[i] != "IMPOSSIBLE")
			{
				cout << "Case #" << numT << ": " << ans[i] << endl;
				break;
			}
		}
	}
	return 0;
}
