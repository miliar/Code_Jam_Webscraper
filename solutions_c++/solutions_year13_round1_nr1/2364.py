#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
const double PI = 1.0;

#define ipow(a,b) (ull)pow((double)a, (double)b)

const char in[]  = "A-small-attempt0.in.txt";
const char out[] = "A.out.txt";

double area = 0.0;

int main(void)
{
    freopen(in, "rt", stdin);
    freopen(out, "wt", stdout);
    
    int T = 0;
    scanf("%d", &T);
    ull i = 0;
    
    for (int casenum = 1; casenum <= T; ++casenum)
    {
        ull r, t;
        scanf("%llu%llu", &r, &t);
        
        double totalbk = 0.0;
        double totalall = 0.0;
        
        for (i = 0; totalbk <= (double)t; ++i)
        {
            area = PI*(r+i)*(r+i) - totalall;
            totalall += area;
            if ( i%2 ) // black
            {
                totalbk += area;
            }
        }
        
        printf("Case #%d: %llu\n", casenum, (i-1)/2);
    }
}
