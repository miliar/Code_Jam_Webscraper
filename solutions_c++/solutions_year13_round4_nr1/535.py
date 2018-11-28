#include <stdio.h>
#include <algorithm>

#define MaxM 1000
#define MOD 1000002013
#define min(a, b) ((a)<(b)?(a):(b))

int N, M;
long long ans;

struct list {
	int x;
	int flag;
	int cnt;

	bool friend operator < (list a, list b){
		if (a.x==b.x) return a.flag < b.flag;
		return a.x < b.x;
	}
} List[MaxM*2], Heap[MaxM*2];
int HCnt;

bool heap_compare(list a, list b){
	return a.x < b.x;
}

int main(void){
	int t, T;
	int i;
	int s, e, p;
	long long cost;

	scanf("%d", &T);
	for (t=1; t<=T; t++){
		scanf("%d%d", &N, &M);
		ans = 0;
		for (i=0; i<M; i++){
			scanf("%d%d%d", &s, &e, &p);
			List[i].x = s; List[i].flag = 0; List[i].cnt = p;
			List[i+M].x = e; List[i+M].flag = 1; List[i+M].cnt = p;

			cost = N * (e-s) - (e-s) * (e-s-1) / 2;
			cost %= MOD;

			ans += cost * p;
			ans %= MOD;
		}

		std::sort(List, List+2*M);
		HCnt = 0;
		for (i=0; i<2*M; i++){
			if (List[i].flag==0){
				Heap[HCnt++] = List[i];
				std::push_heap(Heap, Heap+HCnt);
			}
			else {
				while (List[i].cnt>0){
					p = min(List[i].cnt, Heap[0].cnt);
					e = List[i].x - Heap[0].x;

					cost = N * e - e * (e-1) / 2;
					cost %= MOD;
					ans -= cost*p;
					ans %= MOD;
					if (ans<0) ans += MOD;

					List[i].cnt -= p;
					Heap[0].cnt -= p;
					if (Heap[0].cnt==0) std::pop_heap(Heap, Heap+(HCnt--));
				}
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}

