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

typedef long long DIGIT;

int main() {

//    cout<<" limit is "<< std::numeric_limits<DIGIT>::max() <<" "<< std::numeric_limits<DIGIT>::min();
//    if( std::numeric_limits<DIGIT>::max() < 100000 * 100000 ){
//        cout<<" limit is not enough! ";
//    }

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ntests;
	scanf(" %d", &ntests);
	for( int test = 1; test <= ntests; ++test ) {
		printf("Case #%d: ", test);

		DIGIT rad;
		DIGIT tpaint;

		scanf( "%lld", &rad );
		scanf( "%lld", &tpaint );

		DIGIT answer = 1;
		tpaint -= pow(rad+1,2)-pow(rad,2);

		while(1){
            tpaint -= 2*rad+4*answer+1 ;//pow( rad + answer*2+1 , 2) - pow( rad + answer*2 , 2 );
            if( tpaint < 0 ){
                break;
            }
            answer++;
		}


        printf( "%lld\n", answer );
	}
}
