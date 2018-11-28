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


int T, n, m;
char s[110][110];

int d[5] =  {0, 1, 0, -1, 0};	// y, x
string db = ">v<^";
int check(int y, int x){
	if(s[y][x] == '.') return 0;
	int t = find(ALL(db), s[y][x]) - db.begin();
	{
		int dy = y+d[t];
		int dx = x+d[t+1];
		while(s[dy][dx] != '#'){
			if(s[dy][dx] != '.') return 0;
			dy += d[t];
			dx += d[t+1];
		}
	}
	REP(t, 4){
		int dy = y+d[t];
		int dx = x+d[t+1];
		while(s[dy][dx] != '#'){
			if(s[dy][dx] != '.') return 1;
			dy += d[t];
			dx += d[t+1];
		}
	}
	return INF;
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
		cin >> n >> m;
		memset(s, '#', sizeof(s));
		REPS(i, n)REPS(j, m) cin >> s[i][j];
		ll ans = 0;
		REPS(i, n)REPS(j, m) ans += check(i, j);
		if(ans >= INF) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
