#include<stdio.h>
#include<iostream>

int main() {
    FILE* fin = fopen("D-small-attempt0.in","r");
    FILE* fout = fopen("out.txt","w");
    int cc=1,t;
    fscanf(fin,"%d",&t);
    while(cc<=t) {
        int x,r,c;
        std::string winner;
        fscanf(fin,"%d %d %d",&x,&r,&c);
        if(r<c) {
            int temp=r;
            r=c;
            c=temp;
        }
        if(x==1)
            winner="GABRIEL";
        else if(x==2)
            winner=(r*c%2==0) ? "GABRIEL" : "RICHARD";
        else if(x==3)
            winner=(r>=3 && c>=2 && r*c%3==0) ? "GABRIEL" : "RICHARD";
        else
            winner=(r>=4 && c>=3 && r*c%4==0) ? "GABRIEL" : "RICHARD";
        fprintf(fout,"Case #%d: ",cc);
        if(winner=="GABRIEL")
            fprintf(fout,"GABRIEL\n");
        else
            fprintf(fout,"RICHARD\n");
        cc++;
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
