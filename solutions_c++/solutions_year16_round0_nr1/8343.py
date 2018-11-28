#include <bits/stdc++.h>

using namespace std;
// Constants and macros
#define INF 		(int)1e9
#define EPS 		1e-9
#define bitcount 	__builtin_popcount
#define gcd 		__gcd
#define forall(i,a,b) 	for(int i=a;i<b;i++)
#define pb 		push_back
#define mp		make_pair
#define MAX(a,b)	( (a)>(b) ? (a):(b))
#define MIN(a,b)	( (a)<(b) ? (a):(b))
#define s(a)		scanf("%d", &a)
#define ss(a,b)		scanf("%d %d", &a,&b)
#define sss(a,b,c)	scanf("%d %d %d", &a,&b,&c)
#define sl(a)		scanf("%I64d", &a)

int N, T;
int d[10];

long long sleep(long long N){
	if (N == 0) return 0;
	forall(i,0,10){
		d[i] = 0;
	}
	bool done = false;
	long long m = 0;
	while (!done){
		m++;
		done = true;
		long long K = N*m;
		do {
			int check = K % 10;
			d[check] = 1;
		} while ((K=K/10)!=0);
		forall(i,0,10){
			if (d[i] == 0) done = false;
		}
	}
	return m*N;
}

int main(){
	s(T);
	long long KK =0;
	forall(i,0,T){
		s(N);
		if ((KK = sleep(N)))
			printf("Case #%d: %lld\n", i+1 ,KK);
		else 
			printf("Case #%d: INSOMNIA\n", i+1);
	}
}
