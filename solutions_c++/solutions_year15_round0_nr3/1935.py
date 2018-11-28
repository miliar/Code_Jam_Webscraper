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

int matr[8][8];
int tmatr[4][4] = {
    {0, 1, 2, 3},
    {1, 4, 3, 6},
    {2, 7, 4, 1},
    {3, 2, 5, 4}};

int need[3] = {1, 3, 4};

void test(int T)
{
    string answ = "NO";
    string s;
    int l, x;
    cin>>l>>x>>s;
    int stay = 0;
    int pos = 0;
    for(int i = 0; i < x; ++i)
        for(int j = 0; j < l; ++j)
        {
            int cur = s[j] - 'i' + 1;
            stay = matr[stay][cur];
            if(pos < 3 && stay == need[pos])
                ++pos;
        }
    if(pos == 3 && stay == 4)
        answ = "YES";
    printf("Case #%d: %s\n", T, answ.c_str());
}

int main(int argc, const char * argv[])
{

    freopen("/Users/olpet/Downloads/tmp_files/c.in", "r", stdin);
    freopen("/Users/olpet/Downloads/tmp_files/c.out", "w", stdout);
    for(int i = 0; i < 8; ++i)
        for(int j = 0; j < 8; ++j)
        {
            bool invert = (i>=4)^(j>=4);
            int trg = tmatr[i % 4][j % 4];
            if(!invert)
                matr[i][j] = trg;
            else
                matr[i][j] = (trg + 4) % 8;
        }
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}

