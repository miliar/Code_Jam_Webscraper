#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;
#define MAX 100000000000005LL
vector< long long > v;

int digit[ 105 ] , sz;
void getDigits( long long n ){
    sz = 0;
    int digitInv[ 105 ] , i , j;
    while( n > 0 ){
        digitInv[ sz++ ] = n % 10;
        n /= 10;
    }

    for( i = sz - 1 , j = 0 ; i >= 0 ; --i , ++j ){
        digit[ j ] = digitInv[ i ];
    }
}

bool pal( unsigned long long n ){
    getDigits( n );
    int left = 0 , right = sz;
    while( left < right ){
        if( digit[ left ] != digit[ right - 1 ] ) return false;
        left++;
        right--;
    }
    return true;
}

void brute(){
    unsigned long long i = 1;
    for( ; i * i <= MAX ; ++i ){
        if( pal( i ) && pal( i * i) ) v.push_back( i * i );
    }
}

int main(){

    brute();
    int t , i , cnt;
    long long a , b;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    for( int q = 1 ; q <= t && scanf("%lld %lld" , &a , &b ) ; ++q ){
        printf("Case #%d: " , q  );
        cnt = 0;
        for( i = 0 ; i < v.size() ; ++i ) if( v[ i ] >= a && v[ i ] <= b ) cnt++;
        printf("%d\n" , cnt );
    }
    return 0;
}
