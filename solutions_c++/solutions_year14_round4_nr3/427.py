#include <cstdio>
#include <cstdlib>

int T,H,W,B,fH;
int fld[1008][9008];
int wa[1008];
int wb[1008];
int ha[1008];
int hb[1008];
int bsn[9008];
int cmp(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	return a-b;
}
int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};
int stkx[9000008];
int stky[9000008];
int stkvec[9000008];
int stki[9000008];
int finds(int nx,int ny) {
	int stks=0;
	if(fld[nx][ny]) return 0;
	fld[nx][ny]=1;
	stkx[0]=nx;
	stky[0]=ny;
	stkvec[0]=3;
	stki[0]=0;
	while(stks>=0) {
		if(stky[stks]==H-1) return 1;
		stkvec[stks]=(stkvec[stks]+1)%4;
		stki[stks]++;
		if(stki[stks]==5) {
			stks--;
		} else {
			if(stkx[stks]+dx[stkvec[stks]]>=0&&stkx[stks]+dx[stkvec[stks]]<W) {
				if(stky[stks]+dy[stkvec[stks]]>=0&&stky[stks]+dy[stkvec[stks]]<H) {
					if(fld[stkx[stks]+dx[stkvec[stks]]][stky[stks]+dy[stkvec[stks]]]==0) {
						fld[stkx[stks]+dx[stkvec[stks]]][stky[stks]+dy[stkvec[stks]]]=2;
						stkx[stks+1]=stkx[stks]+dx[stkvec[stks]];
						stky[stks+1]=stky[stks]+dy[stkvec[stks]];
						stkvec[stks+1]=(stkvec[stks]+2)%4;
						stki[stks+1]=0;
						stks++;
					}
				}
			}
		}
	}
	return 0;
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d%d",&W,&H,&B);
		for(int i=0;i<B;i++) {
			scanf("%d%d%d%d",&wa[i],&ha[i],&wb[i],&hb[i]);
			bsn[i*6]=ha[i]-1;
			bsn[i*6+1]=ha[i];
			bsn[i*6+2]=ha[i]+1;
			bsn[i*6+3]=hb[i]-1;
			bsn[i*6+4]=hb[i];
			bsn[i*6+5]=hb[i]+1;
		}
		qsort(bsn,B*6,sizeof(int),cmp);
		fH=1;
		for(int i=1;i<B*6;i++) {
			if(bsn[i]!=bsn[fH-1]) {
				bsn[fH]=bsn[i];
				fH++;
			}
		}
		for(int i=0;i<W;i++) for(int j=0;j<H;j++) fld[i][j]=0;
		for(int i=0;i<B;i++) {
			int mtha=-1,mthb=-1;
			for(int j=0;j<fH;j++) {
				if(ha[i]==bsn[j]) mtha=j;
				if(hb[i]==bsn[j]) mthb=j;
			}
			//ha[i]=mtha;
			//hb[i]=mthb;
			for(int j=ha[i];j<=hb[i];j++) {
				for(int x=wa[i];x<=wb[i];x++) {
					fld[x][j]=1;
				}
			}
		}
		int sol=0;
		for(int i=0;i<W;i++) {
			if(finds(i,0)) sol++;
		}
		printf("Case #%d: %d\n",ts,sol);
	}
	return 0;
}
