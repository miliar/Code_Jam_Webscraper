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

int T, fl, fl1, n, m, x, y, p[111], t[111][111][2], z[111][111];
pair <pii, int> h[111];

void dfs(pair <pii, int> v, int c)
{
	if (v.X.X < 1 || v.X.X > n || v.X.Y < 1 || v.X.Y > m || t[v.X.X][v.X.Y][v.Y] == c)
		return;
	t[v.X.X][v.X.Y][v.Y] = c;
	if (v.Y)
	{
		dfs(mp(mp(v.X.X - 1, v.X.Y), 0), c);
		if (z[v.X.X][v.X.Y] == 0)
			dfs(mp(mp(v.X.X, v.X.Y - 1), z[v.X.X][v.X.Y - 1]), c);
		else
			dfs(mp(mp(v.X.X, v.X.Y + 1), !z[v.X.X][v.X.Y + 1]), c);
	}
	else
	{
		dfs(mp(mp(v.X.X + 1, v.X.Y), 1), c);
		if (z[v.X.X][v.X.Y] == 0)
			dfs(mp(mp(v.X.X, v.X.Y + 1), !z[v.X.X][v.X.Y + 1]), c);
		else
			dfs(mp(mp(v.X.X, v.X.Y - 1), z[v.X.X][v.X.Y - 1]), c);
	}
	return;
}

int main()
{
	fin("t.in");
	fout("t.out");
	sync;
	cin >> T;
	ff(numT, 1, T)
	{
		fl = 0;
		cin >> n >> m;
		fi(1, n + m)
		{
			cin >> x >> y;
			p[x] = y;
			p[y] = x;
		}
		fi(1, m)
		{
			h[i] = mp(mp(1, i), 1);
		}
		
		fi(1, m)
		{
			h[n + m + i] = mp(mp(n, m - i + 1), 0);
		}

		cout << "Case #" << numT << ":" << endl;
		ff(mask, 0, (1 << (n * m)) - 1)
		{
			fl1 = 1;
			fi(1, n)
			{
				fj(1, m)
				{
					t[i][j][0] = 0;
					t[i][j][1] = 0;
					z[i][j] = ((mask & (1 << ((i - 1) * m + j - 1))) > 0);
				}
			}
			fi(1, n)
			{
				h[m + i] = mp(mp(i, m), 0);
				if (z[i][m])
					h[m + i].Y = 1;
			}
			fi(1, n)
			{
				h[n + 2 * m + i] = mp(mp(n - i + 1, 1), 0);
				if (!z[n - i + 1][1])
					h[n + 2 * m + i].Y = 1;
			}

			fi(1, 2 * (n + m))
			{
				dfs(h[i], i);
				if (t[h[p[i]].X.X][h[p[i]].X.Y][h[p[i]].Y] != i)
				{
					/*
					if (mask == 4)
					{
						cout << i << " " << p[i] << endl;
						cout << h[i].X.X << " " << h[i].X.Y << " " << h[i].Y << endl;
						cout << h[p[i]].X.X << " " << h[p[i]].X.Y << " " << h[p[i]].Y << endl;
					}
					*/
					fl1 = 0;
					break;
				}
			}
			if (fl1)
			{
				fl = 1;
				break;
			}
		}
		if (!fl)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		fi(1, n)
		{
			fj(1, m)
			{
				if (z[i][j])
					cout << "\\";
				else
					cout << "/";
			}
			cout << endl;
		}
	}
	return 0;
}
