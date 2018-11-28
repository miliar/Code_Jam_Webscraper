#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>
#include <limits>
using namespace std;

typedef unsigned long long int64;

int64 issquare( int64 Number )
{
    double root = sqrt( Number );
    if( root - ( (int64) root ) == 0 ){
        return (int64) root;
    }
    return -1;
}

bool ispolindrome( int64 Number )
{
    char buff[105];
    itoa( Number, buff, 10 );
    string str(buff);
    int64 len = str.size() - 1;
    for( int i = 0; i <= len ; i++ ){
        if( str[i] != str[ len - i ] ){
            return false;
        }
    }
    return true;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ntests;
	scanf(" %d", &ntests);
	for( int test = 1; test <= ntests; ++test ) {
		printf("Case #%d: ", test);

		int64 A = 0,B = 0 ;
		scanf("%lld",&A);
		scanf("%lld",&B);

        int count = 0;
		for( ; A <= B; ++A ){
		    int64 root = issquare( A );
		    if( root != -1 ){
		        if( ispolindrome( root ) && ispolindrome(A) ){
		            count++;
		        }
		    }
		}

		printf("%d\n", count);
	}
}
