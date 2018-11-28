#include <stdio.h>

#define SOUBOR_VSTUP "B_lawnmover.in"
#define SOUBOR_VYSTUP "B_lawnmover.out"

#define MAXNM 110

int main() {
    FILE *vstup = stdin;
    vstup = fopen(SOUBOR_VSTUP,"r");
    FILE *vystup = stdout;
    vystup = fopen(SOUBOR_VYSTUP,"w");

    int max_x[MAXNM];
    int max_y[MAXNM];

    int grass[MAXNM][MAXNM];

    int T;
    fscanf(vstup,"%d\n",&T);
    for(int i=1;i<=T;i++) {
        int N, M;
        fscanf(vstup,"%d %d\n",&N,&M);
        for(int y=0;y<N;y++) {
            for(int x=0;x<M;x++) fscanf(vstup,"%d",&grass[x][y]);
        }

        //compute max_x and max_y
        for(int y=0;y<N;y++) max_x[y]=0;
        for(int x=0;x<M;x++) {
            max_y[x]=0;
            for(int y=0;y<N;y++) {
                if(max_y[x]<grass[x][y]) max_y[x]=grass[x][y];
                if(max_x[y]<grass[x][y]) max_x[y]=grass[x][y];
            }
        }

        //control if each place is reachable by lawnmover
        bool reachable=true;
        for(int x=0;x<M;x++) {
            for(int y=0;y<N;y++) {
                if(grass[x][y]<max_x[y] && grass[x][y]<max_y[x]) reachable=false;
            }
        }

        if(reachable) fprintf(vystup,"Case #%d: YES\n",i);
        else fprintf(vystup,"Case #%d: NO\n",i);
    }

    return 0;
}
