#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <string>

using namespace std;

const int maxSize = 1000000;


long long getConsonants( char *str, int n, int *buff){
	long long ret = 0;
	
	char *p = str;
	int *b = buff;
	int size = 0;

	while(1){
		if( *p == '\0' ){
			break;
		}
		else{
			size++;
			if( *p == 'a' || *p == 'i' || *p == 'u' || *p == 'e' || *p == 'o' ){
				*b = 0;
			}
			else{
				*b = 1;
			}
			p++;
			b++;
		}
	}

	for( int i = size-2; i >= 0; i-- ){
		if( buff[i] > 0 ){
			buff[i] = buff[i+1]+1;
		}
	}

	int basePos = 0;
	for( int i = 0; i < size; i++ ){
		if( buff[i] >= n){
			//ret += i + 1 - basePos;
			ret += (i + 1 - basePos) * (size - i - n + 1);
			basePos = i+1;
		}
	}


	return ret;
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

		char *str = new char[maxSize+1];
		int *dataBuff = new int[maxSize];
		for( int i = 0; i < dataNum; i++ ){

			int n;
			fscanf( fp, "%s %d",  str, &n );
			
			long long ret = getConsonants( str, n, dataBuff );
			sprintf( out[i], "Case #%d: %I64d", i+1, ret );
			printf( "%s\n", out[i] );
		}
		delete []str;

		fclose(fp);

		fp = fopen( "Consonants.out", "w" );
		for( int i = 0; i < dataNum; i++ ){
			fprintf( fp, "%s\n", out[i] );
		}
		fclose(fp);
		delete []out;
	}
	return 0;
}