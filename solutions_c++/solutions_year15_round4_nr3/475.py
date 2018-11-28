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
typedef pair<double,double> pdd;

vector<vector<string>> inp;
vector<vector<int>> oup;
vector<string> vvv;
int pha[3000];
int ok[3000];
int glob = 0;

int Init()
{
    int answ = 0;
    memset(pha, 0, sizeof(pha));
    for(int i=0; i<oup[0].size(); ++i)
        pha[oup[0][i]] |= 1;
    for(int i=0; i<oup[1].size(); ++i)
    {
        if(pha[oup[1][i]] != 3)
        {
            pha[oup[1][i]] |= 2;
            if(pha[oup[1][i]] == 3)
                ++answ;
        }
    }
    return answ;
}

int hypotesa(int mask)
{
    int answ = 0;
    memset(ok, 0, sizeof(ok));
    for(int i = 2; i < inp.size(); ++i)
    {
        int cur = i-2;
        int what = 1 << ((mask >> cur) & 1);
        for(int j = 0; j < inp[i].size(); ++j)
            if((ok[oup[i][j]] | pha[oup[i][j]]) != 3)
            {
                ok[oup[i][j]] |= what;
                if((ok[oup[i][j]] | pha[oup[i][j]]) == 3)
                    ++answ;
            }
    }
    return answ;
}

char buf[1000000];

void ad(char* c)
{
    string tmp;
    inp.push_back(vector<string>());
    for(int i = 0; c[i]; ++i)
        if(c[i] == ' ')
        {
            inp.back().push_back(tmp);
            vvv.push_back(tmp);
            tmp = "";
        }
        else
            tmp.push_back(c[i]);
    inp.back().push_back(tmp);
    vvv.push_back(tmp);
}

void test(int T)
{
    int answ = 1e9;
    inp.clear();
    vvv.clear();
    oup.clear();
    int n;
    scanf("%d",&n);
    getchar();
    for(int i = 0; i < n; ++i)
    {
        gets(buf);
        ad(buf);
    }
    sort(vvv.begin(), vvv.end());
    for(int i = 0; i < inp.size(); ++i)
    {
        oup.push_back(vector<int>());
        for(int j = 0; j < inp[i].size(); ++j)
            oup.back().push_back(lower_bound(vvv.begin(), vvv.end(), inp[i][j]) - vvv.begin());
    }
    
    glob = Init();
    answ = hypotesa(0);
    for(int i = 1; i < (1<<(n-2)); ++i)
        answ = min(answ, hypotesa(i));
    printf("Case #%d: %d\n", T, answ + glob);
    cerr<<T<<endl;
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
 2 30.0000 65.4321
 0.0001 50.0000
 100.0000 99.9000
 */

