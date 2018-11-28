#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define FOREACH(I,A)  for(__typeof(A.begin()) I = A.begin(); I != A.end(); ++I)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAIN(A,X)  (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong Infinity = 1000000100;
const ldouble Epsilon = 1e-9;

ldouble P[202][202];
ldouble V[202][202];

ldouble X[30];

ldouble K[30];
ldouble L[30];

void test(){
	int n,k;
	scanf("%d%d",&n,&k);

	FOR(i,0,n)FOR(j,0,n)  V[i][j] = P[i][j] =  0;
	V[0][0] = 1;

	FOR(i,1,n){
		ldouble x;
		scanf("%Lf",&X[i-1]);
	}
	ldouble ans = 0;
	FORW(i,1,(1<<n)){
		if( __builtin_popcount(i) != k) continue;
		
		FOR(j,0,k) L[j] = 0;
		L[0] = 1;
		FORW(j,0,n) if(i & (1<<j)){
			ldouble x = X[j];
			FOR(l,1,k) K[l] = L[l]*(1-x) + L[l-1]*x;
			FOR(l,1,k) L[l] = K[l];
			L[0] *= (1-x);
		}
		ans = max(ans, L[k/2]);
	}
	printf("%Lf\n", ans);
}

int main(){
	int T;
	scanf("%d",&T);
	FOR(i,1,T){
		printf("Case #%d: ", i);
		test();
	}
}
