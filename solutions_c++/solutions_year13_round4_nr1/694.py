/*
 * By Duck
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

const int MOD = 1000002013;
const int M = 3000;
struct PCK{
	int p;
	int e;
	PCK(int _e=0, int _p=0) : p(_p), e(_e) {}
};
int comp(PCK a, PCK b) {
	return a.e!=b.e ? a.e<b.e : a.p>b.p;
}


PCK pas[M]; int tp;
PCK tos[M];
int ori[M], end[M], num[M];
int n, m;

int main(){
	int t;
	long long int ttl, dis, tmp, res, ans;
	scanf("%d", &t);	
	for( int r=1; r<=t; r++ ) {
		scanf("%d %d", &n, &m);
		tmp = ttl = res = 0;
		for( int i=0; i<m; i++ ) {
			scanf("%d %d %d", ori+i, end+i, num+i);
			tos[i*2] = PCK(ori[i], num[i]);
			tos[i*2+1]=PCK(end[i], -num[i]);
			dis = end[i] - ori[i];
			ttl += (num[i] * (( dis*n - dis*(dis-1)/2 ) % MOD))%MOD;
			ttl %= MOD;
		}
		std::sort(tos, tos+2*m, comp);
		tp = 0;
		for( int i=0; i<2*m; i++ ) {
			if( tos[i].p>0 ) {
				pas[tp++] = tos[i];
			} else {
				tmp = -tos[i].p;
				while( tp>0&&tmp!=0 ) {
					
					dis = tos[i].e - pas[tp-1].e;
//					printf("at %d dis: %I64d : from%d to %d\n", i, dis, pas[tp-1].e, tos[i].e);
					if( pas[tp-1].p<tmp ) {
						tmp -= pas[tp-1].p;
						res += (pas[tp-1].p * (( dis*n - dis*(dis-1)/2 ) % MOD))%MOD;
						res %= MOD;
						tp--;
					} else {
						res += (tmp * (( dis*n - dis*(dis-1)/2 ) % MOD))%MOD;
						res %= MOD;
						pas[tp-1].p -= tmp;
						if( pas[tp-1].p==0 ) tp--;
						tmp = 0;
					}
				}
			}
		}
		ans = ((ttl - res)+MOD)%MOD;
		printf("Case #%d: %I64d\n", r, ans);
	}
	
}

