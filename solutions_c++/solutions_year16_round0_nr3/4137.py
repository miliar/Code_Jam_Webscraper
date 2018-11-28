#include <bits/stdc++.h>

using namespace std;

int divi(long long n){
	int sq = sqrt(n);
	sq++;
	for(int i = 2; i < sq; i++)
		if(n % i == 0) return i;
	return 0;
}

int N,J,a[11];

long long val(long long mask, int base){
	long long r = 0, V = 1;
	for(int i = 0; i < N; i++){
		if(mask & 1){
			r += V;
		}
		V *= base;
		mask >>= 1;
	}
	return r;
}

long long Cur;

bool check(){
	for(int i = 2; i <= 10; i++){
		int d = divi(val(Cur, i));
		if(d == 0) return 0;
		else a[i] = d;
	}
	return 1;
}

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		printf("Case #%d:\n",t);
		scanf("%d%d",&N,&J);
		Cur = (1 << (N - 1)) + 1;
		while(J){
			if(check()){
				J--;
				printf("%lld",val(Cur,10));
				for(int i = 2; i <= 10; i++){
					printf(" %d",a[i]);
				}
				printf("\n");
			}
			Cur += 2;
		}
	}
}

void fread(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int main(){
	fread();
	init();
	return 0;
}