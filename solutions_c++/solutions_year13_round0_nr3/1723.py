#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <string>

using namespace std;

const int maxSize = 100;

int cmpStr( const char *cS1, const char *cS2, const int max ){
	int ret = 0;
	for( int i = max; i >= 0; i-- ){
		if( cS1[i] < cS2[i] ){
			ret = -1;
			break;
		}
		else if( cS1[i] > cS2[i] ){
			ret = +1;
			break;
		}
	}
	return ret;
}
void pow( char *dst, const char *src, int len ){
	memset( dst, 0, maxSize );
	char buff[maxSize][maxSize] = {0};
	for( int i = 0; i < len; i++ ){
		int pre = 0;
		for( int j = 0; j < len; j++ ){
			int val = src[i]*src[j] + pre;
			buff[i][j+i] = val % 10;
			pre = val / 10;
		}
		buff[i][len+i] = pre;
	}
	{
		int pre = 0;

		for( int i = 0; i < 2*len; i++ ){
			dst[i] = pre;
			for( int j = 0; j < len; j++ ){
				dst[i] += buff[j][i];
			}
			int val = dst[i];
			dst[i] = val % 10;
			pre = val/10;
		}
	}

}
//bool searchSqrt( const char *src, const int pos1, const int pos2 ){
//	bool ret = false;
//	char cpr[maxSize] = {0};
//
//	while( 1 ){
//
//	}
//	return ret;
//}
//bool checkSqrt( const char *src, const int maxLen, const int range ){
//	bool ret = false;
//	if( (maxLen % 2) == 0 ){
//		int pos = maxLen / 2;
//		ret = searchSqrt( src, pos-1-range, pos+range );
//	}
//	else{
//		int pos = maxLen / 2;
//		ret = searchSqrt( src, pos-range, pos+range );
//	}
//
//	return ret;
//}
//void setVal( char *src, const int maxLen, const int range, const char val ){
//	if( (maxLen % 2) == 0 ){
//		int pos = maxLen / 2;
//		src[(pos-1) - range] = src[pos + range] = val;
//	}
//	else{
//		int pos = maxLen / 2;
//		src[pos - range] = src[pos + range] = val;
//	}
//}
//int calcStr( const char *src, const int maxLen, const int range, const char *cA, const int lenA, const char *cB, const int lenB ){
//	char subS[maxSize] ={0};
//	memcpy( subS, src, maxSize );
//
//	int ret = 0;
//	for( int i = 0; i < 10; i++ ){
//		setVal( subS, maxLen, range, i );
//		if( checkSqrt( subS, maxLen, range ) ){
//			
//			if( 2*range > maxLen ){
//				if( conpStr( subS, cA, lenB ) >= 0 && conpStr( subS, cB, lenB ) <= 0 ){
//					ret++;
//				}
//			}
//			else{
//				ret += calcStr( subS, maxLen, range+1, cA, lenA, cB, lenB );
//			}
//		}
//	}
//	return ret;
//}
void printStr( const char *src, const int srcLen ){
	//for( int i = srcLen - 1; i >= 0; i-- ){
	//	printf( "%d", src[i] );
	//}
	//printf("\n");
}
//int subStr( const char *cS1, const char *cS2, const int max ){
//	int ret = 0;
//	int pre = 0;
//
//	for( int i = 0; i < max; i++ ){
//
//		if( cS1[i] < cS2[i] ){
//			ret = -1;
//			break;
//		}
//		else if( cS1[i] > cS2[i] ){
//			ret = +1;
//			break;
//		}
//	}
//	return ret;
//}
void addOneStr( char *cS1, int pos ){
	for( int i = pos; i < maxSize; i++ ){
		if( cS1[i] < 9 ){
			cS1[i]++;
			break;
		}
		else{
			cS1[i] = 0;
		}
	}
}
void nextFairStr( char *src, int srcLen ){
	while( src[srcLen-1] == 0 ){
		srcLen--;
	}
	bool flag = false;
	for( int i = 0; i < srcLen/2; i++ ){
		if( src[i] != src[srcLen-1-i] ) flag = true;
		src[i] = src[srcLen-1-i];
	}
	if( flag ) return;


	addOneStr( src, srcLen/2 );
	if( src[srcLen] > 0 ){
		memset( src, 0, maxSize );
		src[srcLen] = 1;
		src[0] = 1;
	}
	else{
		for( int i = 0; i < srcLen/2; i++ ){
			src[i] = src[srcLen-1-i];
		}
	}
}
bool calcNearSqrt( char *dst, int &dstLen, const char *src, const int srcLen ){
	memset( dst, 0, maxSize );

	dstLen = srcLen / 2 + 1;
	char cmp[maxSize] = {0};
	for( int i = dstLen-1; i >= 0; i-- ){
		for( int n = 0; n < 10; n++ ){
			dst[i] = n;
			pow( cmp, dst, srcLen );
			int ret = cmpStr( cmp, src, 2*srcLen );
			if( ret == 0 ){
				return true;
			}
			else if( ret > 0 ){
				dst[i] = n-1;
				break;
			}
		}
	}
	return false;
}
bool checkFair( char *src, int srcLen ){
	bool ret = true;

	while( src[srcLen-1] == 0 ){
		srcLen--;
	}

	for( int i = 0; i < srcLen/2; i++ ){
		if( src[i] != src[srcLen-1-i] ){
			ret = false;
			break;
		}
	}
	return ret;
}
int calc( const char *cA, const int lenA, const char *cB, const int lenB ){
	int ret = 0;

	char nSA[maxSize] = {0};
	char nSB[maxSize] = {0};
	int nSLenA = 0, nSLenB = 0;

	bool offset = calcNearSqrt( nSA, nSLenA, cA, lenA );
	if( offset == true ){
		offset = checkFair( nSA, nSLenA );
	}
	calcNearSqrt( nSB, nSLenB, cB, lenB );

	printStr( nSA, nSLenA );
	printStr( nSB, nSLenB );

	char crnt[maxSize] = {0};
	char dst[maxSize] = {0};
	memcpy( crnt, nSA, maxSize );

	if( offset == false ){
		nextFairStr( crnt, nSLenB );
		int cmp = cmpStr( crnt, nSA, nSLenA+1 );
		if( cmp < 0 ){
			nextFairStr( crnt, nSLenB );
		}
		printStr( crnt, nSLenB );
	}
	while( 1 ){
		int cmp = cmpStr( crnt, nSB, nSLenB+1 );
		if( cmp > 0 ) break;	
		pow( dst, crnt, nSLenB );
		printStr( dst, 2*nSLenB );
		
		bool ch = checkFair( dst, 2*nSLenB );
		if( ch ) ret++;

		nextFairStr( crnt, nSLenB );
		printStr( crnt, nSLenB );

	}
	
	return ret;
}

