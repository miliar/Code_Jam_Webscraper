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
#define FORE(a, b, c) for(int c=int(a); c<= int(b); ++c)
#define FORD(a, b, c) for(int c=int(a); c>= int(b); --c)
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
typedef set<int> si;
typedef multiset<int> msi;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef pair<pi, string> psi;
typedef pair<int, psi> ipsi;
typedef vector<psi> vpsi;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int sto = 103;

char c;
int n, m, tn;
ll p, q, g;

ll gcd(ll x, ll y) {
	if(x < y) return gcd(y, x);
	if(y == 0LL) return x;
	return gcd(y, x % y);
}

void compute(int ti) {
  cin >> p >> c >> q;
  g = gcd(p, q);
  p /= g;
  q /= g;
  cout << "Case #" << ti << ": ";
  
  ll pot = 1;
  REP(i, 44) {
  	if(pot == q) break;
  	pot *= 2;
  }
  if(pot != q)
  	cout << "impossible" << endl;
  else {
  	int k = 0;
  	while(p < q) {
  		q /= 2;
  		++k;
  	}
  	cout << k << endl;
  }
}

int main() {
  cin >> tn;
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

