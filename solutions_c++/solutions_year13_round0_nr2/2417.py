#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair


typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int MAXN = 100 + 10;

int m, n, a[MAXN][MAXN];
int hr[MAXN], hc[MAXN];

bool check() {
	forn(i,m) forn(j,n) if (a[i][j] != min(hr[i], hc[j])) return false;
	return true;
}

void init() {
	fill(hr, hr+MAXN, 0);
	fill(hc, hc+MAXN, 0);
}

int main() {
        #ifdef LOCAL
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        #endif

        int ncas; cin >> ncas;
        forn(cas,ncas) {
        	cout << "Case #" << cas+1 << ": ";

        	cin >> m >> n;
        	init();
        	forn(i,m) forn(j,n) {
        		cin >> a[i][j];
        		hr[i] = max(hr[i], a[i][j]);
        		hc[j] = max(hc[j], a[i][j]);
        	}

        	cout << (check() ? "YES" : "NO") << endl;
        }




        return 0;
}

