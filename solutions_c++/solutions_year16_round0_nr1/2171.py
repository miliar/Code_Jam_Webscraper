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

void te() {
	set<int> s;
	ll start;
	scanf("%lld", &start);
	if(start == 0) {
		puts("INSOMNIA");
		return;
	}
	for(ll n = start; true; n += start) {
		ll tmp = n;
		while(tmp) {
			s.insert(tmp % 10);
			tmp /= 10;
		}
		if(sz(s) == 10) {
			printf("%lld\n", n);
			return;
		}
	}
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
