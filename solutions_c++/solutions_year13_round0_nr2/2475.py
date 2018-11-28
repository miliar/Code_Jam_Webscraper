#include<cstdio>
#include<algorithm>
#define MAX 105
using namespace std;

int tab[MAX][MAX],col[MAX],row[MAX],t,N,M,i,j,k;

int main(){
	scanf("%d",&t);
	for(i=1; i<=t; ++i){
		scanf("%d%d",&N,&M);
		for(j=0; j<N; ++j)
			for(k=0; k<M; ++k) scanf("%d",&tab[j][k]);

		for(j=0; j<N; ++j){
			int maxi=0;
			for(k=0; k<M; ++k) maxi=max(maxi,tab[j][k]);
			row[j]=maxi;
		}

		for(j=0; j<M; ++j){
			int maxi=0;
			for(k=0; k<N; ++k) maxi=max(maxi,tab[k][j]);
			col[j]=maxi;
		}

		bool res=true;
		for(j=0; j<N; ++j)
			for(k=0; k<M; ++k)
				if(tab[j][k]!=row[j] && tab[j][k]!=col[k]){
					res=false;
				}

		printf("Case #%d: ",i);
		if(res) printf("YES\n");
		else
			printf("NO\n");
	}	
	return 0;
}
