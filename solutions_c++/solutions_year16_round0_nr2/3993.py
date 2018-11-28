#include <bits/stdc++.h>

using namespace std;
#define DEBUG_ON 1

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false);
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define TRAV(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define RTRAV(it,c) for(__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define DBG(x) if(DEBUG_ON) cout << #x << " == " << x << endl
#define DBGP(x) if(DEBUG_ON) cout << "(" << (x).first << ", " << (x).second << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define R(x) scanf(" %d",&(x))
#define RR(x,y) scanf(" %d %d",&(x), &(y))
#define RRR(x,y,z) scanf(" %d %d %d",&(x), &(y),&(z))
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef int int_type;
typedef pair<int_type, int_type> pii;
typedef vector<int_type> vi;
typedef vector<vi> vii;

int solve(string src) {
	unordered_map<string, int> dist;	
	dist[src] = 0;
	queue<string> q;
	q.push(src);
	int sz = src.size();
	string tgt(sz,'+');
	while(!q.empty()) {
		string front = q.front();
		q.pop();
		if(front==tgt) return dist[front];
		int cdist = dist[front];
		FOR(i,1,sz+1) {
			string pos(sz,'-');
			FOR0(j,i) {
				pos[i-1-j] = (front[j]=='+' ? '-' : '+');
			}
			FOR(j,i,sz) pos[j] = front[j];
			if(!dist.count(pos)) {
				dist[pos] = cdist + 1;
				q.push(pos);
			}
		}
	}
}

int solve_fast(string src) {
	int groups = 1;
	FOR(i,1,src.size()) if(src[i] != src[i-1]) ++groups;
	return groups - (src.back()=='+' ? 1 : 0);
}

int main() {
	NSYNC;
	int n;
	cin >> n;
	FOR(t,1,n+1) {
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		cout << solve_fast(s) << endl;
	}
	return 0;
}