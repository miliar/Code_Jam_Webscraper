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
#define MAX 101
int n,m,t[MAX][MAX],il;
bool cz[MAX][MAX];
void poz(){
	R(i,n){
		int pom=0;
		R(j,m)if(t[i][j]>pom)pom=t[i][j];
		R(j,m)if(t[i][j]==pom&&cz[i][j]==0){
			cz[i][j]=1;
			il++;
		}
	}
}
bool test(){
	make(n);
	make(m);
	il=0;
	R(i,n)R(j,m){
		make(t[i][j]);
		cz[i][j]=0;
	}
	poz();
	R(i,max(n,m))F(j,i+1,max(n,m)){
		swap(t[i][j],t[j][i]);
		swap(cz[i][j],cz[j][i]);
	}
	swap(n,m);
	poz();
	return il==n*m;
}
main(){
	int _;make(_);
	R(i,_)printf("Case #%d: %s\n",i+1,test()?"YES":"NO");
}
