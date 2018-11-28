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
#define MAX 2001
int n,a[MAX],b[MAX],os[MAX],il[MAX],wyn[MAX],iwyn;
vector<int> d[MAX];
void licz(){
	make(n);
	iwyn=0;
	R(i,n){
		d[i].clear();
		il[i]=0;
	}
	R(i,n)make(a[i]);
	R(i,n)make(b[i]);
	R(i,n+1)os[i]=-1;
	R(i,n){
		if(os[a[i]]!=-1){
			d[os[a[i]]].PB(i);
			il[i]++;
		}
		os[a[i]]=i;
		if(a[i]!=1){
			d[i].PB(os[a[i]-1]);
			il[os[a[i]-1]]++;
		}
	}
	
	
	R(i,n+1)os[i]=-1;
	FD(i,n){
		if(os[b[i]]!=-1){
			d[os[b[i]]].PB(i);
			il[i]++;
		}
		os[b[i]]=i;
		if(b[i]!=1){
			d[i].PB(os[b[i]-1]);
			il[os[b[i]-1]]++;
		}
	}
	
	FD(i,n){
		if(il[i]==0){
			il[i]=-1;
			wyn[i]=iwyn;
			iwyn++;
			R(j,d[i].size())
				il[d[i][j]]--;
			i=n;
		}
	}
	R(i,n)printf("%d ",n-wyn[i]);
	printf("\n");
}
main(){
	int _;
	make(_);
	R(t,_){
		printf("Case #%d: ",t+1);
		licz();
	}
}