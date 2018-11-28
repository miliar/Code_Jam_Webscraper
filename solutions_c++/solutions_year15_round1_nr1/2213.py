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
#define MAX 1005
int a[ MAX ];
int main() {
    //srand (time(NULL));
    int t, n , ans1 , ans2;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d" , &n ) ; ++q ){
        for( int i = 0 ; i < n && scanf("%d" , &a[i]) ; ++i );
        ans1 = 0; ans2 = 0;
        int maxi = 0;
        for( int i = 1 ; i < n ; ++i ){
            if( a[i - 1] > a[ i ] ){
                ans1 += a[ i - 1 ] - a[i ];
                maxi = max( maxi , a[ i - 1 ] - a[i] );
            }
        }

        for( int i = 0 ; i < n - 1 ; ++i ){
            if( a[i] <= maxi )
                ans2 += a[i];
            else{
                ans2 += maxi;
            }
        }

        printf("Case #%d: %d %d\n", q , ans1 , ans2 ) ;
    }
    return 0 ;
}
