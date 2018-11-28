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
#define MAX 20
int seen[ MAX ];
int main(){
    int t, q , i,  j , x , r1 , r2;
    //freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    for( q = 1 ; q <= t ; ++q ){
        scanf("%d" , &r1 );
        memset( seen , 0 , sizeof( seen ) );
        for( i = 1 ; i <= 4 ; ++i ){
            for( j = 1 ; j <= 4 && scanf("%d" , &x); ++j ){
                if( i == r1 ){
                    seen[ x ]++;
                }
            }
        }
        scanf("%d" , &r2 );
        for( i = 1 ; i <= 4 ; ++i ){
            for( j = 1 ; j <= 4 && scanf("%d" , &x); ++j ){
                if( i == r2 ){
                    seen[ x ]++;
                }
            }
        }

        printf("Case #%d: " , q  );
        int ans = -1;
        bool solved = false;
        for( i = 1 ; i <= MAX ; ++i ){
            if( seen[ i ] > 1 ){
                if( ans == -1 )
                    ans = i;
                else{
                    printf("Bad magician!\n");
                    solved = true;
                    break;
                }
            }
        }

        if( !solved ){
            if( ans == -1 ){
                puts("Volunteer cheated!");
            }
            else
                printf("%d\n" , ans );
        }
    }
    return 0;
}
