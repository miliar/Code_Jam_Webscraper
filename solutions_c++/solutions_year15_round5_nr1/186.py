// Enjoy your stay.

#include <bits/stdc++.h>

#define long long long
#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back

const double EPS = 1e-9;
const double PI = acos(-1.0);
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

typedef istringstream iss;
typedef stringstream sst;
typedef pair<LOOPVAR_TYPE, LOOPVAR_TYPE> pi;
typedef vector<LOOPVAR_TYPE> vi;

#include <sys/time.h>
long getTime(){
	struct timeval t;
	gettimeofday(&t, NULL);
	return t.tv_sec * 1000000LL + t.tv_usec;
}

#define plus plus_
#define minus minus_

int N;
int D;
long S[1000010], M[1000010];
vector<int> g[1000010];
long from[1000010], to[1000010];
long plus[3000010], minus[3000010];

void dfs(int cur, long mi, long ma){
	mi = min(mi, S[cur]);
	ma = max(ma, S[cur]);
	from[cur] = mi;
	to[cur] = ma;
	for(int c: g[cur]){
		dfs(c, mi, ma);
	}
}

void main2(){
	long S0, AS, CS, RS;
	long M0, AM, CM, RM;
	cin >> N >> D >> S0 >> AS >> CS >> RS;
	cin >> M0 >> AM >> CM >> RM;
	S[0] = S0;
	M[0] = M0;
	rep(i, N-1){
		S[i+1] = (S[i] * AS + CS) % RS;
		M[i+1] = (M[i] * AM + CM) % RM;
	}
	rep(i, N){
		g[i].clear();
	}
	rep(i, 1, N){
		g[M[i] % i].pb(i);
	}
	dfs(0, INF, -INF);
	memset(plus,0,sizeof(plus));
	memset(minus,0,sizeof(minus));
	int offset = 1000000;
	rep(i, N)if(to[i] - from[i] <= D){
		//cerr<<from[i]<<" "<<to[i]<<endl;
		plus[to[i] - D + offset]++;
		minus[from[i] + offset]++;
	}
	long ans = 0;
	long cur = 0;
	rep(i, 3000000){
		cur += plus[i];
		ans = max(ans, cur);
		cur -= minus[i];
	}
	cout << ans << endl;
}

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	
	int T;
	cin >> T;
	long start = getTime(), pre = start;
	rep(tc, 1, T + 1){
		cout << "Case #" << tc << ": ";
		main2();
		long now = getTime();
		cerr << tc << "/" << T << ": " << (now - pre) / 1000000. << endl;
		if(tc == T){
			cerr << "Total: " << (now - start) / 1000000. << endl;
			cerr << "  Ave: " << (now - start) / 1000000. / T << endl;
		}
		pre = now;
	}
}
