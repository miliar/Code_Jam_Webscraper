#include <stdio.h>
int main()
{
    int i,j,k,T,N,M,max,rkey,ckey,rmax,cmax,yes;
    int map[100][100],cut[100][100];
    int rm[100],cm[100];
    FILE* iptr;
    FILE* optr;
    iptr = fopen("B-large.in","r");
    optr = fopen("out.txt","w");
    fscanf(iptr,"%d",&T);
    for(i = 1; i <= T; i++) {
        fscanf(iptr,"%d%d",&N,&M);
        for(j = 0; j < N; j++) {
            max = 0;
            for(k = 0; k < M; k++) {
                fscanf(iptr,"%d",&map[j][k]);
                max = (map[j][k] > max) ? map[j][k] : max;
                cut[j][k] = 100;
            }
            rm[j] = max;
        }
        for(j = 0; j < M; j++) {
            max = 0;
            for(k = 0; k < N; k++) {
                max = (map[k][j] > max) ? map[k][j] : max;
            }
            cm[j] = max;
        }

        while(1) {
            rmax = 0;rkey = -1;
            for(j = 0; j < N; j++) {
                if( rm[j] > rmax ) {
                    rmax = rm[j];
                    rkey = j;
                }
            }

            cmax = 0;ckey = -1;
            for(j = 0; j < M; j++) {
                if( cm[j] > cmax ) {
                    cmax = cm[j];
                    ckey = j;
                }
            }
            if( rmax == 0 && cmax == 0 ) break; 
            if( rmax > cmax ) {
                rm[rkey] = 0;
                for(j = 0; j < M; j++) {
                    if( cut[rkey][j] > rmax ) {
                        cut[rkey][j] = rmax;
                    }
                }
            } 
            else {
                cm[ckey] = 0;
                for(j = 0; j < N; j++) {
                    if( cut[j][ckey] > cmax ) {
                        cut[j][ckey] = cmax;
                    }
                }
            }
        }
        yes = 1;
        for(j = 0; j < N; j++) {
            for(k = 0; k < M; k++) {
                if( cut[j][k] != map[j][k] )
                    yes = 0;
            }
        }
        if( yes )
            fprintf(optr,"Case #%d: YES\n",i);
        else
            fprintf(optr,"Case #%d: NO\n",i);
    }
    fclose(iptr);
    fclose(optr);
    return 0;
}
