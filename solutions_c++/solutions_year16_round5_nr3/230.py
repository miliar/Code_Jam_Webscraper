#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1005;

int NODES, MY_ID;

struct P {
	int x[3];
	int dx[3];
	void read() {
		REP(i, 3) scanf("%d", &x[i]);
		REP(i, 3) scanf("%d", &dx[i]);
	}
	P operator - (const P & other) {
		P ans;
		REP(i, 3) ans.x[i] = x[i] - other.x[i];
		REP(i, 3) ans.dx[i] = dx[i] - other.dx[i]; // or maybe *(-1)
		return ans;
	}
	ld real_dist(const P & other) {
		ld ans = 0;
		REP(i, 3) ans += pow(x[i] - other.x[i], 2);
		return sqrt(ans);
	}
	ld real_norm(ld tajm) {
		ld ans = 0;
		REP(i, 3) ans += (x[i] + tajm * dx[i]) * (x[i] + tajm * dx[i]);
		return ans;
	}
	ld low, high;
	void solve(ld max_jump) {
		/*puts("");
		REP(i,3) printf("%d, ", x[i]);
		puts("");
		REP(i, 3) printf("%d ", dx[i]);
		puts("");*/
		max_jump *= max_jump;
		low = 0;
		high = 1e9;
		if(real_norm(0) < max_jump) {
			// binary search
			if(real_norm(high) < max_jump) return;
			REP(_, 70) {
				ld mid = (low + high) / 2;
				if(mid < 1e-9) break;
				if(real_norm(mid) < max_jump)
					low = mid;
				else
					high = mid;
			}
			low = 0;
			return;
		}
		// trinary search
		low = 0;
		high = 1e9;
		REP(_, 70) {
			if(high < 1e-9) break;
			ld a = (2 * low + high) / 3;
			ld b = (low + 2 * high) / 3;
			if(real_norm(a) < real_norm(b))
				high = b;
			else
				low = a;
		}
		ld lowest = (low + high) / 2;
		if(real_norm(lowest) >= max_jump) {
			low = high = -1;
			return;
		}
		low = 0;
		high = lowest;
		// bin_search, first good
		REP(_, 70) {
			ld mid = (low + high) / 2;
			if(mid < 1e-9) break;
			if(real_norm(mid) < max_jump)
				high = mid;
			else
				low = mid;
		}
		ld memo_low = (low + high) / 2;
		if(real_norm(1e9) < max_jump) {
			low = memo_low;
			high = 1e9;
			return;
		}
		// bin_search, first bad
		low = lowest;
		high = 1e9;
		REP(_, 70) {
			ld mid = (low + high) / 2;
			if(mid < 1e-9) break;
			if(real_norm(mid) < max_jump)
				low = mid;
			else
				high = mid;
		}
		high = (low + high) / 2;
		low = memo_low;
	}
};

P in[nax], dif[nax][nax];
ld max_jump;
ld ans[nax];
int e[nax][nax];
set<int> to[nax];

void te(int nr) {
	int n, no_jumping;
	scanf("%d%d", &n, &no_jumping);
	REP(i, n) in[i].read();
	if(nr % NODES != MY_ID) return;
	REP(i, n) FOR(j, i + 1, n - 1)
		dif[i][j] = dif[j][i] = in[i] - in[j];
	ld low = 0, high = in[0].real_dist(in[1]);
	REP(_, 60) {
		//puts("---");
		max_jump = (low + high) / 2;
		if(max_jump < 1e-7) break;
		//max_jump = 2.1;
		/*if(nr == 1) max_jump = 1.72205;
		else if(nr == 2) max_jump = 1.901;
		else if(nr == 3) max_jump = 3.901;
		else assert(false);*/
		vector<pair<ld,pair<int,int>>> events;
		REP(i, n) FOR(j, i + 1, n - 1) {
			dif[i][j].solve(max_jump);
			ld one = dif[i][j].low;
			ld two = dif[i][j].high;
			dif[j][i] = dif[i][j];
			if(two < -0.5) continue;
			events.pb(mp(one, mp(i,j)));
			events.pb(mp(two, mp(i,j)));
			//printf("(%d,%d) -> %.3Lf %.3Lf\n", i, j, dif[i][j].low, dif[i][j].high);
		}
		sort(events.begin(), events.end());
		REP(i, n) ans[i] = -1;
		ans[0] = no_jumping;
		for(pair<ld, pair<int,int>> & event : events) {
			ld when = event.first;
			int i = event.second.first;
			int j = event.second.second;
			if(ans[i] > when || ans[j] > when) {
				maxi(ans[i], dif[i][j].high+no_jumping);
				maxi(ans[j], dif[i][j].high+no_jumping);
				vi kol, kol2;
				kol.pb(i);
				kol.pb(j);
				while(!kol.empty()) {
				//	puts("x");
					for(int a : kol) {
						for(int b : to[a]) {
							kol2.pb(b);
							maxi(ans[a], dif[a][b].high+no_jumping);
							maxi(ans[b], dif[a][b].high+no_jumping);
						}
						to[a].clear();
					}
					kol = kol2;
					kol2.clear();
				}
			}
			//printf("%d %d\n", i, j);	fflush(stdout);
			if(e[i][j]) {
				to[i].erase(j);
				to[j].erase(i);
			}
			else {
				to[i].insert(j);
				to[j].insert(i);
			}
			e[i][j] ^= 1;
		}
		//REP(i, n) printf("%.3lf ", (double) ans[i]); puts("");
		REP(i, n) {
			assert(to[i].empty());
			REP(j, n) {
				//printf("> %d\n", e[i][j]);
				assert(e[i][j] == 0);
			}
		}
		if(ans[1] > -0.5) high = (low + high) / 2;
		else low = (low + high) / 2;
	}
	cerr << "#" << nr << "\n";
	printf("Case #%d: ", nr);
	printf("%.10lf\n", (double) (low + high) / 2);
	//exit(0);
}

int main(int argc, char * argv[]) {
	NODES = atoi(argv[1]);
	MY_ID = atoi(argv[2]);
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		te(nr);
	}
	return 0;
}
