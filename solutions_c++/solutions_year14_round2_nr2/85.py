#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<map>
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
int a,b,c;
bool ma(int a,int b){
	return ((a>>b)&1);
}
void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(a);make(b);make(c);
	LL wyn=0;
	R(i,31)R(j,31)R(k,31){
		if(ma(a,i) && ma(b,j) && ma(c,k)){
			LL re = 1;
			R(l,31){
				int il=0;
				R(w0,2)if(l < i || (ma(a,l) ^ w0 ^ (l != i)))
				R(w1,2)if(l < j || (ma(b,l) ^ w1 ^ (l != j)))
				R(w2,2)if(l < k || (ma(c,l) ^ w2 ^ (l != k)))
				if((w0&w1) == w2)il++;
				re *= il;
			}
			wyn += re;
		}
	}
	printf("%lld\n",wyn);
}
main(){
	int _;make(_);while(_--)test();
}
