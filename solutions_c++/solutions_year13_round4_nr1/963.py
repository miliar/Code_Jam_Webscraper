#include <cstdio>
#include <vector>
#include <algorithm>
#define ll long long

using namespace std;

const ll MD = 1000002013;

struct station {
	int i;
	int p;
	bool ent;
	station() {}
	station(int _i, int _p, bool _ent): i(_i), p(_p), ent(_ent) {}
};

ll cost(ll o, ll e, ll p, ll n) {
	ll tmp = n*(n+1)/2;
	ll tmp2 = e-o;
	tmp -= tmp2*(tmp2+1)/2;
	tmp = tmp%MD;
	
	return (tmp*p)%MD;
}

bool comp(const station& b, const station& a) {
	if(b.i < a.i) {
		return true;
	} else if(b.i == a.i) {
		return b.ent;
	} else {
		return false;
	}
}

int main() {
	
	int test;
	scanf("%d", &test);
	int n,m;
	ll tot;
	ll paid;
	vector<station> st;
	
	vector<pair<int,int> > stack;
	
	for(int k = 1; k <= test; k++) {
		printf("Case #%d: ", k);
		fflush(stdout);
		scanf("%d %d", &n, &m);
		tot = 0;
		paid = 0;
		st.clear();
		st.resize(2*m);
		stack.clear();
		stack.resize(m);
		int stp = -1;
		
		int j = 0;
		for(int i = 0; i < m; i++) {
			int o,e,p;
			scanf("%d %d %d", &o, &e, &p);
			tot += cost(o,e,p,n);
			tot = tot%MD;
			st[j++] = station(o,p,true);
			st[j++] = station(e,p,false); 
		}
		
		sort(st.begin(), st.end(), comp);
		
		for(j = 0; j < (int)st.size(); j++) {
			//printf("s %d %d     ", st[j].i, st[j].ent?1:0);
			if(st[j].ent) {
				stack[++stp] = pair<int,int>(st[j].i, st[j].p);
			} else {
				int p = st[j].p;
				while(p > 0) {
					if(stack[stp].second > p) {
						stack[stp].second -= p;
						paid += cost(stack[stp].first, st[j].i, p, n);
						paid = paid%MD;
						p = 0;
					} else {
						p -= stack[stp].second;
						paid += cost(stack[stp].first, st[j].i, stack[stp].second, n);
						paid = paid%MD;
						stp--;
					}
				}
			}
		}
		
		tot -= paid;
		while(tot < 0) tot += MD;
		
		printf("%lld\n", tot);
	}
	
	return 0;
}
