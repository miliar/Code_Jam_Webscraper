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
#include <map>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int,int> pii;

bool has[120][120][4];
char mp[120][120];
int r,c;

map<char, pii> mmm;
pii SHIFT[5] = {{0,-1}, {0,1}, {1,0}, {-1,0}};

bool testPos(pii cur, pii nap)
{
    if(nap.first + nap.second == 0)
        return false;
    cur.first += nap.first;
    cur.second += nap.second;
    
    while(0 <= cur.first && cur.first < r &&
          0 <= cur.second && cur.second < c)
    {
        if(mp[cur.first][cur.second] != '.')
            return true;
        cur.first += nap.first;
        cur.second += nap.second;
    }
    return false;
}

bool testAtAll(pii cur)
{
    for(int i=0; i<4; ++i)
        if(testPos(cur, SHIFT[i]))
            return true;
    return false;
}

void test(int T)
{
    int answ = 0;
    memset(has, 0, sizeof(has));
    
    scanf("%d%d", &r,&c);
    for(int i=0; i<r; ++i)
        scanf("%s",mp[i]);
    
    for(int i = 0; i < r; ++i)
        for(int j = 0; j < c; ++j)
        {
            if(mp[i][j] == '.' || testPos(pii(i,j), mmm[mp[i][j]]))
                continue;
            if(testAtAll(pii(i,j)))
                ++answ;
            else
            {
                printf("Case #%d: IMPOSSIBLE\n", T);
                return;
            }
        }
    printf("Case #%d: %d\n", T, answ);
}

int main(int argc, const char * argv[])
{
    mmm['<'] = {0,-1};
    mmm['>'] = {0,1};
    mmm['v'] = {1,0};
    mmm['^'] = {-1,0};
    mmm['.'] = {0,0};
    freopen("/Users/olpet/Downloads/tmp_files/a.in", "r", stdin);
    freopen("/Users/olpet/Downloads/tmp_files/a.out", "w", stdout);
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

