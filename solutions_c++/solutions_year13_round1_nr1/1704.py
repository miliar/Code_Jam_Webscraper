#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <string>

using namespace std;

long long calcBullseye( long long t, long long r ){
	long long count = 0;

	for( long long i = r; ; i+=2 ){
		long long a = 2*i+1;
		if( t - a >= 0 ){
			t -= a;
			count++;
		}
		else{
			break;
		}
	}

	return count;
}


int main( int argc, char *argv[] )
{
	char input[512];
#if 1
	strcpy( input, argv[1] );
#else if
	strcpy( input, "A-small-attempt0.in" );
#endif

	printf( "input = %s\n", input );
	FILE *fp = fopen( input, "r" );

	if( fp != NULL ){
		char buff[512] = {0};
		int dataNum = 0;

		fgets( buff, 512-1, fp );
		sscanf( buff, "%d", &dataNum );
		printf( "dataNum = %d\n", dataNum );
		char (*out)[256] = new char[dataNum][256];

		for( int i = 0; i < dataNum; i++ ){

			long long r, t;
			fscanf( fp, "%I64d %I64d",  &r, &t );
			printf( "%d : %I64d %I64d\n", i+1, r, t);
			long long ret = calcBullseye( t, r );
			sprintf( out[i], "Case #%d: %I64d", i+1, ret );
			printf( "%s\n", out[i] );
		}
		fclose(fp);

		fp = fopen( "Bullseye.out", "w" );
		for( int i = 0; i < dataNum; i++ ){
			fprintf( fp, "%s\n", out[i] );
		}
		fclose(fp);
		delete []out;
	}
	return 0;
}