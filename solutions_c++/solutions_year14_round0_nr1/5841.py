#include <cstdio>
#include <memory.h>
int a[4][4],b[4][4];
int cnt[17];
int main() {
	int T,Ti;
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++) {
		int ar,br;
		scanf("%d",&ar);
		int i,j;
		for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&a[i][j]);
		scanf("%d",&br);
		ar--;
		br--;
		for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&b[i][j]);
		for(i=0;i<4;i++) {
			cnt[a[ar][i]]++;
			cnt[b[br][i]]++;
		}
		int cand=-1;
		for(i=1;i<=16;i++) {
			if(cnt[i]==2) {
				if(cand==-1) cand=i;
				else break;
			}
		}
		if(i<=16) {
			printf("Case #%d: Bad magician!\n",Ti);
		}
		else if(cand!=-1) {
			printf("Case #%d: %d\n",Ti,cand);
		} else {
			printf("Case #%d: Volunteer cheated!\n",Ti);
		}
		memset(cnt,0,sizeof(cnt));
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
	}
	return 0;
}