//
//  main.cpp
//  Cookie Clicker Alpha
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

int main(int argc, const char * argv[])
{
    double C = 0, F = 0, X = 0, produce = 0;
    double max = 0, time = 0;
    DRI(T);
    
    for (int x = 1; x <= T; x++) {
        scanf("%lf %lf %lf",&C, &F, &X);
        ll cnt = 1;
        time = 0;
        produce = 2;
        max = X / produce;
        while(1){
            
            time += C / produce;
            produce += F;
            
            if(time + X / produce > max)break;
            max = time + X / produce;
            
            cnt++;

        }
        printf("Case #%d: %.7f\n",x,max);
    }
        
    
    return 0;
}
//while(1){
//    
//    for (ll i = 0; i < cnt; i++)
//    {
//        time = 0;
//        produce = 2;
//        for(ll j = 0; j < i; j++)
//        {
//            time += C / produce;
//            produce += F;
//        }
//        time += X / produce;
//    }
//}
