#include <bits/stdc++.h>
using namespace std;

#define jjs(i, s, x) for (int i = (s); i < int(x); i++)
#define jjl(i, x) jjs(i, 0, x)
#define ji(x) jjl(i, x)
#define jj(x) jjl(j, x)
#define jk(x) jjl(k, x)
#define jij(a, b) ji(a) jj(b)
#define ever ;;
#define foreach(x, C) for (auto& x : (C))
#define INF ((int) 1e9+10)
#define LINF ((ll) 1e16)
#define pb push_back
#define mp make_pair
#define nrint(x) int x; rint(x);
#define nrlong(x) long long x; rint(x);
#define rfloat(x) scanf("%lf", &(x))

#ifndef ONLINE_JUDGE
const bool DEBUG = true;
#define Db(x...)   ({ if (DEBUG) { cout << "Debug["; DB, #x, ":", x, "]\n"; } })
template<class T> void Dbrng(T lo, T hi, string note = "", int w = 0) {
  if (DEBUG) {  
    cout << "Debug[ ";
    if (!note.empty()) cout << setw(3) << note << " : ";
    for (; lo != hi; ++lo) cout << setw(w) << *lo << " ";
    cout << "]" << endl;
  }
}
struct Debugger { template<class T> Debugger& operator ,
  (const T & v) { cout << " " << v << flush; return *this; } } DB;
#else
const bool DEBUG = false;
#define Db(x...)
#endif

#define rint readInteger
template<typename T>
bool readInteger(T& x)
{
	char c,r=0,n=0;
	x=0;
	for (ever)
	{
		c=getchar();
		if ((c<0) && (!r))
			return(0);
		else if ((c=='-') && (!r))
			n=1;
		else if ((c>='0') && (c<='9'))
			x=x*10+c-'0',r=1;
		else if (r)
			break;
	}
	if (n)
		x=-x;
	return(1);
}

const int MOD = 1000000007;
typedef long long ll;
typedef pair<int, int> pi;

#define _L (idx*2+1)
#define _R (idx*2+2)
#define _M ((l+r)/2)

int N, D;
const int MX = 1e6+10;
int par[MX];
vector<int> children[MX];
int sal[MX];
int idxBegin[MX];
int idxEnd[MX];
int nxt;
const int TMX = MX * 4;
int active[TMX];
int laz[TMX];

void propagate(int idx, int l, int r)
{
	assert(l != r);
	laz[_L] += laz[idx];
	laz[_R] += laz[idx];
	laz[idx] = 0;
}

void rejig(int idx, int l, int r)
{
	assert(laz[idx] >= 0);
	if (laz[idx] > 0)
		active[idx] = r - l + 1;
	else if (l == r)
		active[idx] = 0;
	else
		active[idx] = active[_L] + active[_R];
}

void upd(int idx, int l, int r, int a, int b, int v)
{
	assert(l <= r);
	assert(idx < TMX);
	if (b < l || a > r)
		return;
	if (a <= l && b >= r)
	{
		laz[idx] += v;
		rejig(idx, l, r);
		return;
	}
	upd(_L, l, _M, a, b, v);
	upd(_R, _M+1, r, a, b, v);
	rejig(idx, l, r);
}

void upd(int x, int v)
{
	upd(0, 0, N-1, idxBegin[x], idxEnd[x], v);
}

void dfs(int i)
{
	idxBegin[i] = nxt++;
	foreach(o, children[i])
		dfs(o);
	idxEnd[i] = nxt - 1;
}

void mseq(int* arr, ll s, ll a, ll c, ll r)
{
	arr[0] = s;
	jjs(i, 1, N) arr[i] = (arr[i-1] * a + c) % r;
}

int main()
{
	nrint(T);
	jk(T)
	{
		rint(N); rint(D);
		ji(N) children[i].clear();
		assert(N <= MX);
		nrlong(S0);
		nrlong(As);
		nrlong(Cs);
		nrlong(Rs);
		nrlong(M0);
		nrlong(Am);
		nrlong(Cm);
		nrlong(Rm);
		mseq(sal, S0, As, Cs, Rs);
		mseq(par, M0, Am, Cm, Rm);
		jjs(i, 1, N) par[i] %= i;
		jjs(i, 1, N) children[par[i]].pb(i);
		nxt = 0;
		dfs(0);
		vector<pi> V;
		ji(N) V.pb({sal[i], i});
		sort(V.begin(), V.end());
		memset(active, 0, sizeof active);
		memset(laz, 0, sizeof laz);
		int idx = 0;
		int ans = 0;
		ji(N) upd(i, 1);
		ji(N)
		{
			upd(V[i].second, -1);
			while (V[i].first > V[idx].first + D)
				upd(V[idx++].second, 1);
			ans = max(ans, N - active[0]);
		}
		printf("Case #%d: %d\n", k+1, ans);
		fprintf(stderr, "Case #%d: %d\n", k+1, ans);
	}
}
