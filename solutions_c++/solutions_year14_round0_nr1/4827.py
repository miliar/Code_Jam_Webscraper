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

    FILE *ff=fopen("A-small-attempt0.in", "r"), *gg=fopen("A-small-attempt0.out", "w");

    int i,j,r,x,tt,ttt,res,brres,br[555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        for(i=0; i<=16; i++) br[i]=0;

        brres = 0;
        res = 0;

        fscanf(ff,"%d", &r);
        for(i=1; i<=4; i++) {
            for(j=0; j<4; j++) {
                fscanf(ff,"%d", &x);
                if (i==r) br[x]++;
            }
        }
        fscanf(ff,"%d", &r);
        for(i=1; i<=4; i++) {
            for(j=0; j<4; j++) {
                fscanf(ff,"%d", &x);
                if (i==r) {
                    br[x]++;
                    if (br[x]==2) {
                        brres++;
                        res = x;
                    }
                }
            }
        }

        fprintf(gg,"Case #%d: ", tt);
        if (brres == 0) fprintf(gg,"Volunteer cheated!\n");
        if (brres == 1) fprintf(gg,"%d\n", res);
        if (brres > 1) fprintf(gg,"Bad magician!\n");
    }

    fclose(ff); fclose(gg);

    return 0;
}
