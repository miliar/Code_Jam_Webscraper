/*
 Petar 'PetarV' Velickovic
 Task: Magic Trick
*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define DPRINTC(C) printf(#C " = %c\n", (C))
#define DPRINTS(S) printf(#S " = %s\n", (S))
#define DPRINTD(D) printf(#D " = %d\n", (D))
#define DPRINTLLD(LLD) printf(#LLD " = %lld\n", (LLD))
#define DPRINTLF(LF) printf(#LF " = %.5lf\n", (LF))

using namespace std;
typedef long long lld;
typedef unsigned long long llu;

int t;
double c, f, x;

int main()
{
    freopen("/Users/PetarV/CodeJam/B-large.in.txt","r",stdin);
    freopen("/Users/PetarV/CodeJam/B-large-out1.txt","w",stdout);
    
    scanf("%d",&t);
    for (int T=1;T<=t;T++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        double farm_time = 0;
        double t0 = 0.5*x;
        int farm_no = 0;
        
        while (true)
        {
            farm_time += c / (farm_no*f+2.0);
            farm_no++;
            double curr_t = farm_time + x / (farm_no*f + 2.0);
            if (curr_t > t0) break;
            t0 = curr_t;
        }
        
        printf("Case #%d: %.10lf\n", T, t0);
    }
    return 0;
}