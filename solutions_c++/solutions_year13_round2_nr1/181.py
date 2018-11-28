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
#define MAX 1000001
int a,n,t[MAX];
int test(){
	make(a);make(n);
	R(i,n)make(t[i]);
	if(a==1)return n;
	sort(t,t+n);
	int wyn=n;
	int il=0;
	R(i,n){
		if(t[i]<a){
			a+=t[i];
			if(a>MAX)a=MAX;
		}else{
			wyn=min(wyn,il+n-i);
			il++;
			a+=a-1;
			i--;
		}
	}
	return min(wyn,il);
}
main(){
	int _;
	make(_);
	R(i,_)printf("Case #%d: %d\n",i+1,test());
}
