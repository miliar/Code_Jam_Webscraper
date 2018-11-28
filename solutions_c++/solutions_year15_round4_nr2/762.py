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

setmax(1e5+10);
const string imp = "IMPOSSIBLE";

ld eps = 1e-9;

int n;
ld goalvol, goaltemp;
vector<pdd> cold, hot, warm;

ld lim1[maxn], lim2[maxn];

bool ok(ld maxtime)
{
    ld nowvol = 0;

    FOR(i,0,warm.size())
    {
	nowvol += maxtime*warm[i].ff;
    }
    
    FOR(i,0,cold.size())
	lim1[i] = maxtime*cold[i].ff;
    FOR(j,0,hot.size())
	lim2[j] = maxtime*hot[j].ff;
    
    FOR(i,0,cold.size())
    {
	FOR(j,0,hot.size())
	{
	    ld v2 = lim1[i] * (goaltemp-cold[i].ss)/(hot[j].ss-goaltemp);
	    if(v2 <= lim2[j] + eps)
	    {
		nowvol += lim1[i] + v2;

		lim1[i] = 0;
		lim2[j] -= v2;
		continue;
	    }

	    v2 = lim2[j] * (goaltemp-hot[j].ss)/(cold[i].ss-goaltemp);

	    nowvol += lim2[j] + v2;

	    lim1[i] -= v2;
	    lim2[j] = 0;
	}
    }
 //   cerr << "& " << nowvol << endl;
    return nowvol > goalvol;
}

void solve()
{
    cold.clear();
    hot.clear();
    warm.clear();

    cin >> n >> goalvol >> goaltemp;
    FOR(i,0,n)
    {
	ld r,t;
	cin >> r >> t;
	if(t < goaltemp - eps)
	    cold.pb(mp(r,t));
	else if(t > goaltemp + eps)
	    hot.pb(mp(r,t));
	else
	    warm.pb(mp(r,t));
    }

    if(warm.empty() && (cold.empty() || hot.empty()))
    {
	cout << imp;
	return;
    }

    ld lo = 0, hi = INF;
    while(hi - lo > eps)
    {
	ld mid = (lo+hi)/2;
//	cerr << "* " << mid << endl;
	if(ok(mid))
	    hi = mid;
	else
	    lo = mid;
    }

    cout << setprecision(10) << fixed << lo;
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
