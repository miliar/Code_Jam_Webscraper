//
//  main.cpp
//  A
//
//  Created by Oleg Petrov on 12/04/2014.
//  Copyright (c) 2014 Oleg Petrov. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <cstring>

using namespace std;
int c,d,v;
bool dyn[666];
int mas[666];

void test(int T)
{
    int answ = 0;
    scanf("%d%d%d",&c,&d,&v);
    for(int i = 0; i < d; ++i)
        scanf("%d", mas+i);
    sort(mas, mas+d);
    long long pos = 0;
    long long sum = 0;
    while(sum < v)
    {
        if(pos < d && mas[pos] <= sum + 1)
        {
            sum += c * (long long)mas[pos];
            ++pos;
        }
        else
        {
            ++answ;
            sum += c * (sum + 1);
        }
    }
    printf("Case #%d: %d\n", T, answ);
}

int main(int argc, const char * argv[])
{
    
    freopen("/Users/olpet/Downloads/tmp_files/c.in", "r", stdin);
    freopen("/Users/olpet/Downloads/tmp_files/c.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}

/*
 1
 6 2 2
 GOOGLE
 GO
 */

