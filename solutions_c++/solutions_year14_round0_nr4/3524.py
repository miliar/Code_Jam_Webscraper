//
//  main.cpp
//  D Deceitful War
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

double naomi[1021];
double ken[1021];

int main(int argc, const char * argv[])
{
    DRI(T);
    vector<double> naomi;
    vector<double> ken;
    double dummy = 0;
    FOR(x, 1, T+1)
    {
        naomi.clear(); ken.clear();
        DRI(n);
        FOR(i, 0, n)
        {
            scanf("%lf",&dummy);
            naomi.push_back(dummy);
        }
        FOR(i, 0, n)
        {
            scanf("%lf",&dummy);
            ken.push_back(dummy);
        }
        
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        int win = 0;
        
        //cheated
        int her = 0, him = 0;
        int lastHim = n-1, lastHer = n-1;
        while(her < n)
        {
            if(naomi[her] < ken[him])
            {
                her++;
                lastHim--;
            } else {
                her++;
                him++;
                win++;
            }
        }
        int win2 = 0;
        her = him = 0;
        lastHim = n-1;
        while(lastHer >= 0)
        {

            if(naomi[lastHer] > ken[lastHim])
            {
                him++;
                lastHer--;
                win2++;
            } else {
                lastHer--;
                lastHim--;
            }
        }

        cout << "Case #" << x  << ": "<< win << " " << win2 << endl;
    }
    return 0;
}

