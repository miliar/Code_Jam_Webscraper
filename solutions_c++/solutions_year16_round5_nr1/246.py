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
const int nax = 1e6 + 5;

char sl[nax];

void te() {
	scanf("%s", sl);
	int n = strlen(sl);
	int ans = 0;
	vi w;
	REP(i, n) {
		int here;
		if(sl[i] == 'C') here = 1;
		else here = 2;
		if(!w.empty() && w.back() == here) {
			w.pop_back();
			ans += 10;
		}
		else {
			w.pb(here);
		}
	}
	ans += (int) w.size() / 2 * 5;
	printf("%d\n", ans);
}

int main() {
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
