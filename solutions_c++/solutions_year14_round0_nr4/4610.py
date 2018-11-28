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
#define MAX 10005
double a[ MAX ] , b[ MAX ];
int n;
bool cmp( double n1 , double n2 ){
    return n1 > n2;
}
int war(){
    int maxi = 0;
    deque<double> Q1 , Q2;
    for( int i = 0 ; i < n; ++i ){
        Q1.push_back( a[ i ] );
    }

    for( int i = 0 ; i < n; ++i ){
        Q2.push_back( b[ i ] );
    }

    while( !Q1.empty() ){
        double m1 = Q1.front(); Q1.pop_front();
        double m2 = Q2.front();
        if( m1 > m2 ){
            double p2 = Q2.back();
            if( p2 < m1 ){
                maxi++;
            }
            Q2.pop_back();
        }else{
            Q2.pop_front();
        }
    }
    return maxi;
}

int deceitful(){
    int maxi = 0;
    deque<double> Q1 , Q2;
    for( int i = 0 ; i < n; ++i ){
        Q1.push_back( a[ i ] );
    }

    for( int i = 0 ; i < n; ++i ){
        Q2.push_back( b[ i ] );
    }

    while( !Q1.empty() ){
        double m1 = Q1.front();
        double m2 = Q2.front(); Q2.pop_front();
        if( m1 < m2 ){
            double p1 = Q1.back();
            if( p1 > m2 ){
                maxi++;
            }
            Q1.pop_back();
        }else{
            if( m1 > m2 )
                maxi++;
            Q1.pop_front();
        }
    }
    return maxi;
}

double fRand(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

int main(){
    int t, q , i,  j;
    //freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    for( q = 1 ; q <= t && scanf("%d" , &n ) ; ++q ){
        for( i = 0 ; i < n && scanf("%lf" , &a[ i ] ) ; ++i );
        for( i = 0 ; i < n && scanf("%lf" , &b[ i ] ) ; ++i );
        sort( a , a + n , cmp );
        sort( b , b + n , cmp );
        printf("Case #%d: %d %d\n" , q , deceitful() , war() );
    }
    return 0;
}
