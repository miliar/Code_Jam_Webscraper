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
const int nax = 28;

bool in[nax][nax], t[nax][nax];
bool maybe[1 << 4];

void te() {
	int n;
	scanf("%d", &n);
	REP(i, n) {
		char sl[28];
		scanf("%s", sl);
		REP(j, n) in[i][j] = sl[j] == '1';
	}
	int ans = inf;
	REP(mask, (1 << (n * n))) {
		bool ok = true;
		REP(h, n * n) {
			int i = h / n;
			int j = h % n;
			t[i][j] = in[i][j];
			if((mask & (1 << h))) {
				if(in[i][j]) ok = false;
				t[i][j] = true;
			}
		}
		if(!ok) continue;
		int p[28];
		REP(i, n) p[i] = i;
		ok = true;
		do {
			REP(i, (1 << n)) maybe[i] = false;
			maybe[0] = true;
			REP(iii, n) {
				int person = p[iii];
				REP(mach, (1 << n)) if(maybe[mach] && __builtin_popcount(mach) == iii) {
					bool coko = false;
					REP(i, n) if(t[person][i] && !(mach & (1 << i))) {
						maybe[mach | (1 << i)] = true;
						coko = true;
					}
					if(!coko) ok = false;
				}
			}
		} while(next_permutation(p, p + n));
		if(ok) mini(ans, __builtin_popcount(mask));
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	RI(nr, T) {
		cerr << nr << "\n";
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
