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

string one[nax], two[nax];

void te() {
	int n;
	cin >> n;
	int ans = 0;
	REP(i, n) cin >> one[i] >> two[i];
	REP(mask, (1 << n)) {
		int cnt = 0;
		REP(i, n) if(mask & (1 << i)) {
			bool ok = false;
			REP(j, n) if(!(mask & (1 << j)))
				if(one[i] == one[j]) {
					ok = true;
					break;
				}
			if(!ok) continue;
			ok = false;
			REP(j, n) if(!(mask & (1 << j)))
				if(two[i] == two[j]) {
					ok = true;
					break;
				}
			if(ok) ++cnt;
		}
		maxi(ans, cnt);
	}
	cout << ans << "\n";
}

int main() {
	ios_base :: sync_with_stdio(false);
	int z;
	cin >> z;
	RI(nr, z) {
		cout << "Case #" << nr << ": ";
		te();
	}
	return 0;
}
