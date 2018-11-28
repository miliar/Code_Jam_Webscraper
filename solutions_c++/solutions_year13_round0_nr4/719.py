
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst, cas, K,N;
int hav[205], req[22], ins[22][55], x, y, aln;
int sta[1<<20];
char bak[1<<20];

bool set(int mask, int i) {
	return mask & (1<<i);
}

void go(int state) {
	if (sta[state]) return;
	if (state==aln) {
		sta[state]=1;
		return;
	}

	for (int i=0; i<N; i++) if (!set(state,i)) {
		int r=req[i];
		if (hav[r]) {
			hav[r]--;
			int j=0;
			while (true) {
				int ke=ins[i][j++];
				if (!ke) break;
				hav[ke]++;
			}
			sta[state] |= 1<<i;
			
			go(state | (1<<i));
			
			hav[r]++;
			j=0;
			while (true) {
				int ke=ins[i][j++];
				if (!ke) break;
				hav[ke]--;
			}
		}
	}
}

void bk(int state) {
	if (bak[state]==cas) return;
	bak[state]=cas;
	for (int i=0; i<N; i++) if (set(state,i)) {
		int sup=state ^ (1<<i);
		if (set(sta[sup],i)) bk(sup);
	}
}

main() {
	scanf("%d", &tst);
	for (cas=1; cas<=tst; cas++) {
		scanf("%d%d",&K,&N);
		
		fill(hav,hav+205,0);
		aln=(1<<N)-1;
		for (int i=0; i<=aln; i++) {
			sta[i]=0;
		}

		for (int k=0; k<K; k++) {
			scanf("%d",&x);
			hav[x]++;
		}
	
		for (int b=0; b<N; b++) {
			scanf("%d%d", req+b, &y);
			for (int i=0; i<y; i++)
				scanf("%d", ins[b]+i);
			ins[b][y]=0;
		}

		go(0);
		
		if (!sta[aln]) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else {
			printf("Case #%d: ", cas);
			bk(aln);
			int s=0;
			for (int o=0; o<N; o++) {
				int j=-1;
				for (int i=0; i<N; i++) {
					if (!set(s,i) && set(sta[s],i) && bak[s | (1<<i)]==cas) {
						j=i;
						break;
					}
				}
				printf("%d ", j+1);
				s |= (1<<j);
			}
			printf("\n");
		}
	}
}
