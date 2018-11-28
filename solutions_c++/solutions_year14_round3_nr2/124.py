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

#define REP(i, n) for(int i = 0; i< n; ++i)
#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(c, a, b) for(int c=int(a); c<= int(b); ++c)
#define FORD(c, a, b) for(int c=int(a); c>= int(b); --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 
#define ALL(a) a.begin(), a.end()

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(1) 
#define prd dbg printf
#define koniec dbg {SCC(c);SCC(c);} return 0;

using namespace std;

typedef vector<int> vi;
typedef set<char> sc;
typedef multiset<int> msi;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef pair<pi, string> psi;
typedef pair<int, psi> ipsi;
typedef vector<psi> vpsi;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int NMAX = 106, MOD = 1000000007;

char c;
int n, m, tn, ss, shit;
string s;
sc inter;
int loops[NMAX], in[NMAX], out[NMAX], next[NMAX];
ll fact[NMAX];

bool dfs(int start, int v) {
	if(next[v] == -1) return 0;
	if(next[v] == start) return 1;
	return dfs(start, next[v]);
}

void compute(int ti) {
  cin >> n;
  inter.clear();
  REP(i, 26) {
  	in[i] = out[i] = loops[i] = 0;
  	next[i] = -1;
  }
  shit = 0;
  ss = 0;
  
  REP(j, n) {
  	cin >> s;
  	int k = s.size(), last = 0, fir = k - 1;
  	while(last < k && s[last] == s[0]) ++last;
  	while(fir >= 0 && s[fir] == s[k-1]) --fir;
  	FORE(i, last, fir) {
  			if(s[i] != s[i-1] && inter.find(s[i]) != inter.end())
  				shit = 1;
  			else
			  inter.insert(s[i]);
  	}
  	if(s[0] == s[k-1]) {
  		loops[s[0]-'a']++;
  		if(last != k) shit = 1;
  	}
  	else {
  		in[s[k-1]-'a']++;
  		out[s[0]-'a']++;
  		next[s[0]-'a'] = s[k-1]-'a';
  	}
  }
				
  cout << "Case #" << ti << ": ";
  REP(i, 26) {
  	if(in[i] > 1 || out[i] > 1) shit = 1;
  	if(loops[i] + in[i] + out[i] > 0 && inter.find(i + 'a') != inter.end()) shit = 1;
  	if(!in[i] && loops[i] + out[i] > 0) ++ss;
  	if(dfs(i,i)) shit = 1;
  }
  if(shit) {
  	cout << "0" << endl;
  	return;
  }
  
  ll ans = fact[ss];
  REP(i, 26) {
  	ans *= fact[loops[i]];
  	ans %= MOD;
  }
  cout << ans << endl;	
}

int main() {
  fact[0] = fact[1] = 1;
  FORE(i, 2, NMAX - 1) {
  	fact[i] = fact[i-1] * i;
  	fact[i] %= MOD;
  }
  cin >> tn;
  FORE(ti, 1, tn)
    compute(ti);
  return 0;
}

