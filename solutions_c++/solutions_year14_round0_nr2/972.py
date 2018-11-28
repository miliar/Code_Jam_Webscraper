
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

double C,F,X;

double simulate(int farms) {
    double t=0;
    double r=2;
    rep(i,farms) {
        t += C/r;
        r += F;
    }
    return t+(X/r);
}

double tsearch(int a, int b) {
    //printf("%d %d\n",a,b);
    if ((b-a)<3) return min(simulate(a),min(simulate(a+1),simulate(a+2)));
    int offset = (b-a)/3;
    double s1 = simulate(a+offset);
    double s2 = simulate(a+2*offset);
    if (s1 < s2) return tsearch(a,a+2*offset);
    else return tsearch(a+offset,b);
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    rep(tc, T) {
        cin >> C >> F >> X;
        //rep(i,50) printf("sim(%d) = %lf\n",i,simulate(i));
        printf("Case #%d: %.10lf\n",tc+1,tsearch(0,80000000));
    }
}

