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

using namespace std;

void test(int T)
{
    int n;
    string s;
    int sum = 0;
    cin>>n>>s;
    int answ = 0;
    for(int i = 0; i < s.length(); ++i)
    {
        if(i > sum && s[i] > '0')
        {
            int d = i - sum;
            sum += d;
            answ += d;
        }
        sum += s[i] - '0';
    }
    printf("Case #%d: %d\n", T, answ);
}

int main(int argc, const char * argv[])
{

    freopen("/Users/olpet/Downloads/tmp_files/a.in", "r", stdin);
    freopen("/Users/olpet/Downloads/tmp_files/a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}

