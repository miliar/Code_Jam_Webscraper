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
const dbl eps = (dbl) 1e-7;
const int mod = (int) 1000000007;
const int maxn = (int) 1e5 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0))

int T, n, k, y;
dbl p[222], r[222], d[222][222];
dbl rans, ans;

int main()
{
	fin("t.in");
	fout("t.out");
	cout<<fixed<<setprecision(10);
	sync;
	cin >> T;
	ff(numT, 1, T)
	{
		cin >> n >> k;
		k /= 2;
		fi(1, n)
		{
			cin >> p[i];
		}
		sort(p + 1, p + n + 1);
		ans = 0;
		fq(0, 2 * k)
		{
			fi(1, q)
			{
				r[i] = p[i];
			}
			ei(n, n - (2 * k - q) + 1)
			{
				r[q + n - i + 1] = p[i];
			}
			clean(d);
			d[0][0] = 1;
			ri(0, 2 * k)
			{
				fj(0, k)
				{
					y = i - j;
					if (y < 0 || y > k)
						continue;
					d[j][y + 1] = d[j][y + 1] + d[j][y] * r[i + 1];
					d[j + 1][y] = d[j + 1][y] + d[j][y] * ((dbl)1 - r[i + 1]);
				}
			}
			ans = max(ans, d[k][k]);
		}
		/*
		rans = 0;
		ff(mask, 0, (1 << n) - 1)
		{
			y = 0;
			fi(1, n)
			{
				if (mask & (1 << (i - 1)))
				{
					y++;
					r[y] = p[i];
				}
			}
			if (y != 2 * k)
				continue;

			clean(d);
			d[0][0] = 1;
			ri(0, 2 * k)
			{
				fj(0, k)
				{
					y = i - j;
					if (y < 0 || y > k)
						continue;
					d[j][y + 1] = d[j][y + 1] + d[j][y] * r[i + 1];
					d[j + 1][y] = d[j + 1][y] + d[j][y] * ((dbl)1 - r[i + 1]);
				}
			}
			rans = max(rans, d[k][k]);
		}
		if (abs(rans - ans) > eps)
		{
			cout << ans << " " << rans << endl;
			cout << n << " " << 2 * k << endl;
			fi(1, n)
			{
				cout << p[i] << " ";
			}
			cout << endl;
			return 0;
		}
		*/
		cout << "Case #" << numT << ": " << ans << endl;
	}
	return 0;
}
