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

    FILE *ff=fopen("D-large.in", "r"), *gg=fopen("D-large.out", "w");

    int n,i,j,tt,ttt,res1,res2;
    double a[5555],b[5555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%d", &n);

        for(i=0; i<n; i++) fscanf(ff,"%lf", &a[i]);
        for(i=0; i<n; i++) fscanf(ff,"%lf", &b[i]);

        sort(a,a+n);
        sort(b,b+n);

        //for(i=0; i<n; i++) printf("%.3lf ", a[i]); printf("\n");
        //for(i=0; i<n; i++) printf("%.3lf ", b[i]); printf("\n");

        res1 = n;
        i=0; j = 0;
        while(i<n && j<n) {
            while(i<n && a[i] < b[j]) {
                i++;
                res1--;
            }
            i++; j++;
        }

        res2 = n;
        i=0; j=0;
        while(i<n && j<n) {
            while(j<n && b[j] < a[i]) {
                j++;
            }
            if (j<n) {
                j++;
                res2--;
            }
            i++;
        }

        fprintf(gg,"Case #%d: %d %d\n", tt, res1, res2);
        //printf("-> %d %d\n", res1, res2);
        //printf("-----\n");
    }

    fclose(ff); fclose(gg);

    return 0;
}
