#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 2000222
using namespace std;
typedef pair<int,int> pt;

int s[N], m[N], pr[N];
vector<int> v[N];

pair<int, int> q[N];

int p[N], sz[N];
int was[N];

int n, D;

int get(int x) {
	if (p[x] == x) return x;
	return p[x] = get(p[x]);
}

void unite(int x, int y) {
	x = get(x);
	y = get(y);
	if (x == y) return;
	sz[x] += sz[y];
	p[y] = x;
}

void add(int x) {
	if (p[pr[x]] != -1) unite(x, pr[x]);

	for (int i = 0; i < v[x].size(); i++) if (p[v[x][i]] != -1) unite(x, v[x][i]);
}

void del(int x) {
	if (was[x]) return;
	was[x] = 1;
	if (p[x] == -1) sz[x] = 0; else sz[get(x)]--;
	for (int i = 0; i < v[x].size(); i++) del(v[x][i]);
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> D;
		long long S0, As, Cs, Rs;
		long long M0, Am, Cm, Rm;
		cin >> S0 >> As >> Cs >> Rs;
		cin >> M0 >> Am >> Cm >> Rm;

		s[0] = S0;
		for (int i = 1; i < n; i++) s[i] = (s[i - 1] * 1ll * As + Cs) % Rs;

		m[0] = M0;
		for (int i = 0; i < n; i++) v[i].clear();
		pr[0] = 0;
		for (int i = 1; i < n; i++) {
			m[i] = (m[i - 1] * 1ll * Am + Cm) % Rm;
			pr[i] = m[i] % i;
			v[pr[i]].pb(i);
		}
		for (int i = 0; i < n; i++) q[i] = mp(s[i], i);
		sort(q, q + n);

		for (int i = 0; i < n; i++) p[i] = -1, sz[i] = 1;
		for (int i = 0; i < n; i++) was[i] = 0;

		int u = -1;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			while (u + 1 < n && q[u + 1].F - q[i].F <= D) {
				u++;
				p[q[u].S] = q[u].S;
				add(q[u].S);
			}
			if (i > 0) del(q[i - 1].S);

			if (p[0] != -1) ans = max(ans, sz[get(0)]);
		}

		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}