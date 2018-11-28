#include <cstdio>
#include <algorithm>
#include <queue>

using std::sort;
using std::priority_queue;

const long long MOD = 1000002013;
const long long MX = 1100;

int N, M, M2;

struct s_pa{
	long long o, e;
	long long ct;
	int id;
	bool operator < (const s_pa &b) const{
		if(o != b.o) return (o < b.o);
		return (e < b.e);
	}
} pp[MX], pp2[MX];

struct s_evnt{
	long long t;
	long long ct;
	bool operator < (const s_evnt &b) const {
		if(t != b.t) return (t < b.t);
		if(ct > 0 && b.ct < 0) return true;
		return false;
	}
} evnt[MX * 2];

struct s_hp{
	long long ct;
	long long  t;
	bool operator < (const s_hp &b) const {
		return (t < b.t);
	}
	s_hp(){}
	s_hp(long long ctt, long long tt){
		ct = ctt;
		t  = tt;
	}
};
priority_queue<s_hp> hp;

inline long long calc(long long dist){
	long long a = N;
	long long b = N - dist + 1;
	return ((a + b) % MOD) * (dist % MOD) / 2;
}

inline long long min(long long a, long long b){ return a < b ? a : b; }
inline long long max(long long a, long long b){ return a > b ? a : b; }

int main(){
	for(int t = 1, T, zzz = scanf("%d", &T); t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d %d", &N, &M);
		long long ans0 = 0;
		for(int i = 0; i < M; i++){
			scanf("%lld %lld %lld", &pp[i].o, &pp[i].e, &pp[i].ct);
			ans0 += calc(pp[i].e - pp[i].o) % MOD * pp[i].ct % MOD;
			ans0 %= MOD;
			evnt[i * 2    ].t  =  pp[i].o;
			evnt[i * 2    ].ct =  pp[i].ct;
			evnt[i * 2 + 1].t  =  pp[i].e;
			evnt[i * 2 + 1].ct = -pp[i].ct;
		}
		std::sort(evnt, evnt + M * 2);
		long long ans = 0;
		
		while(!hp.empty()) hp.pop();
		
		for(int i = 0; i < M * 2; i++){
			if(evnt[i].ct > 0){
				hp.push(s_hp(evnt[i].ct, evnt[i].t));
			}else{
				long long ct = -evnt[i].ct;
				while(ct > 0){
					s_hp nw = hp.top();
					hp.pop();
					if(nw.ct > ct){
						ans += calc(evnt[i].t - nw.t) % MOD * ct % MOD;
						ans %= MOD;
						hp.push(s_hp(nw.ct - ct, nw.t));
						ct -= ct;
					}else{
						ans += calc(evnt[i].t - nw.t) % MOD * nw.ct % MOD;
						ans %= MOD;
						ct -= nw.ct;
					}
				}
			}
		}
		printf("%lld\n", (ans0 - ans + MOD) % MOD);
	}
	return 0;
}
