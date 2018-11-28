#include <cstdio>
#include <cstdlib>

int T,M,N;
int ln[1008];
int num[1008];
char str[1008][108];
int cmp(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	if(ln[a]>ln[b]) {
		for(int i=0;i<ln[b];i++) {
			if(str[a][i]!=str[b][i]) return (int)str[a][i]-(int)str[b][i];
		}
		return ln[a]-ln[b];
	} else {
		for(int i=0;i<ln[a];i++) {
			if(str[a][i]!=str[b][i]) return (int)str[a][i]-(int)str[b][i];
		}
		return ln[a]-ln[b];
	}
}
int wrs(int kvx,int kvy) {
	if(kvx<0) return ln[num[kvy]];
	int vx=num[kvx];
	int vy=num[kvy];
	if(ln[vx]>ln[vy]) {
		for(int i=0;i<ln[vy];i++) {
			if(str[vx][i]!=str[vy][i]) return ln[vy]-i;
		}
		return 0;
	} else {
		for(int i=0;i<ln[vx];i++) {
			if(str[vx][i]!=str[vy][i]) return ln[vy]-i;
		}
		return ln[vy]-ln[vx];
	}
}
int wnum,sol;
int lsts[9];
void sets(int dep) {
	if(dep==M) {
		for(int i=0;i<N;i++) {
			int flg=1;
			for(int j=0;j<M;j++) if(lsts[j]==i) flg=0;
			if(flg) return;
		}
		int knum=0;
		for(int i=0;i<M;i++) {
			int bef=-1;
			for(int j=0;j<i;j++) {
				if(lsts[i]==lsts[j]) bef=j;
			}
			knum+=wrs(bef,i);
		}
		if(knum>wnum) {
			wnum=knum;
			sol=0;
		}
		if(knum==wnum) sol++;
	} else {
		for(int i=0;i<N;i++) {
			lsts[dep]=i;
			sets(dep+1);
		}
	}
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d",&M,&N);
		for(int i=0;i<M;i++) {
			scanf("%s",str[i]);
			ln[i]=0;
			while(str[i][ln[i]]!='\0') ln[i]++;
			num[i]=i;
		}
		qsort(num,M,sizeof(int),cmp);
		wnum=-1;
		sol=0;
		sets(0);
		printf("Case #%d: %d %d\n",ts,wnum+N,sol);
	}
	return 0;
}
