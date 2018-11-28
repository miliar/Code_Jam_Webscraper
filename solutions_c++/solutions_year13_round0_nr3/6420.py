#include <stdio.h>
#include <math.h>
#include <string.h>
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");
int ary[100001];
int solve(int a,int b){
	int i,p=sqrt((double)a),q=sqrt((double)b);
	if(sqrt((double)a)==p) p--;
	return ary[q]-ary[p];
}
int palin(long long int i) {
	int j;
	char st[30];
	int len;
	sprintf(&st[1],"%d",i);
	len = strlen(&st[1]);
	for(j=1;j<=len/2;j++) {
		if(st[j]!=st[len-j+1]) break;
	}
	if(j==len/2+1) return 1;
	return 0;
}
void calc() {
	long long int i,j;
	for(i=1;i<=100000;i++) {
		ary[i]=ary[i-1];
		if(palin(i) && palin(i*i)) {
			ary[i]++;
		}
	}
}
int main(){
	int t;
	int i,a,b;
	fscanf(in,"%d",&t);
	calc();
	for(i=1;i<=t;i++) {
		fscanf(in,"%d %d",&a,&b);
		fprintf(out,"Case #%d: %d\n",i,solve(a,b));
	}
	return 0;
}