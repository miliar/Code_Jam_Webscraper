#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
struct PT {
	LL i, a, b;
	bool operator<(const PT& p) const {
		if (b != p.b) return b<p.b;
		return a > p.a;
	}
};
#define FOR(i,a,b) for(LL i=a;i<LL(b);i++)

LL TC , N , D , S[1000005] , As , Cs , Rs , M[1000005] , Am , Cm , Rm;
vector<vector<LL>> childs;
vector<PT> rts;

void dfs(LL i, LL a, LL b) {
	a = min(a, S[i]);
	b = max(b, S[i]);
	rts.push_back(PT{i,a,b});
	for(LL j : childs[i]) dfs(j, a, b);
}

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> D >> S[0] >> As >> Cs >> Rs >> M[0] >> Am >> Cm >> Rm;
		FOR(i,1,N) {
			S[i] = (S[i-1]*As+Cs)%Rs;
			M[i] = (M[i-1]*Am+Cm)%Rm;
		}
		childs.assign(N, vector<LL>());
		FOR(i,1,N) {
			M[i] %= i;
			childs[M[i]].push_back(i);
		}
		
		rts.clear();
		dfs(0, S[0], S[0]);
		sort(begin(rts), end(rts));

		set<pair<LL,LL>> swp;
		LL ans = 0;
		FOR(pb,0,N) {
			swp.emplace(rts[pb].a, rts[pb].i);
			while (!swp.empty() && rts[pb].b - begin(swp)->first > D) swp.erase(begin(swp));
			ans = max(ans, (LL)swp.size());
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}
}
