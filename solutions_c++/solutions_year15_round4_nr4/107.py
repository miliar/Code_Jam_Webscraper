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
template<class S, class T> ostream& operator<<(ostream &os, const map<S, T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class S, class T> pair<S,T> operator+(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first+t.first, s.second+t.second);}
template<class S, class T> pair<S,T> operator-(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first-t.first, s.second-t.second);}

const int INF = 1<<28;
const double EPS = 1e-8;
const int MOD = 1000000007;


int T, n, m;
string s;
int b[10][10];
int d[5] =  {0, 1, 0, -1, 0};	// y, x

int check(int y, int x){
	if(x == 0) x = m;
	if(x == m+1) x = 1;
	if(y == 0 || y == n+1) return 1;
	if(b[y][x] == -1) return 1;
	int cmin = 0, cmax = 0;
	REP(i, 4){
		int dy = y+d[i], dx = x+d[i+1];
		if(dy == 0 || dy == n+1) continue;
		if(dx == 0) dx = m;
		if(dx == m+1) dx = 1;
		int t = b[dy][dx];
		if(t == b[y][x]){
			cmin ++; cmax ++;
		}else if(t == -1) cmax ++;
	}
/*	cout << cmin << " < " << cmax << "(" << y << ", " << x << ")" << endl;
	if(!(cmin <= b[y][x] && b[y][x] <= cmax)){
			REPS(i,n){
				cout << "!";
				REPS(j,m) cout << b[i][j];
				cout << endl;
			}
	}
*/
	return (cmin <= b[y][x] && b[y][x] <= cmax);
}
set<vi> used;
int dfs(int y, int x){
	if(x == m+1){
		y ++; x = 1;
	}
	if(y == n+1){
		REPS(i, n)REPS(j, m) if(!check(i, j)) return 0;
		vi t;
		REPS(i, n)REPS(j, m) t.pb(b[i][j]);
		if(used.find(t) != used.end()) return 0;
		REP(k, m){
			vi t;
			REPS(i, n)REPS(j, m) t.pb(b[i][(j+k)%m + 1]);
			used.insert(t);
		}
/*		REPS(i,n){
			cout << ">";
			REPS(j,m) cout << b[i][j];
			cout << endl;
		}
		cout << endl;
*/		return 1;
	}
	int res = 0;
	REPS(i, 4){
		b[y][x] = i;
/*		REPS(i,n){
			cout << "?!";
			REPS(j,m) cout << b[i][j];
			cout << endl;
		}
*///		if(!check(y-1, x) || !check(y, x) || !check(y, x-1) || !check(y, x+1) || !check(y+1, x)){
		if(!check(y-1, x) || !check(y, x) || !check(y, x-1) || !check(y, x+1) || !check(y+1, x)){
			continue;
		}
		res += dfs(y, x + 1);
		if(res >= MOD) res -= MOD;
	}
	b[y][x] = -1;
	return res;
}

int solve(){
	memset(b, -1, sizeof(b));
	used.clear();
	return dfs(1, 1);
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
		cin >> n >> m;
		int ans = solve();
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}
