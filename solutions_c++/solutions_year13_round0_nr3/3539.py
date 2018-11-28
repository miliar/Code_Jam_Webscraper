// QuaC.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <string.h>

const char *properPalindroms[] = {
	// 1 digit
	"1", "4", "9",
	// 3 digit
	"121", "484",
	// 5 digit
	"10201", "12321", "14641", "40804", "44944",
	// 7 digit
	"1002001", "1234321", "4008004",
	// 9 digit
	"100020001", "102030201", "104060401", "121242121", "123454321", "125686521", "400080004", "404090404",
	// 11 digit
	"10000200001", "10221412201", "12102420121", "12345654321", "40000800004",
	// 13 digit
	"1000002000001", "1002003002001", "1004006004001", "1020304030201", "1022325232201",
	"1024348434201", "1210024200121", "1212225222121", "1214428244121", "1230127210321",
	"1232346432321", "1234567654321", "4000008000004", "4004009004004"
};

const int tableSize = sizeof( properPalindroms ) / sizeof( *properPalindroms );

int _tmain(int argc, _TCHAR* argv[])
{
	int nTestCases = 0;

	scanf( "%u", &nTestCases );

	for ( int i = 0; i < nTestCases; i++ ) {
		char a[120] = {0};
		char b[120] = {0};

		scanf( "%s %s", &a, &b );

		bool biggerThanA = false;
		int strALen = strlen( a );
		int strBLen = strlen( b );
		int nPalindrons = 0;
		for ( int j = 0; j < tableSize; j++ ) {
			int currLen = strlen( properPalindroms[ j] );

			if ( !biggerThanA ) {
				if ( currLen < strALen ) {
					continue;
				} else if (currLen == strALen && strcmp( properPalindroms[ j], a ) < 0 ){
					continue;
				}
			}
			biggerThanA = true;

			if ( strBLen < currLen ) {
					break;
			} else if (strBLen == currLen && strcmp( b, properPalindroms[ j] ) < 0 ) {
					break;
			}

			nPalindrons++;
		}

		printf( "Case #%u: %u\n", i+1, nPalindrons );



	}
	return 0;
}

