#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;
typedef long long LL ;
const int INF = 1000*1000*1000 ;
const LL INFLL = (LL)INF * (LL)INF ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define CLEAR(t) memset(t,0,sizeof(t))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const int MOD = 1000002013 ;

struct ent {
	LL time, p ;
	bool in ;
	ent(LL ttime=0, LL pp=0, bool iin=false) : time(ttime), p(pp), in(iin) {}
} ;
bool operator<(const ent &a, const ent &b) {
	if(a.time != b.time) return a.time < b.time ;
	else return a.in > b.in ; // pierwszenstwo maja wsiadajacy
}

LL dist(LL k) {
	return (k*(k-1)/2)%MOD ;
}

void _main() {
	int n, m ;
	LL o, e, p ;
	vector<ent> t ;
	cin >> n >> m ;
	LL x=0 ;
	while(m--) {
		cin >> o >> e >> p ;
		t.PB(ent(o, p, true)) ;
		t.PB(ent(e, p, false)) ;
		LL k = e-o ;
		x += (dist(k) * p) %MOD ;
		x %= MOD ;
	}
//	cout << "x= " << x << endl ;
	sort(ALL(t)) ;
	
	LL y=0 ;
	vector<pair<int,int> > pom ; // stacja, ile
	FOREACH(q, t) {
		if(q->in)
			pom.PB(MP(q->time, q->p)) ;
		else {
			p = q->p ; // tyle ludzi wysiada
			e = q->time ;
			while(p > 0) {
				assert(!pom.empty()) ;
				
				if(pom.back().SE <= p) {
					y += (dist(e-pom.back().FI)*pom.back().SE ) %MOD ;
					y %= MOD ;
					
					p -= pom.back().SE ;
					pom.pop_back() ;
				}
				else {
					y += (dist(e-pom.back().FI)*p ) %MOD ;
					y %= MOD ;
					pom.back().SE -= p ;
					break ;
				}
			}
		}
	}
	assert(pom.empty()) ;
//	cout << "y= " << y << endl ;
	cout << (y-x+MOD)%MOD << endl ; 
}

int main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(int tests=1 ; tests<=C ; tests++) {
		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		_main() ;
	}
}

