#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int a[4][4], b[4][4];

int main( ){
	int casos;
	scanf("%d",&casos);
	for( int k=0; k<casos; k++ ){
		int choose_a, choose_b;
		vector< int > ans;
		scanf("%d",&choose_a);
		choose_a--;
		for( int i=0; i<4; i++ )
			for(int j=0; j<4; j++)
				scanf("%d",&a[i][j]);

		scanf("%d",&choose_b);
		choose_b--;
		for( int i=0; i<4; i++ )
			for(int j=0; j<4; j++){
				scanf("%d",&b[i][j]);

			}


		for( int i=0; i<4; i++ )
			for(int j=0; j<4; j++){
				if( a[choose_a][i] == b[choose_b][j])
					ans.push_back( a[choose_a][i]);
			}
		
		printf("Case #%d: ", k+1 );
		if( ans.size() == 0 ) printf("Volunteer cheated!\n");
		if( ans.size() > 1 )  printf("Bad magician!\n");
		if( ans.size()==1  )  printf("%d\n", ans[0] );

	}
	return 0;	
}