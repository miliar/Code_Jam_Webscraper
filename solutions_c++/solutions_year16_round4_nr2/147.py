#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define REPS(i,x) for(int i=1;i<=(int)(x);i++)
#define RREP(i,x) for(int i=((int)(x)-1);i>=0;i--)
#define RREPS(i,x) for(int i=((int)(x));i>0;i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)
#define ALL(container) (container).begin(), (container).end()
#define RALL(container) (container).rbegin(), (container).rend()
#define SZ(container) ((int)container.size())
#define mp(a,b) make_pair(a, b)
#define pb push_back
#define eb emplace_back
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"["; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"]"; return os;
}
template<class T> ostream& operator<<(ostream &os, const set<T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class S, class T> pair<S,T> operator+(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first+t.first, s.second+t.second);}
template<class S, class T> pair<S,T> operator-(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first-t.first, s.second-t.second);}

const int INF = 1<<28;
const double EPS = 1e-8;
const int MOD = 1000000007;


int T, n, m;

double calc(const vector<double> &v){
	int n = v.size(), m = v.size() / 2;
	vector<double> dp(m+2, 0);
	dp[0] = 1;
	for(double p : v){
		vector<double> nxt(m+2, 0);
		REP(i, m+1){
			nxt[i] += dp[i] * (1-p);
			nxt[i+1] += dp[i] * p;
		}
		swap(dp, nxt);
	}
	return dp[m];
}


int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(_, T){
		cin >> n >> m;
		vector<double> v(n);
		REP(i, n) cin >> v[i];
		sort(ALL(v));
		
		double dans = 0;
		vector<double> fkgn2;
		REP(j, m+1){
			vector<double> w;
			REP(i, j) w.pb(v[i]);
			RREP(i, m-j) w.pb(v[n-1-i]);
			if(chmax(dans, calc(w))) fkgn2 = w;
		}
		
/*		vector<double> fkgn;
		double ans = 0;
		REP(i, 1<<n)if(__builtin_popcount(i) == m){
			vector<double> w;
			REP(j, n)if(1 & (i>>j)) w.pb(v[j]);
			if(chmax(ans, calc(w))){
				fkgn = w;
			}
		}
		if(abs(ans - dans) > EPS){
			cerr << n << " " << m << endl;
			cerr << v << endl;
			cerr << fkgn << ": " << calc(fkgn) << endl;
			cerr << fkgn2 << ": " << calc(fkgn2) << endl << endl;
		}
*/
		printf("Case #%d: %.15f\n", _, dans);
	}
	return 0;
}
