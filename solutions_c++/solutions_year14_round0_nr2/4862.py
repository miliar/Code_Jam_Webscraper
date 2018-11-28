#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int main() {

    FILE *ff=fopen("B-small-attempt0.in", "r"), *gg=fopen("B-small-attempt0.out", "w");

    int tt,ttt;
    double c,f,x,k,t,r,res;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%lf%lf%lf", &c, &f, &x);

        k = 2.0;
        t = 0.0;

        res = x / 2.0;

        while( k <= 5*x ) {
            t += c / k;
            k += f;

            r = t + x/k;

            if (r < res) res = r;
        }

        fprintf(gg,"Case #%d: %.7lf\n", tt, res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
