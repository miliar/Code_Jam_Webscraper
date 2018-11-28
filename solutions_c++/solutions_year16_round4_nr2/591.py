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

int w[555];
double p[555],r[222][222];

int main() {

    FILE *ff=fopen("B-large.in", "r"), *gg=fopen("B-large.out", "w");

    int n,k,i,s,l,z,rs,ps,uk,t1,t2,tt,ms,pp1,pp2,prvih,ttt;
    double t,res;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d%d", &n, &k);

        for(i=0; i<n; i++) {
            fscanf(ff,"%lf", &p[i]);
        }

        sort(p,p+n);

        res = 0.0;
        for(prvih=0; prvih<=k; prvih++) {

            for(i=0; i<prvih; i++) w[i] = i;
            for(i=0; i<k-prvih; i++) w[prvih+i] = n-1-i;

            for(i=0; i<=k; i++) for(z=0; z<=k; z++) r[i][z] = 0.0;

            r[0][0] = 1.0;
            for(i=1; i<=k; i++) {
                //printf("-> %lf\n", p[w[i-1]]);
                for(z=0; z<=k/2; z++) {
                    r[i][z] = r[i-1][z] * (1.0 - p[w[i-1]]);
                    if (z>0) {
                        r[i][z] += r[i-1][z-1] * p[w[i-1]];
                    }
                }
            }

            if (r[k][k/2] > res) res = r[k][k/2];
        }

        fprintf(gg,"%.9lf\n", res);

    }

    fclose(ff); fclose(gg);

    return 0;
}
