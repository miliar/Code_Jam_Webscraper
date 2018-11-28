#include <cstdio>

char sol[12];
char ksol[12];
int sim(int lf,int rg) {
	if(lf==rg) {
		if(ksol[lf]=='R') return 0;
		if(ksol[lf]=='S') return 1;
		if(ksol[lf]=='P') return 2;
	}
	int hf=(lf+rg)/2;
	int va=sim(lf,hf);
	int vb=sim(hf+1,rg);
	if(va==-1||vb==-1) return -1;
	if(va==vb) return -1;
	if(va==0&&vb==2) return vb;
	if(va==2&&vb==0) return va;
	if(va<vb) return va;
	return vb;
}
void check(int nw,int N,int r,int c,int p) {
	if(nw==N) {
		if(sim(0,N-1)!=-1) {
			for(int i=0;i<N;i++) {
				if(sol[i]>ksol[i]) {
					for(int j=0;j<N;j++) {
						sol[j]=ksol[j];
					}
					sol[N]='\0';
					break;
				} else {
					if(sol[i]<ksol[i]) break;
				}
			}
		}
	} else {
		if(r>0) {
			ksol[nw]='R';
			check(nw+1,N,r-1,c,p);
		}
		if(c>0) {
			ksol[nw]='S';
			check(nw+1,N,r,c-1,p);
		}
		if(p>0) {
			ksol[nw]='P';
			check(nw+1,N,r,c,p-1);
		}
		
	}
}
int main() {
	int T,N;
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d",&N);
		int r,c,p;
		scanf("%d%d%d",&r,&p,&c);
		sol[0]='Z';
		sol[1]='\0';
		check(0,(1<<N),r,c,p);
		if(sol[0]=='Z') {
			printf("Case #%d: IMPOSSIBLE\n",ts);
		} else {
			printf("Case #%d: %s\n",ts,sol);
		}
	}
	return 0;
}