int countFairAndSquare( const char *A, const char *B ){
	int ret= 0;


	int lenA = strlen( A );
	int lenB = strlen( B );
	char cA[maxSize] = {0};
	char cB[maxSize] = {0};

	for( int i = 0; i < lenA; i++ ){
		char str[2] = {0};
		str[0] = A[lenA-1-i];
		cA[i] = atoi(str);
	}
	for( int i = 0; i < lenB; i++ ){
		char str[2] = {0};
		str[0] = B[lenB-1-i];
		cB[i] = atoi(str);
	}

	//for( int i = lenA-1; i >=0; i-- ){
	//	printf("%d", cA[i] );
	//}
	//printf("\n");
	//for( int i = lenB-1; i >=0; i-- ){
	//	printf("%d", cB[i] );
	//}
	//printf("\n");
	ret = calc( cA, lenA, cB, lenB );

	return ret;
}


int main( int argc, char *argv[] )
{
	char input[512];
#if 1
	strcpy( input, argv[1] );
#else if
	strcpy( input, "C-small-attempt0.in" );
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

			char min[256], max[256];
			fscanf( fp, "%s %s",  &min, &max );
			
			int ret = countFairAndSquare( min, max );
			sprintf( out[i], "Case #%d: %d", i+1, ret );
			printf( "%s\n", out[i] );
		}
		fclose(fp);

		fp = fopen( "FairAndSquare.out", "w" );
		for( int i = 0; i < dataNum; i++ ){
			fprintf( fp, "%s\n", out[i] );
		}
		fclose(fp);
		delete []out;
	}
	return 0;
}