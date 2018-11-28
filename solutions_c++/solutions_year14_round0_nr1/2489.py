#include <iostream>
#include <cstdio>

#define ZERO 0
#define ONE 1
#define TWO 2

using namespace std;

int main()
{
	int t,r1,r2,state,test = 1,num;
	int mat1[4][4],mat2[4][4],arr[17];
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%d",&r1);
		for ( int i = 0; i < 4; i++ ) 
			for ( int j = 0; j < 4; j++ ) 
				scanf("%d",&mat1[i][j]);
		scanf("%d",&r2);
		for ( int i = 0; i < 4; i++ ) 
			for ( int j = 0; j < 4; j++ ) 
				scanf("%d",&mat2[i][j]);

		fill(arr,arr+17,0);
		r1 -= 1; r2 -= 1;
		for ( int i = 0; i < 4; i++ ) arr[ mat1[r1][i] ] += 1;
		state = ZERO;
		for ( int i = 0; i < 4; i++ ) {
			arr[ mat2[r2][i] ] += 1;
			if ( state == ZERO ) {
				if ( arr[ mat2[r2][i] ] == 2 ) {
					state = ONE;
					num = mat2[r2][i];
				}
			}
			else if ( state == ONE ) {
				if ( arr[ mat2[r2][i] ] > 1 && num != mat2[r2][i] ) {
					state = TWO;
				}
			}
			else if ( state == TWO ) break;
		}

		printf("Case #%d: ",test);
		if ( state == ZERO ) printf("Volunteer cheated!\n");
		else if ( state == TWO )  printf("Bad magician!\n");
		else if ( state == ONE ) printf("%d\n",num);
		test++;
	}
}
