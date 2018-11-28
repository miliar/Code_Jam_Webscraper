#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;

int T;
ll A[11111], B[11111];
ll res[11111];

int check(ll n);

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%lld%lld", &A[q], &B[q]);
		res[q]=0;
	}

		for(int i=1; i<=9; i++) {
			ll p=1*i;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) {
			ll p=11*i;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) {
			ll p=101*i+10*j;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) {
			ll p=1001*i+110*j;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) for(int k=0; k<=9; k++) {
			ll p=10001*i+1010*j+100*k;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) for(int k=0; k<=9; k++) {
			ll p=100001*i+10010*j+1100*k;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) for(int k=0; k<=9; k++) for(int l=0; l<=9; l++) {
			ll p=1000001*i+100010*j+10100*k+1000*l;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

		for(int i=1; i<=9; i++) for(int j=0; j<=9; j++) for(int k=0; k<=9; k++) for(int l=0; l<=9; l++) {
			ll p=10000001*i+1000010*j+100100*k+11000*l;
			ll sq=p*p;
			if(check(sq)) {
				for(int q=1; q<=T; q++) if(A[q]<=sq && sq<=B[q]) res[q]++;
			}
		}

	for(int q=1; q<=T; q++) {
		printf("Case #%d: %lld\n", q, res[q]);
	}

	return 0;
}

int check(ll n)
{
	static int dig[20];
	int k=0;
	while(n>0) {
		dig[k++]=n%10;
		n/=10;
	}
	for(int i=0; i<k/2; i++) if(dig[i]!=dig[k-1-i]) return 0;
	return 1;
}
