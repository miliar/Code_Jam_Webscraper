#include<iostream>
#include<cstdio>
using namespace std;
int C[4],R[4];
int main(){

	int runs, k;
	scanf("%d",&runs);
	for( int r = 1; r <= runs; r++){
		int row1;
		scanf("%d",&row1);
		k = 0;
		row1--;
		for( int i = 0; i < 4;i++){
			for( int j = 0; j < 4; j++){
				int tmp; 
				scanf("%d",&tmp);
				if ( i == row1 ) C[k++] = tmp;
			}
		}
		int row2;
		scanf("%d",&row2);
		k = 0;
		row2--;
		for( int i = 0; i < 4;i++){
			for( int j = 0; j < 4; j++){
				int tmp; 
				scanf("%d",&tmp);
				if ( i == row2 ) R[k++] = tmp;
			}
		}
		int ans, dup = 0;
		for( int i = 0; i < 4; i++){
			for( int j = 0; j < 4; j++){
				if ( C[i] == R[j] ) {
					ans = C[i];
					dup++;
				}
			}
		}
		printf("Case #%d: ",r);
		if ( dup > 1 ) puts("Bad magician!");
		else{
			if ( dup == 0 ) puts("Volunteer cheated!");
			else printf("%d\n", ans );
		}
	}

	return 0;
}
