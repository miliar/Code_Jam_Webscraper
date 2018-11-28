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
#define MAX 201
int all[MAX],ak[MAX],n,k,o[MAX];
vector<int> d[MAX],dk[MAX];
bool cz[MAX],czk[MAX],czgl[MAX];
void clr(){
	R(i,MAX){
		all[i]=0;
		ak[i]=0;
		czgl[i]=0;
		d[i].clear();
		dk[i].clear();
	}
}
void dfs2(int);
void dfs(int k){
	if(czk[k]==1)return;
	czk[k]=1;
	R(i,dk[k].size())
	dfs2(dk[k][i]);
}
void dfs2(int nr){
	if(cz[nr]==1)return;
	cz[nr]=1;
	R(i,d[nr].size())
	dfs(d[nr][i]);
}
bool spr(){
	R(i,n)cz[i]=czgl[i];
	R(i,MAX)czk[i]=0;
	R(i,MAX)if(ak[i])dfs(i);
	R(i,n)if(cz[i]==0)return 0;
	return 1;
}
void add(int nr){
	czgl[nr]=1;
	ak[o[nr]]--;
	R(i,d[nr].size())
		ak[d[nr][i]]++;
}
void us(int nr){
	czgl[nr]=0;
	ak[o[nr]]++;
	R(i,d[nr].size())
		ak[d[nr][i]]--;
}
void test(){
	make(k);
	make(n);
	clr();
	R(i,k){
		int pom;make(pom);
		all[pom]++;
		ak[pom]++;
	}
	R(i,n){
		make(o[i]);
		all[o[i]]--;
		dk[o[i]].PB(i);
		int pom;make(pom);
		while(pom--){
			int pom2;make(pom2);
			all[pom2]++;
			d[i].PB(pom2);
		}
	}
	R(i,MAX)if(all[i]<0){
		printf(" IMPOSSIBLE\n");
		return;
	}
	if(spr()==0){
		printf(" IMPOSSIBLE\n");
		return;
	}
	R(i,n)R(j,n){
		if(czgl[j]==1||ak[o[j]]==0)continue;
		add(j);
		if(spr()){
			printf(" %d",j+1);
			break;
		}
		us(j);
	}
	printf("\n");
}
main(){
	int _;make(_);
	R(i,_){
		printf("Case #%d:",i+1);
		test();
	}
}
