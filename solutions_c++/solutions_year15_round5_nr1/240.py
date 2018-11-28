#include <cstdio>
#include <cstdlib>

int T,N,D,As,Cs,Rs,Am,Cm,Rm;
int S[1000008];
int M[1000008];
int manager[10000008];
int stk[1000008][4];
int enums[1000008];
int esum;
int eid[2000008];
int est[2000008];
int egl[2000008];
int sset[1000008];
int opts[1000008];
int findn(int vl) {
	int minv=0; int maxv=N;
	while(minv<maxv) {
		int hf=(minv+maxv+1)/2;
		if(sset[hf]>vl) {
			maxv=hf-1;
		} else {
			minv=hf;
		}
	}
	return minv;
}
int cmp(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	if(est[a]!=est[b]) return est[a]-est[b];
	return egl[a]-egl[b];
}
int cmp2(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	return a-b;
}
void init(void) {
	for(int i=0;i<1000008;i++) {
		enums[i]=0;
		opts[i]=0;
	}
	esum=0;
}
void adde(int es,int eg) {
	eid[esum]=esum;
	est[esum]=es;
	egl[esum]=eg;
	esum++;
	eid[esum]=esum;
	est[esum]=eg;
	egl[esum]=es;
	esum++;
	enums[es+1]++;
	enums[eg+1]++;
}
int getmin(int va,int vb) {
	if(va>vb) return vb;
	return va;
}
int getmax(int va,int vb) {
	if(va<vb) return vb;
	return va;
}
void search(void) {
	int sz=0;
	int stkfrm=-1;
	stk[sz][0]=0;
	stk[sz][1]=S[0];
	stk[sz][2]=S[0];
	stk[sz][3]=enums[0];
	opts[findn(S[0])+1]--;
	opts[findn(S[0]-D-1)+1]++;
	while(1) {
		if(stk[sz][3]==enums[stk[sz][0]+1]) {
			sz--;
			if(sz<0) break;
			if(sz==0) {
				stkfrm=-1;
			} else {
				stkfrm=stk[sz-1][0];
			}
		} else {
			//printf("*%d %d %d %d\n",stk[sz][0],stk[sz][3],est[eid[stk[sz][3]]],egl[eid[stk[sz][3]]]);
			if(est[eid[stk[sz][3]]]!=stk[sz][0]) {printf("err"); while(1) {printf("");}}
			if(egl[eid[stk[sz][3]]]!=stkfrm) {
				stkfrm=stk[sz][0];
				stk[sz+1][0]=egl[eid[stk[sz][3]]];
				stk[sz+1][1]=getmin(S[stk[sz+1][0]],stk[sz][1]);
				stk[sz+1][2]=getmax(S[stk[sz+1][0]],stk[sz][2]);
				stk[sz+1][3]=enums[stk[sz+1][0]];
				//printf("%d %d %d %d %d\n\n",stk[sz+1][0],stk[sz+1][1],stk[sz+1][2],sset[findn(stk[sz+1][1])+1],sset[findn(stk[sz+1][2]-D-1)+1]);
				if(findn(stk[sz+1][2]-D-1)+1<=findn(stk[sz+1][1])+1) {
					opts[findn(stk[sz+1][1])+1]--;
					opts[findn(stk[sz+1][2]-D-1)+1]++;
				}
				stkfrm=stk[sz][0];
				stk[sz][3]++;
				sz++;
			} else {
				stk[sz][3]++;
			}
		}
	}
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d%d%d%d%d%d%d%d%d",&N,&D,&S[0],&As,&Cs,&Rs,&M[0],&Am,&Cm,&Rm);
		sset[0]=S[0];
		for(int i=1;i<N;i++) {
			S[i]=(int)(((long long)S[i-1]*As+Cs)%Rs);
			M[i]=(int)(((long long)M[i-1]*Am+Cm)%Rm);
			manager[i]=M[i]%i;
			sset[i]=S[i];
		}
		sset[N]=-100000000;
		init();
		for(int i=1;i<N;i++) adde(i,manager[i]);
		qsort(eid,N*2-2,sizeof(int),cmp);
		for(int i=1;i<=N;i++) enums[i]+=enums[i-1];
		qsort(sset,N+1,sizeof(int),cmp2);
		search();
		int sol=opts[0];
		for(int i=1;i<=N;i++) {
			opts[i]+=opts[i-1];
			sol=getmax(sol,opts[i]);
		}
		printf("Case #%d: %d\n",ts,sol);
		
	}
	return 0;
}
