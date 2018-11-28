#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char * argv[])
{
    int t;
    scanf("%d", &t);
    while(t--) {
        double c,f,x;
        scanf("%lf %lf %lf", &c, &f, &x);
        // T = min(x/(v+f), (x-c)/v) 
        double v=2, s=0, t=0, n=0;
        while(s<x) {
            if ( s >= c ) {
                double tn = (x-c)/v;
                double ty = x/(v+f);
                if (tn<ty) {
//                    printf("not buying is faster\n");
                    t+=(x-c)/v;
                    s = x;
                } else {
                    ++n;
                    s-=c;
                    v+=f;
//                    printf("buying\n");
                }
            } else {
//                printf("not enough to buy\n");
            }
            if(s+c<=x) 
            {
                t+=c/v;
                s+=c;
            } else {
                t+=(x-s)/v;
                s = x;
            }
        }
        static int id = 0;
        printf("Case #%d: %.7f\n", ++id, t);
    }
    return 0;
}
