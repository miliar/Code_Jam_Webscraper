#include <algorithm>
#include <cstdio>
#include <map>
using namespace std;
typedef long long ll;
const ll mod= 1000002013;
const int MaxN= 2222;
int T, caseCnt, N, M, tp;
ll ans1, ans2;
ll calc(ll l, ll r){
	return (r-l) * (r-l-1ll) / 2ll % mod;
}
struct __data{
	int pos;
	ll cnt;
	__data(int pos, ll cnt) : pos(pos), cnt(cnt) {}
	__data() {}
	void show(){
		printf("%d %lld\n", pos, cnt);
	}
}data[MaxN], st[MaxN];
bool cmp(const __data&a, const __data&b){
	return a.pos != b.pos ? a.pos < b.pos : a.cnt > b.cnt;
}
int main(){
	scanf("%d", &T);
	while(T --){
		scanf("%d%d", &N, &M);
		ans1= ans2= 0ll;
		for(int i= 1;i<= M;++ i){
			int o, e, p;
			scanf("%d%d%d", &o, &e, &p);
			(ans1 += calc(o, e) * ll(p) % mod)%= mod;
			data[i*2-1]= __data(o, p);
			data[i*2]= __data(e, -p);
		}
//		printf("ans1:%lld\n", ans1);
		sort(data+1, data+1+M*2, cmp);
//		for(int i= 1;i<= M*2;++ i)
//			data[i].show();
		for(int i= 1;i<= M*2;++ i) if(data[i].cnt > 0){
			if(st[tp].pos != data[i].pos)
				st[++ tp]= data[i];
			else
				st[tp].cnt+= data[i].cnt;
		}else{
			while(data[i].cnt < 0){
				if(-data[i].cnt >= st[tp].cnt){
					data[i].cnt+= st[tp].cnt;
					(ans2+= calc(st[tp].pos, data[i].pos) * st[tp].cnt % mod)%= mod;
					-- tp;
				}else{
					st[tp].cnt+= data[i].cnt;
					(ans2+= calc(st[tp].pos, data[i].pos) * (-data[i].cnt) % mod)%= mod;
					data[i].cnt= 0;
				}
			}
		}
//		printf("ans2:%lld\n", ans2);
		printf("Case #%d: %lld\n", ++ caseCnt, (ans2 - ans1 + mod) % mod);
	}
	return 0;
}

