#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
#define MAX 1001
int n,t[MAX],wyn;
void licz(int* t,int n){
	if(n == 1)return;
	int mi = 0;
	R(i,n)if(t[i] < t[mi]) mi = i;
	if(mi<n-mi-1){
		wyn += mi;
		for(int j = mi;j>0;j--)
			t[j] = t[j-1];
		licz(t+1,n-1);
	}else{
		wyn += n-mi-1;
		for(int j = mi;j<n-1;j++)
			t[j] = t[j+1];
		licz(t,n-1);
	}
}
void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(n);
	wyn = 0;
	R(i,n)make(t[i]);
	licz(t,n);
	printf("%d\n",wyn);
}
main(){
	int _;make(_);while(_--)test();
}
