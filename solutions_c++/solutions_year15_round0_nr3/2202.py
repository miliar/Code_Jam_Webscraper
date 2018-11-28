#include<stdio.h>
#define MN 10000

typedef long long ll;

int mult[5][5]={
	0,0,0,0,0,
	0,1,2,3,4,
	0,2,-1,4,-3,
	0,3,-4,-1,2,
	0,4,3,-2,-1
};

struct QUAT{
	int v;
	QUAT(){v=1;}
	QUAT(char c){v=c-'i'+2;}
	QUAT(int c){v=c;}
	QUAT operator *(QUAT A)const{
		int sgn1=1,sgn2=1;
		if(v<0)sgn1=-1;
		if(A.v<0)sgn2=-1;
		return QUAT(sgn1*sgn2*mult[sgn1*v][sgn2*A.v]);
	}
	QUAT operator *=(QUAT A){
		return (*this)=(*this)*A;
	}
	bool operator ==(QUAT A)const{
		return v==A.v;
	}
	bool operator !=(QUAT A)const{
		return v!=A.v;
	}
};

QUAT pow(QUAT v,ll p){
	QUAT retval;
	while(p){
		if(p&1){
			retval*=v;
		}
		p>>=1;
		v*=v;
	}
	return retval;
}

char inp[MN+1];
QUAT A[4*MN];

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		int N;ll X;
		scanf("%d%lld",&N,&X);
		scanf("%s",inp);
		for(int i=0;i<4*N;i++)A[i]=QUAT(inp[i%N]);
		QUAT ent_v,lhs,rhs;
		for(int i=0;i<N;i++)ent_v*=A[i];
		ent_v=pow(ent_v,X);
		if(ent_v!=QUAT(-1)){
			puts("NO");
			continue;
		}
		int lv=-1,rv=-1;
		for(int i=0;i<4*N;i++){
			lhs*=A[i];
			if(lhs==QUAT('i')){
				lv=i+1;
				break;
			}
		}
		for(int i=0;i<4*N;i++){
			rhs=A[4*N-1-i]*rhs;
			if(rhs==QUAT('k')){
				rv=i+1;
				break;
			}
		}
		if(lv==-1 || rv==-1 || (ll)(lv+rv)>N*X){
			puts("NO");
			continue;
		}
		puts("YES");
	}
	return 0;
}