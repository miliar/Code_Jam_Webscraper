
#include <stdio.h>
#include <tchar.h>

typedef unsigned char uchar;
typedef uchar lawn[101][101];


void checkRows( int sizeN, int sizeM, lawn pattern, lawn &negatives, int &negativesCount ) {
	int passed = 0;
	for ( int i = 0; i < sizeN; i++ ) {
		bool blocked = false;
		uchar edgeHeight = 0;

		for (int j = 0; j < sizeM; j++ ) {
			if ( pattern[ i][ j] > edgeHeight ) {
				edgeHeight = pattern[ i][ j];
			}
		}

		for (int j = 0; j < sizeM; j++ ) {
			if ( pattern[ i][ j] == edgeHeight ) {
				if ( !negatives[ i][ j] ) {
					// positive
					negatives[ i][ j] = 1;
					negativesCount--;
				}
			} else if ( pattern[ i][ j] > edgeHeight ) {
				blocked = true;
			}
		} // for j
	} // for i
}

void checkCols( int sizeN, int sizeM, lawn pattern, lawn &negatives, int &negativesCount ) {
	int passed = 0;
	for ( int i = 0; i < sizeM; i++ ) {
		bool blocked = false;
		uchar edgeHeight = 0;
		for ( int j = 0; j < sizeN; j++ ) {
			if ( pattern[ j][ i] > edgeHeight ) {
				edgeHeight = pattern[ j][ i];
			}
		}

		for ( int j = 0; j < sizeN; j++ ) {
			if ( ( pattern[ j][ i] == edgeHeight ) && !negatives[ j][ i] ) {
					// positive
					negatives[ j][ i] = 1;
					negativesCount--;
			}
		} // for j
	} // for i
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nTestCases = 0;
	scanf( "%u", &nTestCases );

	for ( int i = 0; i < nTestCases; i++ ) {
		lawn pattern = {0};
		int sizeN = 0; // rows
		int sizeM = 0; // cols
		scanf( "%u %u", &sizeN, &sizeM );

		// load pattern
		for ( int j = 0; j < sizeN; j++ ) {
			for ( int k = 0; k < sizeM; k++ ) {
				scanf( "%u", pattern[ j] + k );
			}
		}

		lawn negatives = {0};
		int negativesCount = sizeN * sizeM;

		if ( sizeN == 1 || sizeM == 1 ) {
			negativesCount = 0;
		} else {
			checkCols( sizeN, sizeM, pattern, negatives, negativesCount );
			checkRows( sizeN, sizeM, pattern, negatives, negativesCount );
		}

		printf("Case #%u: %s\n", i+1, (negativesCount == 0)?"YES":"NO" );
	}

	return 0;
}

