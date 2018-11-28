#include <stack>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;


int N, TC;
double B[1000], G[1000]; 
bool used[1000];
int maxB, maxG, minB, minG;

int war(){

	int res=N;
	for(int i=0; i<N; ++i){
		for(int o=0; o<N; ++o){
			if( B[o] > G[i] && !used[o] ){
				used[o]=1;
				--res;
				break;
			}
		}
	}
	return res;

}

int deceit(int cur, int tot){

	if( cur == N ) return tot;

	if( G[maxG] > B[maxB] ){
		used[maxB] = 1;
		--maxG, --maxB;
		return deceit(cur+1,tot+1);
	}

	else{
		minG++;
		--maxB;
		return deceit(cur+1,tot);
	}
	
}


int main(){
	scanf("%d",&TC);
	for(int tc=1; tc<=TC; ++tc){

		scanf("%d",&N);
		for(int i=0; i<N; ++i) scanf("%lf",&G[i]);
		for(int i=0; i<N; ++i){
			used[i]=0;
			scanf("%lf",&B[i]);
		}
		sort(G,G+N); sort(B,B+N);
		maxB = N-1; maxG = N-1;
		minB = 0; minG = 0;
		//for(int i=0; i<N; ++i) cout<<B[i]<<endl;

		printf( "Case #%d: %d %d\n", tc, deceit(0,0), war() );

	}

	return 0;
}
