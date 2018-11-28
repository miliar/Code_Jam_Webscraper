#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<iostream>

// macros

#define SC(n) scanf("%d", &n)
#define SC2(n, m) scanf("%d %d", &n, &m)
#define SCC(c) scanf(" %c", &c)
#define FORE(c, a, b) for(int c=a; c<= int(b); ++c)
#define FORD(c, a, b) for(int c=a; c>= int(b); --c)
#define FORIT(it, cont, cont_t) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define ALL(a) a.begin(), a.end() 
#define PR(n) printf("%d ", (int) (n)) 
#define PRL(n) printf("%lld ", (ll) (n)) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0)
#define prd dbg printf

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef vector<vi> vvi;
typedef set<pi> sii;

// actual code

const int NMAX = 1000009;

int tt, n, nn, d, out;
int As, Cs, Rs;
int Am, Cm, Rm;
int s[NMAX], m[NMAX], sum[NMAX];
vii emp;
vi ch[NMAX];
sii blocked;

void dfs_kill(int v) {
	if(s[v] == -1) return;
	prd("kill %d\n", v);
	nn--;
	s[v] = -1;
	FORIT(it, ch[v], vi)
		dfs_kill(*it);
}

void dfs(int v, int mini, int maxi) {
	prd("dfs %d %d %d\n", v, mini, maxi);
	if(s[v] < maxi - d || s[v] > mini + d) {
		dfs_kill(v);
		return;
	}
	mini = min(mini, s[v]);
	maxi = max(maxi, s[v]);
	sum[v] = 1;
	FORIT(it, ch[v], vi) {
		dfs(*it, mini, maxi);
		sum[v] += sum[*it]; // zabity zwraca 0
	}
}

void block_bigger(int v, int mini) {
	if(s[v] > mini + d) {
		prd("block %d\n", v);
		nn -= sum[v];
		blocked.insert(mp(s[v], v));
	}
	else {
		FORIT(it, ch[v], vi)
			block_bigger(*it, mini);
	}
}

void solve(int ti) {
	SC2(n, d);
	SC2(s[0], As);
	SC2(Cs, Rs);
	SC2(m[0], Am);
	SC2(Cm, Rm);
	nn = n;
	out = 0;
	
	emp.clear();
	emp.pb(mp(s[0], 0));
	ch[0].clear();
	blocked.clear();
	
	FORE(i, 1, n-1) {
		ll tmp = (ll) s[i-1] * As;
		tmp += Cs;
		s[i] = tmp % Rs;
		tmp = (ll) m[i-1] * Am;
		tmp += Cm;
		m[i] = tmp % Rm;
		emp.pb(mp(s[i], i));
		ch[i].clear();
		sum[i] = 0;
	}
	sort(ALL(emp));
	
	FORE(i, 1, n-1) {
		m[i] %= i;
		prd("man %d : %d\n", i, m[i]);
		ch[m[i]].pb(i);
	}
	dfs(0, s[0], s[0]);
	
	int k = 0;
	while(s[emp[k].yy] == -1) k++;
	block_bigger(0, emp[k].xx);
	out = nn;
	
	while(k < n) {
		prd("kick %d\n", emp[k].yy);
		// wywalamy emp[i], dodajemy emp[i+1]
		dfs_kill(emp[k].yy);
		
		int k1 = k + 1;
		while(k1 < n && s[emp[k1].yy] == -1) k1++;
		if(k1 == n) break;
		
		int new_mini = emp[k1].xx;
		while(!blocked.empty()) {
			sii::itr sit = blocked.begin();
			if(sit->xx > new_mini + d)
				break;
			blocked.erase(sit);
			int v = sit->yy;
			prd("return %d\n", v);
			nn += sum[v];
			block_bigger(v, new_mini);
		}
		out = max(out, nn);
		k = k1;
	}
	
	printf("Case #%d: %d\n", ti, out);
}

int main() {
	SC(tt);
	REP(ti, tt)
		solve(ti + 1);
	return 0;
}
