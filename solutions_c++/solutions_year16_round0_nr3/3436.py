#include <bits/stdc++.h>
#define LL long long
using namespace std;
LL mrandom(){
	LL x = ((LL)rand()) * ((LL)rand());
	return x;
}
LL my_random(LL a, LL b){
	LL dif = b - a + 1;
	return mrandom()%dif + a;
}
LL mulmod(LL a, LL b, LL m){
	LL x = 0LL, y = a%m;
	while(b > 0LL){
		if(b & 1LL) x = (x + y)%m;
		y = (y*2)%m;
		b>>=1LL;
	}
	return x%m;
}
LL fpow(LL a, LL e, LL m){
	LL x = 1, y = a;
	while(e > 0LL){
		if(e & 1LL) x = mulmod(x,y,m);
		y = mulmod(y,y,m);
		e>>=1LL;
	}
	return x%m;
}
bool primetest(LL n, int k){
	if(n==1LL) return false;
	if(n==2LL || n==3LL) return true;
	if(!(n & 1LL)) return false;
	LL r = 0, d = n-1;
	while(!(d & 1LL)){ r++; d/=2LL;}
	for(int i=0; i<k; i++){
		LL a = my_random(2LL, n-2);
		LL x = fpow(a, d, n);
		if(x==1LL || x==n-1LL) continue;
		bool compo = true;
		for(int i=0; i<r-1 && compo; i++){
			x = fpow(x, 2LL, n);
			if(x==1LL) return false;
			if(x==n-1LL){
				compo = false;
			}
		}
		if(compo) return false;
	}
	return true;
}
char ans[50];
int C;
LL A[20];
int n, j;
void f(int num){
	for(int i=2; i<=10; i++){
		A[i] = 0LL;
		for(int r=0; r<n; r++){
			A[i] = A[i]*(LL)i;
			if(num & (1<<(n-r-1))) A[i]++;
		}
		if(primetest(A[i], 6)) return;
	}
	for(int i=0; i<n; i++) printf("%c", (num & (1<<(n-i-1))) ? '1' : '0');
	printf(" ");
	for(int i=2; i<=10; i++){
		printf("%s", (i==2) ? ("") : (" "));
		for(int r=2; r<A[i]; r++){
			if(A[i]%r==0){
				printf("%d", r);
				break;
			}
		}
	}
	C++;
	printf("\n");
}
int main(){
	scanf("%*d");
	scanf("%d %d", &n, &j);
	printf("Case #1:\n");
	C = 0;
	for(int i=0; i<(1<<n) && C < j; i++){
		if(!(i & 1) || !(i & (1<<(n-1)))) continue;
		f(i);
	}
	return 0;
}