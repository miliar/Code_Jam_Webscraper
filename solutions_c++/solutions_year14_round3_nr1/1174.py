#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;
long long int arr[41];

void build(void){
	memset(arr, 0, sizeof(arr));
	arr[0] = 1;
	for(int i=1; i<=40; i++){
		arr[i] = arr[i-1]*2;
	}
}
long long int gcd(long long int p, long long int q){
	for(long long int t; q!=0; t=p%q, p=q, q=t);
	return p;
}
int counting(long long int p, long long int q){
	int cnt = 0;
	while( p < q ){
		cnt++;
		p *= 2;
	}
	return cnt;
}
int check(long long int q){
	for(int i=1; i<=40; i++){
		if( q==arr[i] ){
			return 1;
		}
	}
	return 0;
}

int main(void){
	FILE* fin = fopen("A-large.in","r");
	FILE* fout = fopen("A-large.out","w");

	int T;
	long long int P, Q;
	int cases = 0, i;
	char tmp;
	char str[1000];

	build();

	fscanf(fin, "%d\n", &T);
	while( cases++ < T ){
		/*Input*/
		fgets(str, 1000, fin);
		i = 0;
		P = 0;
		while( (tmp=str[i++])!='/' ){
			P *= 10;
			P += (tmp-'0');
		}
		Q = 0;
		while( (tmp=str[i++])!='\n' ){
			Q *= 10;
			Q += (tmp-'0');
		}
		/*Solve*/
		long long int r = gcd(P,Q);
		P /= r;
		Q /= r;
		int ans = counting(P,Q);
		/*Output*/
		fprintf(fout, "Case #%d: ", cases);
		if( check(Q) ){
			fprintf(fout, "%d\n", ans);
		}else{
			fprintf(fout, "impossible\n", ans);
		}
	}

	return 0;
}
