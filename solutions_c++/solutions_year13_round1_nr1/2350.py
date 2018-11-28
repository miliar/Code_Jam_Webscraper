//============================================================================
// File        : 
// Author      : AHMED HANI IBRAHIM
// Copyright   : AHani
// Version     : 
// Created on April 27, 2012, 7:31 PM
//============================================================================

#include <cstdlib>
#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#define Max 50 + 5
#define INF 1000000000
//#define INT_MAX 2147483647
#define FOR(i, N) for( int i = 0 ; i < N ; i++ )
#define FOR1e(i, N) for( int i = 1 ; i <= N ; i++ )
#define FORe(i, N) for(int i = 0 ; i <= N ; i++ )
#define FOR1(i, N) for(int i = 1 ; i < N ; i++ )

using namespace std;

int TestCases; 
long long R, T, Sum, Result; 
 
int main(int argc, char** argv) {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &TestCases);
    int Cases = 1;
    while(TestCases-- > 0) {
        scanf("%lld %lld", &R, &T);
        int i = 1;
        Sum = Result = 0;
        while(true) {
            Sum += ((i + R) * (i + R)) - ((i - 1 + R) * (i - 1 + R));
            if(Sum > T)break;
            i += 2;
            Result++;
        }
        printf("Case #%d: %d\n", Cases++, Result);
    }

    return 0;
}

