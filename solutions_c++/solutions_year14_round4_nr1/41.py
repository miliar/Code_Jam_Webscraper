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
#define MAX 100001
int n,x;
int t[MAX];
void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(n);make(x);
	R(i,n)make(t[i]);
	sort(t,t+n);
	int i=0,j=n-1,wyn=0;
	while(i<j){
		if(t[i] + t[j] <= x){
			wyn++;
			i++;
		}
		j--;
	}
	printf("%d\n",n-wyn);
}
main(){
	int _;make(_);while(_--)test();
}
