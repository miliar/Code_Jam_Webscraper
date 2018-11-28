#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>
using namespace std;
int main() {
    int tc,tci,i,j,N,M,k,rect[100][100],breakcase,possible;
    FILE *fp = fopen("C:/ikj/input.txt","r");
    FILE *fp2 = fopen("C:/ikj/output.txt","w");
    fscanf(fp,"%d",&tc);
    for(tci=0;tci<tc;tci++) {
        fscanf(fp,"%d%d",&N,&M);
        for(i=0;i<N;i++) {
            for(j=0;j<M;j++)
                fscanf(fp,"%d",&rect[i][j]);
        }
        breakcase=0;
        for(i=0;((i<N)&&(breakcase!=1));i++) {
            for(j=0;((j<M)&&(breakcase!=1));j++) {
                possible=0;
                for(k=0;k<N;k++) {
                    if(rect[k][j] > rect[i][j]) {possible=1;break;}
                }
                if(possible==0) continue;
                for(k=0;k<M;k++) {
                    if(rect[i][k] > rect[i][j]) {possible=2;break;}
                }
                if(possible==2) {
                    fprintf(fp2,"Case #%d: NO\n",tci+1);
                 //   fprintf(fp2,"%d %d %d\n",i,j,rect[i][j]);
                    breakcase=1;
                }
            }
        }
        if(breakcase!=1) fprintf(fp2,"Case #%d: YES\n",tci+1);
    }
}
