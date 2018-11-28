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
	RI(i, n - 1) if(sl[i] != sl[i-1]) ++ans;
	if(sl[n-1] == '-') ++ans;
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	RI(i, T) {
		printf("Case #%d: ", i);
		te();
	}
	return 0;
}
