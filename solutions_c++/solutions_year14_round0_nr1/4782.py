#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>

using namespace std;

int T,hang,lie,ge,number;
int array1[20][20],array2[20][20];

void work( int cas ){
		scanf("%d",&hang);
		int i,j;
		ge = 0,number = 0;

		for ( i = 1; i <= 4; ++i )
			for ( j = 1; j <= 4; ++j )
				scanf("%d",&array1[i][j]);

		scanf("%d",&lie);
		for ( i = 1; i <= 4; ++i )
			for ( j = 1; j <= 4; ++j )
				scanf("%d",&array2[i][j]);


		for ( i = 1; i <= 4; ++i )
			for ( j = 1; j <= 4; ++j )
				if ( array1[hang][i] == array2[lie][j] ) {
					number = array1[hang][i];
					ge++;
				}
		printf("Case #%d: ",cas);

		if ( ge == 0 ) printf("Volunteer cheated!\n");

		if ( ge > 1 ) printf("Bad magician!\n");

		if ( ge == 1 ) printf( "%d\n",number);


}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	scanf("%d",&T);
	int i;
	for ( int i = 1; i <= T; ++i ) work(i);
	return 0;
}
