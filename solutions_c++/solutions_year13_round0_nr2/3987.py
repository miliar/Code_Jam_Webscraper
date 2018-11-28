#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;


int T,N,M;
int A[100][100];
int mr[100],mc[100];


int max(int a, int b){
	return a>b?a:b;
}

int main(){
	scanf("%d ", &T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d %d ", &N, &M);
		
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				scanf("%d ", &A[i][j]);
			}
		}

		for(int i=0;i<100;i++){mr[i]=0;mc[i]=0;}

		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				mr[i]=max(mr[i], A[i][j]);
			}
		}

		for(int j=0;j<M;j++){
			for(int i=0;i<N;i++){
				mc[j]=max(mc[j], A[i][j]);
			}
		}


		bool val=true;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(A[i][j] < mr[i] && A[i][j] < mc[j]) val = false;
			}
		}
		if(val) printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
	}



	return 0;
}
