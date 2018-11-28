//
//  main.cpp
//  topcoder
//
//  Created by Jun Chen on 4/4/14.
//  Copyright (c) 2014 Jun Chen. All rights reserved.
//

#include <iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<ctime>
#include<set>
#include<string>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;
const int MAX=200005;
const int inf=1<<30;
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define ll long long
#define PB push_back
#define PII pair<int,int>
#define MP(x,y) make_pair(x,y)
int a[5][5], b[111];
int main(int argc, const char * argv[])
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, cas = 0;
    cin >> T;
    int x, y;
    while (T--) {
        cin >> x;
        memset(b, 0, sizeof(b));
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                cin >> a[i][j];
        for (int j = 1; j <= 4; j++)
            b[a[x][j]]++;
        cin >> y;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                cin >> a[i][j];
        for (int j = 1; j <= 4; j++)
            b[a[y][j]]++;
        int cnt = 0;
        for (int i = 1; i <= 16; i++)
            if (b[i] == 2)
                cnt++, x = i;
        printf("Case #%d: ", ++cas);
         if (cnt == 0)
             puts("Volunteer cheated!");
        else if (cnt == 1)
            cout << x << endl;
        else
            puts("Bad magician!");
    }
    return 0;
}

