#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

#define ROWSIZE 4

void Solve( int caseId )
{
	int rowId1, rowId2;
	std::vector<int> intersect, row1, row2;
	int dummyLoad;

	scanf( "%d\n", &rowId1 );
	for( int i = 1; i <= ROWSIZE; i ++ )
	{
		for( int j = 0; j < ROWSIZE; j ++ )
		{
			scanf( "%d", & dummyLoad );
			if( rowId1 == i )
				row1.push_back( dummyLoad );
		}
	}

	scanf( "%d\n", &rowId2 );
	for( int i = 1; i <= ROWSIZE; i ++ )
	{
		for( int j = 0; j < ROWSIZE; j ++ )
		{
			scanf( "%d", & dummyLoad );
			if( rowId2 == i )
				row2.push_back( dummyLoad );
		}
	}

	std::sort( row1.begin(), row1.end() );
	std::sort( row2.begin(), row2.end() );
	std::set_intersection( row1.begin(), row1.end(), row2.begin(), row2.end(), std::back_inserter( intersect ) );

	// for( int i : row1 ) printf("%d ", i);
	// printf(" | ");
	// for( int i : row2 ) printf("%d ", i);
	// printf(" | ");
	// for( int i : intersect ) printf("%d ", i);

	printf("Case #%d: ", caseId );

	if( intersect.size() == 0 )
		printf( "Volunteer cheated!" );
	else if( intersect.size() == 1 )
		printf( "%d", * intersect.begin() );
	else
		printf( "Bad magician!" );

	printf("\n");
}

int main( int argc, char * argv [] )
{
	int cases;
	scanf( "%d\n", & cases);

	for( int i = 1; i <= cases; i++ )
		Solve( i );

	return 0;
}