#include<stdio.h>
#include<math.h>

FILE *in=fopen("test.in","r");
FILE *out=fopen("test.out","w");


int d[11000000];
int T;


long long int reverse(long long int i){
	int t = 0;
	while(i!=0){
		t *= 10;
		t+= i%10;
		i /= 10;
	}
	return t;
}
int main(){
	long long int t;
	int cnt = 0;
	for(int i=1;i<=10000000;i++){
		if(i == reverse(i)){
			if(i*i == reverse(i*i)){
				cnt++;
			}
		}
		d[i] = cnt;
	}
	fscanf(in, "%d", &T);
	int a,b;
	int ta, tb;
	for(int i=1;i<=T;i++){
		fscanf(in, "%d %d", &a, &b); 
		ta = sqrt((double)a);
		tb = sqrt((double)b);

		if(ta*ta == a)  ta-=1;

		fprintf(out, "Case #%d: %d\n", i, d[tb]-d[ta]);
	}
}