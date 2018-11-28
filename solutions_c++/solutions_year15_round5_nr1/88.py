#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <deque>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <unordered_map>
#include <iterator>
#include <functional>
#include <cassert>
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


int T, n, D;
int S[1000005], M[1000005], valid[1000005];
vector<vi> g;

int fill(int u){
	if(valid[u] == -1) return 0;
	int res = valid[u];
	valid[u] = -1;
	for(int v : g[u]) res += fill(v);
	return res;
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
cerr << t << "/" << T << endl;
		cin >> n >> D;
		g = vector<vi>(n);
		ll As, Cs, Rs, Am, Cm, Rm;
		cin >> S[0] >> As >> Cs >> Rs >> M[0] >> Am >> Cm >> Rm;
		REP(i, n){
			S[i+1] = (S[i]*As + Cs) % Rs;
			M[i+1] = (M[i]*Am + Cm) % Rm;
			if(i) g[M[i]%i].pb(i);
		}
		REP(i, n) valid[i] = 0;
		int ans = 1, curmax = 0, cur = 0;
		priority_queue<pii, vector<pii>, greater<pii>> addq, remq;
		addq.emplace(S[0], 0);
		while(!addq.empty()){
			int u, w; tie(w, u) = addq.top(); addq.pop();
			if(valid[u] == -1) continue;
			valid[u] = 1; cur ++;
			curmax = max(curmax, S[u]);
			remq.emplace(w, u);
			for(int v : g[u]) addq.emplace(S[v], v);
			while(!remq.empty() && remq.top().first + D < curmax){
				int u = remq.top().second; remq.pop();
				cur -= fill(u);
			}
			ans = max(ans, cur);
		}
		
		
		printf("Case #%d: %d\n", t, ans);
//		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
