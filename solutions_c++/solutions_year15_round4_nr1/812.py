/*
ID: keyvank2
TASK: combo
LANG: C++
*/

#include <bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define FOR(i,j,k) for(int i = j; i < (int)(k); i++)
#define FORV(i, v) FOR(i, 0, ((v).size()))
#define REP(i,j,k) for(int i = j; i >= (int)(k); i--)
#define setmax(i) const int maxn = (int) i;
#define setmod(i) const int MOD = (int) i;
#define all(a) a.begin(),a.end()
#define autodef(x,v) typeof(v) x = (v)
#define autoref(x,v) typeof(v)& x = (v)
#define forit(it, c) for (autodef(it, ((c).begin())); it != ((c).end()); ++it)

//typedef complex<double> Point;
//#define X real()
//#define Y imag()

using namespace std;

//ifstream fin("");
//ofstream fout("");
//#define cin fin
//#define cout fout

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;
typedef pair<pii,int> ppi;
typedef pair<pll,ll> ppl;
typedef pair<int,pii> pip;
typedef pair<ll,pll> plp;
typedef pair<pii,pii> ppp;

const int INF = (int) 2e9;
const ll INFL = (ll) 9e18;
const int MAXINT = ((~0) ^ (1 << 31));
const ll MAXLL = ((~0) ^ ((ll)1 << 63));

template<class T> inline T pow2(T a) { return a*a;}
template<class T> inline bool mineq(T& a, T b){return (a > b) ? (a=b, true) : false;}
template<class T> inline bool maxeq(T& a, T b){return (a < b) ? (a=b, true) : false;}

//srand (time(NULL));

setmax(111);

int l[maxn][maxn], r[maxn][maxn], u[maxn][maxn], d[maxn][maxn], id, n, m;
int num[maxn][maxn];
char grid[maxn][maxn];

void pre()
{
    id = 1;
    FOR(i,0,maxn)
    {
	FOR(j,0,maxn)
	{
	    l[i][j] = -1;
	    r[i][j] = -1;
	    u[i][j] = -1;
	    d[i][j] = -1;
	    num[i][j] = -1;
	}
    }
}

int solve()
{
    pre();

    cin >> n >> m;
    FOR(i,0,n)
    {
	FOR(j,0,m)
	{
	    cin >> grid[i][j];
	    if(grid[i][j] != '.')
		num[i][j] = id++;
	}
    }

    FOR(i,0,n)
    {
	int now = -1;
	FOR(j,0,m)
	{
	    l[i][j] = now;
	    maxeq(now,num[i][j]);
	}
	now = -1;
	REP(j,m-1,0)
	{
	    r[i][j] = now;
	    maxeq(now,num[i][j]);
	}
    }

    FOR(j,0,m)
    {
	int now = -1;
	FOR(i,0,n)
	{
	    u[i][j] = now;
	    maxeq(now,num[i][j]);
	}
	now = -1;
	REP(i,n-1,0)
	{
	    d[i][j] = now;
	    maxeq(now,num[i][j]);
	}
    }

    //cerr << "* " << u[0][0] << endl;

    int ans = 0;
    FOR(i,0,n)
    {
	FOR(j,0,m)
	{
	    if(l[i][j] == -1 && r[i][j] == -1 && d[i][j] == -1 && u[i][j] == -1 && grid[i][j] != '.')
	    {
		cout << "IMPOSSIBLE";
		return 0;
	    }
	    if(grid[i][j] == '^' && u[i][j] == -1)
		ans++;
	    if(grid[i][j] == '<' && l[i][j] == -1)
		ans++;
	    if(grid[i][j] == '>' && r[i][j] == -1)
		ans++;
	    if(grid[i][j] == 'v' && d[i][j] == -1)
		ans++;
	}
    }
    cout << ans;
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int t;
    cin >> t;
    FOR(i,1,t+1)
    {
	cout << "Case #" << i << ": ";
	solve();
	cout << endl;
	cerr << i << "Done" << endl;
    }
}
