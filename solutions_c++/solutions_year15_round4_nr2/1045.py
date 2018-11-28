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

    int n,i,tt,ttt;
    double V,X,t0,t1,v[555],x[555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d%lf%lf", &n, &V, &X);
        for(i=0; i<n; i++) {
            fscanf(ff,"%lf%lf", &v[i], &x[i]);
        }

        if (n == 1) {
            if (fabs(X-x[0]) > eps) {
                fprintf(gg,"IMPOSSIBLE\n");
            } else {
                fprintf(gg,"%.9lf\n", V/v[0]);
            }
        } else {
            if (fabs(x[0]-x[1]) < eps) {
                //printf("%d kako\n", tt);
                if (fabs(X-x[0]) > eps) {
                    fprintf(gg,"IMPOSSIBLE\n");
                } else {
                    fprintf(gg,"%.9lf\n", V/(v[0]+v[1]));
                }

            } else {
                if ((X > x[0]+eps && X > x[1]+eps) || (X+eps < x[0] && X+eps < x[1])) {
                    fprintf(gg,"IMPOSSIBLE\n");
                } else {
                    t1 = (V*(X-x[0]))/(v[1]*(x[1]-x[0]));
                    t0 = (V-v[1]*t1)/v[0];
                    if (t0 > t1) {
                        fprintf(gg,"%.9lf\n", t0);
                    } else {
                        fprintf(gg,"%.9lf\n", t1);
                    }
                }
            }
        }

        //fprintf(gg, "%d\n", res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
