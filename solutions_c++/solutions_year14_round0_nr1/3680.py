//
//  main.cpp
//  Magic Trick
//
//  Created by Adam Plánský on 12/04/14.
//  Copyright (c) 2014 Adam Plansky. All rights reserved.
//

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

int game1[4][4];
int game2[4][4];
int main(int argc, const char * argv[])
{
    DRI(T)
    int T1 = 1;
    while(T--)
    {
        DRI(A);
        FOR(i,0,4)
        {
            RIIII(game1[i][0],game1[i][1],game1[i][2],game1[i][3]);
        }
        DRI(B);
        FOR(i,0,4)
        {
            RIIII(game2[i][0],game2[i][1],game2[i][2],game2[i][3]);
        }
        int match = 0;
        int m1 = 0;
        FOR(i, 0, 4)
        {
            FOR(j,0,4)
            {
                if(game1[A-1][i] == game2[B-1][j])
                {
                    match++;
                    m1 = game2[B-1][j];
                }
            }
        }
        cout << "Case #" << T1++ << ": " ;
        if(match == 1) cout << m1 << endl;
        else if(match > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
        
    }
    return 0;
}

