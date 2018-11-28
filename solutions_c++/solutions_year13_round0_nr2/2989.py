#include<iostream>
#include<cstdio>
#include<string.h>

using namespace std;

main () {
	int cases;
	int Matrix[100][100];
	int N,M;
	int R[100];
	int C[100];
	bool valid = true;
	scanf("%d",&cases);
	for ( int z=1; z <= cases; z++) {
		valid = true;
		scanf("%d %d",&N,&M);
		for ( int i=0; i < N ; i++ ) {
   			for ( int j=0; j < M; j++ ){
   				scanf("%d",&Matrix[i][j]);
   			}
		}
		
		memset(R,0,sizeof(R));
		memset(C,0,sizeof(C));
		
		for ( int i=0; i < N ; i++ ) {
   			for ( int j=0; j < M; j++ ){
   				if ( Matrix[i][j] > R[i] ) { 
   					R[i] = Matrix[i][j];
   				}
   				if ( Matrix[i][j] > C[j] ) {
   					C[j] = Matrix[i][j]; 
   				}	
   			}
		}
		
		for ( int i=0; i < N ; i++ ) {
   			for ( int j=0; j < M; j++ ){
   				if ( Matrix[i][j] < C[j] && Matrix[i][j] < R[i] ) {
   					valid = false;
   				}
   			}
		}
		
		if ( valid ) {
			printf("Case #%d: YES\n",z);
		} else {
			printf("Case #%d: NO\n",z);
		}
		
	}


}
