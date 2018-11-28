#include<cstdio>
using namespace std;
long long fairs[100];
int d[20];
bool is_palindrome(long long x){
	int len = 0;
	while(x){
		d[len++]=x%10;
		x/=10;
	}
	for(int i = 0; i < len-i-1; i++)
		if(d[i] != d[len-i-1])
			return false;
	return true;
}
int main(){
	int len = 0;
	for(long long i = 0; i < 10000000; i++)
		if(is_palindrome(i) && is_palindrome(i*i)){
			fairs[len++]=i*i;
		}
	int tests;
	scanf("%d",&tests);
	for(int t = 1; t <= tests; t++){
		int a, b;
		long long A, B;
		scanf("%d %d", &a, &b);
		A=a;
		B=b;
		
		int p = 0;
		int q = len - 1;
		while(p < len && fairs[p]<A){
			p++;
		}
		while(fairs[q]>B){
			q--;
		}
		printf("Case #%d: %d\n", t, q - p + 1);
	}
	return 0;
}
