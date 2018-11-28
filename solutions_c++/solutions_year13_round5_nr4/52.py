#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
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
#define make(A) scanf("%d",&A);
#define MAX 21
char t[MAX];
int n;
D wyn[(1<<MAX)];
D licz(int mb){
	if(wyn[mb]>-0.5){
		return wyn[mb];
	}
	D wynn = 0.;
	R(i,n){
		int il=0;
		int pom = i+il ;
		while(mb & (1<<pom)){
			pom--;
			if(pom==-1)pom=n-1;
			il++;
		}
		wynn += n - il + licz(mb | (1<<pom));
	}
	wyn[mb] = wynn/n;
	return wyn[mb];
}
void test(){
	scanf(" %s",t);
	n=0;while(t[n])n++;
	int mb=0;
	R(i,(1<<n))
	wyn[i]=-1.;
	wyn[(1<<n)-1]=0;
	R(i,n){
		mb*=2;
		if(t[i]=='X')
			mb++;
	}
	printf("%.10f\n",licz(mb));
}
main(){
	int _;
	make(_);
	R(i,_){
		printf("Case #%d: ",i+1);
		test();
	}
}