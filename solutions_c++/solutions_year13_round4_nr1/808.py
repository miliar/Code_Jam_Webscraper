#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#define eps 1e-8
#define oo 1<<29
#define LL long long

using namespace std;

LL T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, an, ans, y;
LL old, total;
LL b[2010];
LL bsize, cur;

struct aa{
	LL start;
	LL end;
	LL p;
};

struct bb{
	LL pos;
	LL number;
};

aa a[10010];
bb c[1000100];

bool ss(bb q, bb w){
	return q.pos < w.pos;
}

LL cost(LL q, LL w){
	return (n+(n-(w-q)+1))*(w-q)/2;
}

int main(){
	scanf("%lld", &T);
	for (LL rr = 1; rr <= T; rr++){
		memset(b, 0, sizeof(b));
		memset(c, 0, sizeof(c));
		printf("Case #%lld: ", rr);
		scanf("%lld%lld", &n, &m);
		/*		
					if (rr == 4){
					printf("cost: %lld\n", cost(1, 1));
					printf("cost: %lld\n", cost(1, 2));
					printf("cost: %lld\n", cost(1, 3));
					printf("cost: %lld\n", cost(1, 4));
					printf("cost: %lld\n", cost(1, 5));
					printf("cost: %lld\n", cost(1, 6));
					}
		 */		
		old = 0;
		for (LL i=0; i<m; i++){
			scanf("%lld%lld%lld", &a[i].start, &a[i].end, &a[i].p);
			b[i*2] = a[i].start;
			b[i*2+1] = a[i].end;
			old += a[i].p*cost(a[i].start, a[i].end);
		}
		sort(b, b+2*m);
		bsize = (LL)(unique(b, b+2*m) - b);
		total = 0;
		cur = 0;

		for (LL i=0; i<bsize; i++){

			for (LL j=0; j<m; j++)
				if (a[j].start == b[i]){
					c[cur].pos = a[j].start;
					c[cur].number = a[j].p;
					cur++;
				}
			sort(c, c+cur, ss);
			for (LL j=1; j<cur; j++)
				if (c[j-1].pos == c[j].pos){
					c[j-1].number += c[j].number;
					c[j].pos = -1;
				}
			e = 0;
			for (LL j=0; j<cur; j++){
				if (c[j].pos == -1 || c[j].number == 0)
					continue;
				c[e].pos = c[j].pos;
				c[e].number = c[j].number;
				e++;
			}
			cur = e;
/*			
			printf("cur = %lld b[i] = %lld\n", cur, b[i]);
			for (LL j=0; j<cur; j++)
				printf("%lld %lld %lld\n", j, c[j].pos, c[j].number);
			puts("");
*/			
			for (LL j=0; j<m; j++)
				if (a[j].end == b[i]){
					t = a[j].p;
					for (LL k=cur-1; k>=0; k--){
						if (t >= c[k].number){
							total += c[k].number*cost(c[k].pos, b[i]);
							t -= c[k].number;
							c[k].number = 0;
						} else {
							total += t*cost(c[k].pos, b[i]);
							c[k].number -= t;
							t = 0;
						}
						if (t == 0)
							break;
					}
				}
			e = 0;
			for (LL j=0; j<cur; j++){
				if (c[j].pos == -1 || c[j].number == 0)
					continue;
				c[e].pos = c[j].pos;
				c[e].number = c[j].number;
				e++;
			}
			cur = e;
			//			printf("%lld\n", total);
		}
//		printf("old: %lld new: %lld\n", old, total);
		printf("%lld\n", (old-total)%1000002013);
	}
	return 0;
}
