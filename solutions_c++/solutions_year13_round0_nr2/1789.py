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

int r[155],c[155],a[155][155];

int main() {

    FILE *ff=fopen("B-large.in", "r"), *gg=fopen("B-large.out", "w");

    int n,m,i,j,h,b,tt,ttt;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%d%d", &n, &m);

        for(i=0; i<100; i++) {
            r[i]=0; c[i]=0;
        }

        for(i=0; i<n; i++) for(j=0; j<m; j++) fscanf(ff,"%d", &a[i][j]);

        printf("ok\n");

        b=1;
        for(h=100; h>=0; h--) if(b) {
            for(i=0; i<n; i++) if(b) {
                for(j=0; j<m; j++) if(b) {
                    if (a[i][j] == h) {
                        if (r[i] && c[j]) b=0;
                    }
                }
            }

            for(i=0; i<n; i++) if(b) {
                for(j=0; j<m; j++) if(b) {
                    if (a[i][j] == h) {
                        r[i]=1; c[j]=1;
                    }
                }
            }
        }

        fprintf(gg,"Case #%d: %s\n", tt, b ? "YES" : "NO");
    }

    fclose(ff); fclose(gg);

    return 0;
}
