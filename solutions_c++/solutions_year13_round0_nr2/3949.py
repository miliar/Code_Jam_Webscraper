#include <algorithm>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>

bool f1 (int** tmp, int length, int rc, int value, int direction, int index) {
	// printf("length=%d, value=%d, direction=%d, index=%d \n",length,value,direction,index);
	if (index < length) {
		if (direction) {
			// printf("tmp[%d][%d]=%d, value=%d\n", index, rc, tmp[index][rc], value);
			if (tmp[index][rc] == value || !tmp[index][rc] ) 
				return f1(tmp, length, rc, value, 1, index+1);
			else {
				// printf("false\n");
				return false;
			}
		}
		else {
			// printf("tmp[%d][%d]=%d, value=%d\n", rc, index, tmp[rc][index], value);
			if (tmp[rc][index] == value || !tmp[rc][index] ) 
				return f1(tmp, length, rc, value, 0, index+1);
			else {
				// printf("false\n");
				return false;
			}
		}
	}
	else {
		// printf("true\n");
		return true;
	}
}

void main() {
	int i,j;
	int N,M,T,Trun=1;
	int end,counter,killed,height = 100;
	std::cin >> T;
	while(Trun <=T) {
		end = 0, counter = 1, killed = 0;
		std::cin >> N >> M;	
		int* hash = new int[height+1];
		int* xhash = new int[M];
		int* yhash = new int[N];
		int** d = new int*[N];
		for ( i = 0; i <= height; i++ )
			hash[i] = 0;
		for( i = 0; i < N; i++ ) {
			d[i] = new int[M];
			for ( j = 0; j < M; j++ ) {
				std::cin >> d[i][j];
				hash[d[i][j]]++;
			}
		}
		// printf("\n");
		// for ( i = 0; i < height+1 ; i++ ){
		// 	printf("%d ",hash[i]);
		// }
		// printf("\n");
		while ( counter <= height && !end ) {
			if ( hash[counter] ) {
				killed = 0;
				for( i = 0; i < M; i++ ) 
					if ( f1(d, N, i, counter, 1, 0) ) {
						xhash[i]=1;
					}
				for( j = 0; j < N; j++ ) 
					if ( f1(d, M, j, counter, 0, 0) ) {
						yhash[j]=1;
					}
				// for ( i = 0; i < N; i++ ) {
				// 	for ( j = 0; j < M; j++ )
				// 			printf("%d ",d[i][j]);
				// 	printf("\n");
				// }
				for ( i = 0; i < M; i++ )
					if ( xhash[i] == 1)
						for ( j = 0; j < N; j++ ) {
							if ( d[j][i] ) {
								killed++;
								d[j][i] = 0;
							}
						}
				for ( j = 0; j < N; j++ )
					if ( yhash[j] == 1 )
						for ( i = 0; i < M; i++ ) {
							if ( d[j][i] ) {
								killed++;
								d[j][i] = 0;
							}
						}
				if ( hash[counter] > killed ) {
					end=1;
					break;
				}
			}
			counter++;
		}
		if (end) 
			printf("Case #%d: No\n", Trun++);
		else 
			printf("Case #%d: Yes\n", Trun++);
		for( i = 0; i < N; i++ )
			delete[] d[i];
		delete[] hash,yhash,yhash,d;
	}

}

