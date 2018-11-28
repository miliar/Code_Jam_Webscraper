//============================================================================
// File        : main.cpp
// Author      : AHMED HANI IBRAHIM
// Copyright   : AHani
// Version     : UVa - Accepted - 0.032
// Created on April 11, 2013, 2:33 AM
//============================================================================

#include <cstdlib>
#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>
#include <math.h>
#define Max 1000 + 5
#define INF 1000000000
//#define INT_MAX 2147483647
#define FOR(i, N) for( long long i = 0 ; i < N ; i++ )
#define FOR1e(i, N) for( long long i = 1 ; i <= N ; i++ )
#define FORe(i, N) for(long long i = 0 ; i <= N ; i++ )
#define FOR1(i, N) for(long long i = 1 ; i < N ; i++ )

using namespace std;

int TestCases;
long long First, Second;
long long Counter;

vector<long long> Generate(long long Size) {
    vector<long long> Result;
    while(Size) {
        long long Tmp = Size % 10;
        Result.push_back(Tmp);
        Size = Size / 10;
    }
    return Result;
}

bool IsPalindrome(vector<long long> N) {
    long long Last = N.size() - 1;
    for(long long i = 0; i < N.size() / 2; i++) {
        if(N[i] != N[Last]) {
            return false;
            Last--;
        }
    }
    return true;
}

bool Solve(long long Start, long long End) {
    vector<long long> Input = Generate(Start);
    long long Middle = sqrt(Start);
    if(Middle > End || Middle * Middle < Start)         return false;
    if(IsPalindrome(Input) && IsPalindrome(Generate(Middle))) return true;
    else        return false;
}


int main(int argc, char** argv) {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int Cases = 1;
    scanf("%d", &TestCases);
    while(TestCases-- > 0) {
        scanf("%lld %lld", &First, &Second);
        Counter = 0LL;
        for(long long i = min(First, Second); i <= max(First, Second); i++) {
            if(Solve(i, max(First, Second)))    Counter++;
        }
        printf("Case #%d: ", Cases++);
        printf("%lld\n", Counter);
    }
         
    
    return 0;
}

