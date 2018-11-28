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
//#include <time.h>
using namespace std;
#define MAX 10
#define pii pair<long long , long long>
#define mp make_pair

int seen;
void mark( long long n ){
    while( n > 0 ){
        seen |= 1<<(n % 10);
        n /= 10;
    }
}

int countOnes( int x ){
    int ones = 0;
    while( x ){
        x = x & ( x - 1 );
        ones++;
    }
    return ones;
}

void simulate( long long n ){
    seen = 0;
    for( long long i = 1 ; i < 200 ; ++i ){
        mark(n * i);
        if( countOnes(seen) == 10 ){
            printf("%lld\n", n * i);
            return;
        }
    }
    puts("INSOMNIA");
}

int main() {
    //srand (time(NULL));
    //for( int i = 0 ; i <= 1000000 ; ++i ){
    //    simulate(i);
    //}
    int t;
    int n;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d" , &n ) ; ++q ){
        printf("Case #%d: ", q  );
        if( n == 0 ){
            puts("INSOMNIA");
        }else{
            simulate(n);
        }
    }
    return 0 ;
}
