#include <bits/stdc++.h>

using namespace std;

#define fr(a, b, c) for(int a = b, __ = c; a < __; a++)
#define fe(a, b, c) for(int a = b, __ = c; a <= __; a++)

#define rp(a, b) fr(a, 0, b)

#define iter(c) __typeof((c).begin())
#define tr(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define iz(a) if(a == 0) { break; }

#define FASTIO ios_base::sync_with_stdio(0);

#define F first
#define S second

#define clr(a, b) memset(a, b, sizeof(a))

#define mp make_pair
#define pb push_back

#define sd(x) scanf("%d", &x)
#define sll(x) scanf("%lld", &x)
#define slf(x) scanf("%lf", &x)
#define sii(x) scanf("%d%d", &x.F, &x.S)
#define sc(x) scanf(" %c", &x)
#define ss(x) scanf(" %s", x)
#define sn(x) scanf(" %[^\n]", x)

#define sd1(a) scanf("%d", &a)
#define sd2(a,b) scanf("%d %d", &a, &b)
#define sd3(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sd4(a,b,c,d) scanf("%d %d %d %d", &a, &b, &c, &d)

#define dbg(x) cout << x << endl;
#define db2(x) cout << #x << " = " << x << endl;
#define _ << ", " <<
#define line(x) { fr(i, 0, x) putchar('-'); puts(""); }
#define hello dbg("hello");

template <class T1, class T2>
	ostream& operator<< (ostream& c, pair<T1, T2> p) { return c << "(" << p.F << ", " << p.S << ")"; }

template <class _T> inline string tostr(const _T& a){ ostringstream os(""); os << a; return os.str(); }
template <class T> inline T sqr(const T& x) { return x * x; }

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef vector<int> vi;

const int inf = 0x3f3f3f3f;
const double eps = 1e-7;

int n, m;
char ma[111][111];
bool fuck[5][111][111];
map<char, int> yay;

int main()
{
	yay['.'] = 4;
	yay['<'] = 0;
	yay['>'] = 1;
	yay['^'] = 2;
	yay['v'] = 3;
	
	int T;
	sd(T);
	fe(cas, 1, T)
	{
		clr(fuck, false); // no fucks given
		
		sd2(n, m);
		rp(i, n) rp(j, m) sc(ma[i][j]);

		rp(i, n)
		{
			int j = 0;
			while(j < m, ma[i][j] == '.') j++;
			if(j == m) continue;
			fuck[0][i][j] = true;
		}
		rp(i, n)
		{
			int j = m - 1;
			while(j >= 0, ma[i][j] == '.') j--;
			if(j < 0) continue;
			fuck[1][i][j] = true;
		}
		rp(j, m)
		{
			int i = 0;
			while(i < n, ma[i][j] == '.') i++;
			if(i == n) continue;
			fuck[2][i][j] = true;
		}
		rp(j, m)
		{
			int i = n - 1;
			while(i >= 0, ma[i][j] == '.') i--;
			if(i < 0) continue;
			fuck[3][i][j] = true;
		}
		
		bool imp = false;
		int ans = 0;
		rp(i, n) rp(j, m)
		{
			bool ok = false;
			rp(k, 4)
			{
				ok = ok || !fuck[k][i][j];
			}
			if(!ok) imp = true;
			
			if(fuck[yay[ma[i][j]]][i][j]) ans++;
		}
		
		printf("Case #%d: ", cas);
		if(imp) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}

