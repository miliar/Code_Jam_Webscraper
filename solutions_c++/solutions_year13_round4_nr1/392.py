#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
typedef long long lld;

struct node{
	int t, k, n; //k = 0 in, 1 out
}in[3000], t[3000];

const lld P = 1000002013;

lld cal(lld n, lld len){
	return (len * (n + n - len + 1) / 2) % P;
}

bool cmp(const node &a, const node &b) {
if (a.t == b.t) return a.k < b.k;
return a.t < b.t;
}
int main(){
	int T, n, m;
	int o, e, p;
	//freopen("in", "r", stdin);
	scanf("%d", &T);
	for (int I=1; I<=T; ++I){
		scanf("%d%d", &n, &m);
		lld ans = 0;
		for (int i=0; i<m; ++i){
			scanf("%d%d%d", &o, &e, &p);
			if (I == 12){
				//printf("%d %d %d\n", o, e, p);
			}
			ans = (ans + cal(n, e - o) * p) % P;
			in[i*2].t = o, in[i*2].k = 0, in[i*2].n = p;
			in[i*2+1].t = e, in[i*2+1].k = 1, in[i*2+1].n = p;
		}
		int top = 0;
		sort(in, in+2*m, cmp);
		//ms(2*m);
		for (int i=0; i<2*m; ++i){
			if (in[i].k == 0){
				t[top].t = in[i].t;
				t[top].n = in[i].n;
				top ++;
			}else {
				int cnt = in[i].n;
				while (cnt){
					if (cnt < t[top-1].n){
						ans = (ans - cal(n, in[i].t-t[top-1].t) * cnt) % P;
						t[top-1].n -= cnt;
						cnt = 0;
					}else{
						top --;
						cnt -= t[top].n;
						ans = (ans - cal(n, in[i].t-t[top].t) * t[top].n) % P;
					}
				}
			}
		}
		ans = (ans % P + P) % P;
		printf("Case #%d: %lld\n", I, ans);
	}
	return 0;
}
