#include <stdio.h>

#define MAX 100000000000000

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int T;
long long A, B;
int Cnt;
long long P[50];

bool palin(long long a){
	char p[15];
	int i,k;
	for(i=0;a>0;i++){
		p[i] = a%10;
		a/=10;
	}
	p[i]=0;
	for(k=0;k<i/2;k++){
		if(p[k]!=p[i-k-1])return false;
	}
	return true;
}


int main(void){
	int i,j,k;
	long long x;
	for(i=1;;i++){
		if(!palin(long long(i)))continue;
		x = i;
		if(x*x>=(long long)(MAX))break;
		if(!palin(x*x))continue;
		P[Cnt++]=x*x;
	}
	P[Cnt]=(long long)MAX + 1;

	fscanf(in,"%d",&T);
	for(k=1;k<=T;k++){
		fscanf(in,"%lld%lld",&A,&B);
		for(i=0;P[i]<A;i++){
		}
		for(j=0;P[j]<=B;j++){
		}
		j--;
		fprintf(out, "Case #%d: %d\n", k, j-i+1);
	}
	return 0;
}