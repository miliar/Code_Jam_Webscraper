#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef long long lint;

const lint MOD = 1000002013;

vector< pair<lint, lint> > starts;
multiset< pair<lint, lint> > ends;

int main() {
	int ntests, m;
	lint n;
	
	scanf("%d", &ntests);
	
	for (int test = 1; test <= ntests; test++) {
		lint ans = 0;
		
		starts.clear();
		ends.clear();
		
		scanf("%I64d %d", &n, &m);
		
		for (int i = 0; i < m; i++) {
			lint o, e, p;
			scanf("%I64d %I64d %I64d", &o, &e, &p);
			lint S;
			if (e == o) S = 0;
			else {
				lint k = e - o - 1;
				
				S = ((k + 1) * n) % MOD;
				S = (S + ( MOD - ( (k * (k + 1) / 2) % MOD ) ) ) % MOD;
			}
			ans = (ans + ( p * (S % MOD) )) % MOD; 
			
			starts.push_back(make_pair(o, p));
			ends.insert(make_pair(e, p));
		}
		
		sort(starts.begin(), starts.end());
		
		for (int i = starts.size() - 1; i >= 0; i--) {
			pair<lint, lint> cur = starts[i];
			
			while (cur.second > 0) {
				set< pair<lint, lint> >::iterator chosen = ends.lower_bound(make_pair(cur.first, 0));
				
				pair<lint, lint> cp = *chosen;
				
				lint o = cur.first;
				lint e = cp.first;
				lint p = 0;
				
				if (cp.second < cur.second) {
					p = cp.second;
				} else {
					p = cur.second;
				}
				
				lint S;
				if (e == o) S = 0;
				else {
					lint k = e - o - 1;
					S = ((k + 1) * n) % MOD;
					S = (S + MOD - ( (k * (k + 1) / 2) % MOD )) % MOD;
				}
				ans = (ans + MOD - ( ( p * (S % MOD) ) % MOD ) ) % MOD; 
				
				cur.second -= p;
				cp.second -= p;
				
				ends.erase(chosen);
				
				if (cp.second > 0) {
					ends.insert(cp);
				}
			}
		}
		
		printf("Case #%d: ", test);
		printf("%I64d\n", ans);
	}
	return 0;
}