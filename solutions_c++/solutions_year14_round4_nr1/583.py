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

int s[333555];
bool mark[333555];

int main() {

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");

    int n,x,i,j,tt,ttt,res;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d%d", &n, &x);

        for(i=0; i<n; i++) {
            fscanf(ff,"%d", &s[i]);
            mark[i] = false;
        }

        sort(s,s+n);

        res = 0;
        j = n-2;
        for(i=n-1; i>=0; i--) {
            if (mark[i]) continue;

            for(j=i-1; j>=0; j--) {
                if (mark[j]) continue;
                if (s[i] + s[j] <= x) {
                    mark[j] = true;
                    break;
                }
            }
            res++;

            /*j = i-1;

            while(j>=0 && s[i]+s[j] > x) {
                j--;
                while(j>=0 && mark[j]) j--;
            }

            if (j>=0) {
                mark[j] = true;
            }

            res++;*/
        }

        fprintf(gg, "%d\n", res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
