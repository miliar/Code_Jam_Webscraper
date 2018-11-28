#include <iostream>
#include <cstdlib>

using namespace std;

int card[17];
int mat1[4][4];
int mat2[4][4];

int main()
{
	int T,a,b;
	while ( scanf("%d",&T) != EOF ) 
	for ( int t = 1 ; t <= T ; ++ t ) {
		scanf("%d",&a);
		for ( int i = 0 ; i < 4 ; ++ i )
		for ( int j = 0 ; j < 4 ; ++ j )
			scanf("%d",&mat1[i][j]);
		scanf("%d",&b);
		for ( int i = 0 ; i < 4 ; ++ i )
		for ( int j = 0 ; j < 4 ; ++ j )
			scanf("%d",&mat2[i][j]);
		for ( int i = 1 ; i < 17 ; ++ i )
			card[i] = 0;
		for ( int i = 0 ; i < 4 ; ++ i ) {
			card[mat1[a-1][i]] ++;
			card[mat2[b-1][i]] ++;
		}
		int count = 0,max = 0;
		for ( int i = 1 ; i < 17 ; ++ i ) 
			if ( card[i] == 2 ) {
				max = i;
				count ++;
			}
		
		printf("Case #%d: ",t);
		if ( count == 1 ) printf("%d\n",max);
		else if ( count ) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	
	return 0;
}
