#include <stdio.h>

int main(){
    int T,first,afirst[4][4],second,asecond[4][4],answer,repeat;
    FILE *in,*out;
    if((in=fopen("A-small-attempt1.in","r"))!=NULL)
        out=fopen("A-small-attempt1.out","w");
    fscanf(in,"%d",&T);
    for(int i=1;i<=T;i++){
        fscanf(in,"%d",&first);
        fscanf(in,"%d %d %d %d",&afirst[0][0],&afirst[0][1],&afirst[0][2],&afirst[0][3]);
        fscanf(in,"%d %d %d %d",&afirst[1][0],&afirst[1][1],&afirst[1][2],&afirst[1][3]);
        fscanf(in,"%d %d %d %d",&afirst[2][0],&afirst[2][1],&afirst[2][2],&afirst[2][3]);
        fscanf(in,"%d %d %d %d",&afirst[3][0],&afirst[3][1],&afirst[3][2],&afirst[3][3]);
        fscanf(in,"%d",&second);
        fscanf(in,"%d %d %d %d",&asecond[0][0],&asecond[0][1],&asecond[0][2],&asecond[0][3]);
        fscanf(in,"%d %d %d %d",&asecond[1][0],&asecond[1][1],&asecond[1][2],&asecond[1][3]);
        fscanf(in,"%d %d %d %d",&asecond[2][0],&asecond[2][1],&asecond[2][2],&asecond[2][3]);
        fscanf(in,"%d %d %d %d",&asecond[3][0],&asecond[3][1],&asecond[3][2],&asecond[3][3]);
        repeat=0;
        for(int j=0;j<4;j++)
        for(int k=0;k<4;k++){
            if(afirst[first-1][j]==asecond[second-1][k]){
                answer=afirst[first-1][j];
                repeat++;
            }
        }
        fprintf(out,"CASE #%d: ",i);
        if(repeat==0) fprintf(out,"Volunteer cheated!\n");
        else if(repeat==1) fprintf(out,"%d\n",answer);
        else fprintf(out,"Bad magician!\n");
    }
    return 0;
}
