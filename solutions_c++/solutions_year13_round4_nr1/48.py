using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>

typedef long double D; typedef long long LL; typedef pair<int,int> pii;
#define ALL(v) (v).begin(),(v).end()
#define REP(i, n) for (int i (0); i < (n); i ++)
#define FORIT(a,b, it) for(__typeof(b)it(a);it!=(b);++it)
#define FOREACH(v, it) FORIT((v).begin(),(v).end(),it)
#define len(v) ((int)(v).size())
#define append push_back
#define _ make_pair
#define fi first
#define se second
#define add insert
#define remove erase
#define TWO(x) (1<<(x))
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
const int infInt (1010101010);
const LL  infLL  (4 * LL (infInt) * LL (infInt));

template<class T>void pv(T a,T b){FORIT(a,b,it)cout<<*it<<" ";cout<<endl;}

inline void chmin(int&x,int y){x=min(x,y);}
inline void chmax(int&x,int y){x=max(x,y);}

const int mod = 1000002013;

inline int cost(int n) { return ((long long) n * (n - 1) / 2) % mod; }

struct Part {
	int s, t;
	long long cnt;
	void read() { scanf("%d%d%lld",&s,&t,&cnt); }
};

int main() {
	int T;
	scanf("%d",&T);
	for (int case_nr=1; case_nr<=T; case_nr++) {
		int N, M;
		scanf("%d%d",&N,&M);
		vector<int> xx;
		vector<Part> parts (M);
		for (int i=0; i<M; i++) {
			parts[i].read();
			xx.push_back(parts[i].s);
			xx.push_back(parts[i].t);
		}
		sort(xx.begin(),xx.end());
		UNIQUE(xx);
		int nx = (int) xx.size();
		vector<long long> flow (nx - 1, 0);
		for (int i=0; i<M; i++) {
			Part & p = parts[i];
			int start = lower_bound(xx.begin(), xx.end(), p.s) - xx.begin();
			int stop  = lower_bound(xx.begin(), xx.end(), p.t) - xx.begin();
			for (int i=start; i<stop; i++) {
				flow[i] += p.cnt;
			}
		}
		long long orig_cost = 0;
		for (int i=0; i<M; i++) {
			Part & p = parts[i];
			orig_cost += (long long) cost(p.t - p.s) * p.cnt % mod;
			orig_cost %= mod;
		}
		long long reduced_cost = 0;
		while (*max_element(flow.begin(), flow.end()) != 0) {
			int i_init = max_element(flow.begin(), flow.end()) - flow.begin();
			int l = i_init;
			int r = i_init;
			while (l-1 >= 0 and flow[l-1] != 0) l = l-1;
			while (r+1 < nx-1 and flow[r+1] != 0) r = r+1;
			long long delta = *min_element(flow.begin()+l, flow.begin()+r+1);
			for (int i=l; i<=r; i++) {
				flow[i] -= delta;
			}
			reduced_cost += (long long) delta % mod * cost(xx[r+1] - xx[l]) % mod;
			reduced_cost %= mod;
		}
		long long diff = reduced_cost - orig_cost;
		diff %= mod;
		diff += mod;
		diff %= mod;
		printf("Case #%d: %d\n", case_nr, (int) diff);
	}
}
